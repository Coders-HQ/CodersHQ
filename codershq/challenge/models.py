from ckeditor.fields import RichTextField
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from codershq.users.models import User


class Challenge(models.Model):
    """Main challenge model"""

    # the name of the challenge
    name = models.CharField(_("Name of Challenge"), max_length=100)
    # host name
    host_name = models.CharField(_("Challenge host name"), max_length=100)
    # short description of the challenge
    host_logo = models.ImageField(_("Your logo"), blank=True, null=True)
    short_description = models.TextField(
        _("Short challenge description"),
        max_length=150,
        help_text="Short description of the challenge",
    )
    # full challenge description
    description = RichTextField(help_text="Detailed descripton of the challenge")
    # how the challenge will be evaluated
    evaluation = RichTextField(help_text="Detailed evaluation criteria")
    # the reward structure
    reward = RichTextField(help_text="detailed reward structure")
    # addition rule detail
    rules = RichTextField(
        _("Rules (optional)"),
        help_text="Rules related to submission (optional)",
        null=True,
        blank=True,
    )
    # is the reward cash
    is_monetary = models.BooleanField(_("Is the reward a cash prize?"), default=False)
    # total reward if its monetary
    prize_pool = models.IntegerField(_("Total prize pool"), default=0)
    # reward if its not monetary
    alternate_reward = models.CharField(
        _("Reward if its not monetary"), max_length=50, null=True, blank=True
    )
    # image to be placed in the smaller card and banner
    image = models.ImageField(
        _("Challenge Image"),
        upload_to="challenges/image/",
        blank=True,
        default=None,
        null=None,
    )
    # test and train data
    train_data = models.URLField(
        _("Train data link"), null=True, blank=True, help_text="Link to train data set"
    )
    test_data = models.URLField(
        _("Test data link"), null=True, blank=True, help_text="Link to test data set"
    )
    # github link for additional information
    github_link = models.URLField(
        _("Challenge github link"), default=None, blank=True, null=True
    )
    # website if companies need to add more data
    website = models.URLField(_("Website link"), null=True, blank=True)
    # end date of the challenge
    end_date = models.DateTimeField(_("Challenge end date"))
    # timeline in detail if needed
    timeline = RichTextField(null=True, blank=True, help_text="Detailed timeline")
    # 1 st place
    gold_award = models.ForeignKey(
        User, related_name="gold_award", on_delete=models.CASCADE, null=True, blank=True
    )
    # second place
    silver_award = models.ForeignKey(
        User,
        related_name="silver_award",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # third place
    bronze_award = models.ForeignKey(
        User,
        related_name="bronze_award",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )
    # user who created the challenge
    owner = models.ForeignKey(User, related_name="owner", on_delete=models.CASCADE)
    # participants
    participants = models.ManyToManyField(User, related_name="participants", blank=True)
    # submission email
    submission_email = models.EmailField(_("Email for submission"))

    def __str__(self) -> str:
        return "Challenge: " + self.name

    @property
    def is_over(self):
        """return true if challenge is over"""
        return self.end_date < timezone.now()

    @property
    def has_data(self):
        # returns true if has either test or train data
        if self.train_data is not None or self.test_data is not None:
            return True
        return False

    def get_reward(self):
        """return reward based on selected"""
        if self.is_monetary:
            return "AED " + str("{:,}".format(self.prize_pool))
        else:
            return self.alternate_reward

    def get_time_left(self):
        if not self.is_over:
            time_now = timezone.now()
            end_date = self.end_date
            delta = end_date - time_now

            days_left = delta.days
            weeks_left = delta.days // 7
            months_left = delta.days // 30

            if days_left <= 7:
                return str(days_left) + " day(s) to go"

            if weeks_left <= 4:
                return str(weeks_left) + " week(s) to go"

            return str(months_left) + " month(s) to go"
        return "Ended"

    @property
    def end_date_pretty(self):
        return self.end_date.strftime("%d %B, %Y")

    def save(self, *args, **kwargs):
        """Validate form"""
        validate_challenge(self)
        super(Challenge, self).save(*args, **kwargs)

    def clean(self):
        """Validate form"""
        validate_challenge(self)

    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse("challenge:challenge-detail", kwargs={"pk": self.pk})


def validate_challenge(challenge: Challenge):
    # dont save if is_monetary is True and prize_pool = 0
    if challenge.is_monetary and challenge.prize_pool <= 0:
        raise ValidationError("Cannot have both is_monetary True and prize_pool = 0")

    # dont save if two reward types are chosen
    if challenge.prize_pool > 0 and challenge.alternate_reward is not None:
        raise ValidationError(
            "Cannot have both prize_pool and alternate reward at the same time"
        )

    # prize must be chosen
    if challenge.prize_pool <= 0 and challenge.alternate_reward is None:
        raise ValidationError(
            "Prize pool cant be zero and Alternate reward empty at the same time"
        )

    # cannot choose winner before end date
    if not challenge.is_over:
        if (
            challenge.gold_award is not None
            or challenge.silver_award is not None
            or challenge.bronze_award is not None
        ):
            raise ValidationError("Cannot choose winners before end date of challenge")
