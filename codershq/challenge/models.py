from django.db import models
from django.db.models.fields import DateTimeField
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from codershq.users.models import User
from django.urls import reverse


class Challenge(models.Model):
    """Main challenge model"""

    # the name of the challenge
    name = models.CharField(_("Name of Challenge"), max_length=100)
    # short description of the challenge
    short_description = models.TextField(
        _("Short challenge description"), max_length=150, help_text="Short description of the challenge"
    )
    # full challenge description
    description = RichTextField()
    # how the challenge will be evaluated
    evaluation = RichTextField()
    # the reward structure
    reward = RichTextField()
    # total reward
    prize_pool = models.IntegerField(_("Total prize pool"), default=0)
    # image to be placed in the smaller card and banner
    image = models.ImageField(_("Challenge Image"), upload_to="challenges/image/", blank=True, default=None, null=None)
    # test and train data
    train_data = models.URLField(_("Train data link"), null=True, blank=True, help_text="Link to train data set")
    test_data = models.URLField(_("Test data link"), null=True, blank=True, help_text="Link to test data set")
    # github link for additional information
    github_link = models.URLField(_("Challenge github link"),  default=None, blank=True, null=True)
    # website if companies need to add more data
    website = models.URLField(_("Website link"), null=True, blank=True)
    # end date of the challenge
    end_date = models.DateTimeField(_("Challenge end date"))
    # winner announcement 
    winner = models.ForeignKey(User, related_name='winner',on_delete=models.CASCADE, null=True, blank=True)
    # user who created the challenge
    owner = models.ForeignKey(User, related_name='owner',on_delete=models.CASCADE)
    # participants
    participants = models.ManyToManyField(User, related_name='participants', null=True, blank=True)


    def __str__(self) -> str:
        return "Challenge: " + self.name


    def get_absolute_url(self):
        """Returns the url to access a particular instance of the model."""
        return reverse('challenge:challenge-detail', kwargs={'pk' : self.pk})

