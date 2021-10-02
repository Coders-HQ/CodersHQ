import pytest
from codershq.challenge.models import SubmittedCode, Challenge
from codershq.users.models import User
from codershq.users.tests.factories import UserFactory
import tempfile
from django import urls
from django.test import RequestFactory
from codershq.challenge.views import ChallengeList, ChallengeDetail, ChallengeEnrol

pytestmark = pytest.mark.django_db(transaction=True)

def test_model():
    proto_user = UserFactory.build()
    user = User()
    user.username = proto_user.username
    user.password1 = proto_user._password
    user.password2 = proto_user._password
    user.save()

    length = len(Challenge.objects.all())
    assert length == 0

    challenge = Challenge()
    challenge.name = 'test'
    challenge.description = 'testing'
    challenge.logo = tempfile.NamedTemporaryFile(suffix=".jpeg").name
    challenge.github_link = 'http://test.com'
    challenge.website = 'http://test.com'
    challenge.save()

    length = len(Challenge.objects.all())
    assert length == 1

    length = len(SubmittedCode.objects.all())
    assert length == 0

    submitted_code = SubmittedCode()
    submitted_code.user = user
    submitted_code.challenge = challenge
    submitted_code.code_file = tempfile.NamedTemporaryFile(suffix=".zip").name
    submitted_code.save()

    length = len(SubmittedCode.objects.all())
    assert length == 1
    assert SubmittedCode.objects.filter(user = user).exists()
    assert SubmittedCode.objects.filter(challenge = challenge).exists()


class TestViews:
    def test_challenge_list(self, user: User, rf: RequestFactory):
        url = urls.reverse('challenge:list')
        request = rf.get(url)
        request.user = UserFactory()
        challenge_list = ChallengeList.as_view()
        response = challenge_list(request, username = user.username)
        assert response.status_code == 200

    def test_challenge_detail(self, user: User, rf: RequestFactory):
        challenge = Challenge()
        challenge.name = 'test'
        challenge.description = 'testing'
        challenge.logo = tempfile.NamedTemporaryFile(suffix=".jpeg").name
        challenge.github_link = 'http://test.com'
        challenge.website = 'http://test.com'
        challenge.save()
        length = len(Challenge.objects.all())
        assert length == 1

        url = urls.reverse('challenge:detail', kwargs={'id': challenge.id})
        request = rf.get(url)
        request.user = UserFactory()
        challenge_detail = ChallengeDetail.as_view()
        response = challenge_detail(request, username = user.username, id = challenge.id)
        assert response.status_code == 200

    def test_challenge_enrol(self, user: User, rf: RequestFactory):
        challenge = Challenge()
        challenge.name = 'test'
        challenge.description = 'testing'
        challenge.logo = tempfile.NamedTemporaryFile(suffix=".jpeg").name
        challenge.github_link = 'http://test.com'
        challenge.website = 'http://test.com'
        challenge.save()
        length = len(Challenge.objects.all())
        assert length == 1

        url = urls.reverse('challenge:enroll', kwargs={'id': challenge.id})
        request = rf.get(url)
        request.user = UserFactory()
        challenge_enrol = ChallengeEnrol.as_view()
        response = challenge_enrol(request, username = user.username, id = challenge.id)
        assert response.status_code == 200
        assert Challenge.objects.filter(prticipant_teams=user.teams).exists()
   