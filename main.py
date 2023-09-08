from datetime import datetime, timezone
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/api/{slack_name}/{track}")
async def get_user_info(slack_name: str, track: str):
    """
    Retrieve user information.

    Args:
        slack_name (str): The Slack name of the user.
        track (str): The track the user is in.

    Returns:
        dict: A dictionary containing user information.
    """
    return {
        "slack_name": slack_name,
        "current_day": datetime.now().strftime('%A'),
        "utc_time": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "track": track,
        "github_file_url": "www",
        "github_repo_url": "www",
        "status_code": 200,
    }
