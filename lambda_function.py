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
