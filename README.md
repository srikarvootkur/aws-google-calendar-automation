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
The lambda_function.py Python script processes the incoming request, interacts with the Google Calendar API, and handles authentication and event creation.

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

