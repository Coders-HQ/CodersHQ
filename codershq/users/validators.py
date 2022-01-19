"""
Custom model validators
"""

import re

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# from users.CHQ_Scoring.github_score import CHQScore
# from django.conf import settings
# from users.utils import get_github_username


def validate_github_profile(value):
    """validate github profile"""

    pattern = r"^github.com\/[a-zA-Z0-9]+(?:-[a-zA-Z0-9]+)*\/?$"
    if re.search(pattern, value) is None:
        raise ValidationError(
            _("%(value)s is not a valid github profile."),
            params={"value": value},
        )


# def validate_github_user(value):
#     """make sure github user is an actual user, consumes one api call"""

#     user_name = get_github_username(value)
#     chq_score = CHQScore(settings.GITHUB_TOKEN)
#     if chq_score.check_user_exists(user_name) == False:
#         raise ValidationError(_('github username %(value)s doesnt exist'),
#                               params={'value': user_name},)
