# Simple Fastapi Endpoint

This module defines a simple FastAPI application with one main API endpoint. The purpose of this endpoint is to retrieve information about a user associated with the HNG program based on their Slack name and track.

## API Endpoint

### Get User Information

- **URL:** `/api`
- **HTTP Method:** GET

#### Request Parameters

- `slack_name` (str): The Slack name of the user.
- `track` (str): The track the user is in.

#### Example Request

```http
GET /api?slack_name=johndoe&track=backend
```

#### Response

- Status Code: 200 OK
- Content-Type: application/json

#### Example Response

```json
{
    "slack_name": "johndoe",
    "current_day": "Wednesday",
    "utc_time": "2023-09-06T12:34:56Z",
    "track": "backend",
    "github_file_url": "https://github.com/Cofucan/simple_fastapi_endpoint/blob/main/main.py",
    "github_repo_url": "https://github.com/Cofucan/simple_fastapi_endpoint",
    "status_code": 200
}
```

#### Description

This endpoint allows you to retrieve information about an HNG user.
It expects two query parameters: `slack_name` and `track`.
After receiving the parameters, it returns a JSON response containing the following information:

- `slack_name`: The Slack name of the user.
- `current_day`: The current day of the week in UTC time.
- `utc_time`: The current UTC time in the format "YYYY-MM-DDTHH:MM:SSZ".
- `track`: The track the user is in.
- `github_file_url`: URL to the main.py file of this FastAPI application on GitHub.
- `github_repo_url`: URL to the GitHub repository of this FastAPI application.
- `status_code`: The HTTP status code, which will always be 200 for successful requests.


### Running the Application

To run this FastAPI application locally, follow these steps:

1. Clone the GitHub repository:

    ```shell
    git clone https://github.com/Cofucan/simple_fastapi_endpoint.git
    ```

2. Install the required dependencies using pip or pip3:

    ```shell
    pip install -r requirements.txt
    ```

3. Change directory to the project folder:

    ```shell
    cd simple_fastapi_endpoint
    ```

4. Run the application using Uvicorn:

    ```shell
    uvicorn main:app --reload
    ```

The API will be available at http://localhost:8000.

### Unit Tests

There are a few unit tests available, implemented using `pytest`. You can run the tests using:

```python
pytest
```
