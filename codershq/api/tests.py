import pytest
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_token_obtain_and_admin_endpoint_permissions(django_user_model):
    client = APIClient()

    admin_password = "admin-pass-123"
    admin = django_user_model.objects.create_user(
        username="admin_user",
        password=admin_password,
        is_staff=True,
        is_superuser=True,
    )

    user_password = "user-pass-123"
    django_user_model.objects.create_user(
        username="normal_user",
        password=user_password,
        is_staff=False,
        is_superuser=False,
    )

    # Unauthenticated should be rejected (IsAdminUser)
    unauth_resp = client.get("/api/users/data/")
    assert unauth_resp.status_code in (401, 403)

    # Normal user token -> still forbidden
    token_resp = client.post(
        "/api/token/",
        {"username": "normal_user", "password": user_password},
        format="json",
    )
    assert token_resp.status_code == 200
    access = token_resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {access}")
    forbidden_resp = client.get("/api/users/data/")
    assert forbidden_resp.status_code in (401, 403)

    # Admin token -> allowed
    token_resp = client.post(
        "/api/token/",
        {"username": admin.username, "password": admin_password},
        format="json",
    )
    assert token_resp.status_code == 200
    admin_access = token_resp.data["access"]
    client.credentials(HTTP_AUTHORIZATION=f"Bearer {admin_access}")

    ok_resp = client.get("/api/users/data/")
    assert ok_resp.status_code == 200
    assert "data" in ok_resp.json()


@pytest.mark.django_db
def test_legacy_api_token_auth_returns_token_field(django_user_model):
    client = APIClient()

    password = "pass-123"
    django_user_model.objects.create_user(username="legacy_user", password=password)

    resp = client.post(
        "/api-token-auth/",
        {"username": "legacy_user", "password": password},
        format="json",
    )
    assert resp.status_code == 200
    assert "token" in resp.data
    assert "access" in resp.data
    assert "refresh" in resp.data
