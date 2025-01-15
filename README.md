# aws-google-calendar-automation
# Automating Google Calendar Event Creation Using AWS Lambda

## Overview
I use Google Calendar to organize my daily life, and I wanted a way to easily create Google Calendar events. After some research, I decided AWS Lambda is a great service for what I wanted to achieve. I started with setting up the Google Calendar API on the Google Cloud Console. Then, I created a Python script to parse natural language of event details as JSON text. Finally, I created the AWS Lambda Function to execute the python script. I connected the function to the AWS API Gateway so that external services can call the API Gateway to execute event creation.

Summary: The workflow is designed to accept natural language or structured JSON input via an HTTP API, parse the input into the appropriate format, and interact with the Google Calendar API to schedule events.

---

## Workflow Diagram

```
User Input -> API Gateway -> Lambda Function -> Google Calendar API -> Event Scheduled
```

### Detailed Workflow Steps:
1. **User Input**: The user sends a request (natural language or structured JSON) to the API Gateway endpoint.
2. **API Gateway**: Acts as the entry point, validating the incoming HTTP request and triggering the Lambda function.
3. **Lambda Function**: The core of the workflow:
   - Parses the incoming request.
   - Converts the input into the Google Calendar API’s required format.
   - Sends a request to the Google Calendar API to create the event.
   - Returns a success or error response to the user.
4. **Google Calendar API**: Processes the event creation request and schedules the event in the user’s calendar.
5. **Response**: The Lambda function returns a confirmation or error message to the user via the API Gateway.

---

## Implementation Details

### 1. **Python Script for Lambda Function**
This Python script processes the incoming request, interacts with the Google Calendar API, and handles authentication and event creation.

#### Code:
```python
import json
import re
from datetime import datetime, timedelta
import requests

GOOGLE_TOKEN_URL = "https://oauth2.googleapis.com/token"
GOOGLE_CALENDAR_API_URL = "https://www.googleapis.com/calendar/v3/calendars/primary/events"

# Function to refresh the access token
def refresh_access_token(refresh_token, client_id, client_secret):
    payload = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token'
    }

    response = requests.post(GOOGLE_TOKEN_URL, data=payload)
    if response.status_code == 200:
        tokens = response.json()
        return tokens['access_token']
    else:
        raise Exception(f"Failed to refresh token: {response.status_code} {response.text}")

# Lambda handler function
def lambda_handler(event, context):
    # Replace these with your actual credentials
    CLIENT_ID = "1042953427809-tsou3jq0m9o0rm3tmt609dj26i3hh6av.apps.googleusercontent.com"
    CLIENT_SECRET = "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"
    REFRESH_TOKEN = "1//04oMlHg9x8ugACgYIARAAGAQSNwF-L9IrGwJQzspPRBACvzGnvoS9xMdxMKfDEBgBMxGZ7Aix2uLaVJR43cPtQS3zzp0HBTjzTAI"

    # Refresh the access token
    access_token = refresh_access_token(REFRESH_TOKEN, CLIENT_ID, CLIENT_SECRET)

    # Check if the request contains event details in natural language or JSON
    try:
        body = json.loads(event.get('body', '{}'))
        if 'natural_language' in body:
            # Parse natural language input (e.g., "Schedule a meeting tomorrow at 3 PM CST for 2 hours")
            event_details = parse_natural_language(body['natural_language'])
        else:
            # Standard JSON payload
            event_details = body
    except Exception as e:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': f"Failed to parse input: {str(e)}"})
        }

    # Send the request to Google Calendar API
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    try:
        response = requests.post(GOOGLE_CALENDAR_API_URL, headers=headers, json=event_details)
        if response.status_code in [200, 201]:
            return {
                'statusCode': 200,
                'body': json.dumps({'message': 'Event created successfully', 'event': response.json()})
            }
        else:
            return {
                'statusCode': response.status_code,
                'body': json.dumps({'error': 'Failed to create event', 'details': response.text})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': f"An error occurred: {str(e)}"})
        }

def parse_natural_language(input_text):
    # Simple regex-based parsing for demo purposes
    # Example input: "Schedule a meeting tomorrow at 3 PM CST for 2 hours"
    match = re.search(r"(?P<summary>.+?) (on|tomorrow|at) (?P<datetime>.+?) for (?P<duration>\d+) hour", input_text)
    if not match:
        raise ValueError("Failed to parse natural language input")
    
    # Extract details
    summary = match.group("summary")
    date_time = match.group("datetime")
    duration_hours = int(match.group("duration"))

    # Calculate start and end times
    start_time = datetime.strptime(date_time, "%I %p CST")
    end_time = start_time + timedelta(hours=duration_hours)

    # Return structured JSON for Google Calendar API
    return {
        "summary": summary,
        "start": {
            "dateTime": start_time.isoformat(),
            "timeZone": "America/Chicago"
        },
        "end": {
            "dateTime": end_time.isoformat(),
            "timeZone": "America/Chicago"
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {
                    "method": "popup",
                    "minutes": 120
                }
            ]
        }
    }

```

---

### 2. **API Gateway Setup**

#### **Steps to Create Event**:
1. Construct the JSON event in the format of the example test below (you can use any AI chat to construct this for you)
2. Run a Curl command in the following form:
   ```Command Line
   curl -X POST https://2k0px8lwj3.execute-api.us-east-2.amazonaws.com/Create_Google_Calendar_Event \
   -H "Content-Type: application/json" \
   -d '{
     "summary": "Test Event",
     "start": {
       "dateTime": "2025-01-15T10:00:00-05:00",
       "timeZone": "America/New_York"
     },
     "end": {
       "dateTime": "2025-01-15T11:00:00-05:00",
       "timeZone": "America/New_York"
     },
     "reminders": {
       "useDefault": false,
       "overrides": [
         {
           "method": "popup",
           "minutes": 15
         }
       ]
     }
   }'
   ```
#### **API Endpoint**:
```
[https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/schedule](https://2k0px8lwj3.execute-api.us-east-2.amazonaws.com/Create_Google_Calendar_Event)
```

---

### 3. **Testing with JSON**

#### **Example JSON Test Event**:
```json
{
  "summary": "Test Event",
  "start": {
    "dateTime": "2025-01-15T10:00:00-05:00",
    "timeZone": "America/New_York"
  },
  "end": {
    "dateTime": "2025-01-15T11:00:00-05:00",
    "timeZone": "America/New_York"
  },
  "reminders": {
    "useDefault": false,
    "overrides": [
      {
        "method": "popup",
        "minutes": 15
      }
    ]
  }
}
```

