"""This module defines an endpoint for getting a HNG user's information."""
from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello fellow"}


@app.get("/api")
async def get_user_info(slack_name: str, track: str):
    """
    Retrieve user information.

    Args:
        slack_name (str): The Slack name of the user.
        track (str): The track the user is in.

    Returns:
        dict: A dictionary containing user information.
    """
    now = datetime.now(timezone.utc)

    return {
        "slack_name": slack_name,
        "current_day": now.strftime('%A'),
        "utc_time": now.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": "www",
        "github_repo_url": "www",
        "status_code": 200,
    }
