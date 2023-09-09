"""Unit test module for the `get_user_info` function."""

import pytest
from main import get_user_info


class TestGetUserInfo:

    #  Tests that the function retrieves user information with valid slack_name and track parameters.
    @pytest.mark.asyncio
    async def test_valid_slack_name_and_track(self):
        response = await get_user_info("slack_name", "track")
        assert response["slack_name"] == "slack_name"
        assert response["track"] == "track"
        assert response["status_code"] == 200

    #  Tests that the function retrieves user information with slack_name and track parameters containing special characters.
    @pytest.mark.asyncio
    async def test_special_characters_in_slack_name_and_track(self):
        response = await get_user_info("!@#$%^&*()", "!@#$%^&*()")
        assert response["slack_name"] == "!@#$%^&*()"
        assert response["track"] == "!@#$%^&*()"
        assert response["status_code"] == 200

    #  Tests that the function retrieves user information with slack_name and track parameters containing numbers.
    @pytest.mark.asyncio
    async def test_numbers_in_slack_name_and_track(self):
        response = await get_user_info("12345", "67890")
        assert response["slack_name"] == "12345"
        assert response["track"] == "67890"
        assert response["status_code"] == 200

    #  Tests that the function retrieves user information with slack_name and track parameters containing uppercase and lowercase letters.
    @pytest.mark.asyncio
    async def test_uppercase_and_lowercase_letters_in_slack_name_and_track(self):
        response = await get_user_info("SlackName", "Track")
        assert response["slack_name"] == "SlackName"
        assert response["track"] == "Track"
        assert response["status_code"] == 200

    #  Tests that the function retrieves user information with slack_name and track parameters containing the maximum allowed length.
    @pytest.mark.asyncio
    async def test_maximum_length_in_slack_name_and_track(self):
        response = await get_user_info("a" * 100, "b" * 100)
        assert response["slack_name"] == "a" * 100
        assert response["track"] == "b" * 100
        assert response["status_code"] == 200

    #  Tests that the function retrieves user information with slack_name and track parameters containing the minimum allowed length.
    @pytest.mark.asyncio
    async def test_minimum_length_in_slack_name_and_track(self):
        response = await get_user_info("a", "b")
        assert response["slack_name"] == "a"
        assert response["track"] == "b"
        assert response["status_code"] == 200
