# aws-google-calendar-automation
# Automating Google Calendar Event Creation Using AWS Lambda

## Overview
This project demonstrates the use of AWS Lambda, API Gateway, and Python to automate the creation of Google Calendar events. The workflow is designed to accept natural language or structured JSON input via an HTTP API, parse the input into the appropriate format, and interact with the Google Calendar API to schedule events.

This guide includes a workflow diagram, detailed instructions for implementation, and tips for presenting this project on GitHub to showcase your technical skills to potential employers.

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
import requests

def lambda_handler(event, context):
    try:
        # Parse input
        body = json.loads(event['body'])
        
        # Google Calendar API endpoint
        calendar_api_url = "https://www.googleapis.com/calendar/v3/calendars/primary/events"

        # Headers (replace with your actual access token)
        headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Content-Type": "application/json"
        }

        # Send event data to Google Calendar API
        response = requests.post(calendar_api_url, headers=headers, json=body)

        # Return response
        if response.status_code == 200 or response.status_code == 201:
            return {
                "statusCode": 200,
                "body": json.dumps({"message": "Event created successfully", "response": response.json()})
            }
        else:
            return {
                "statusCode": response.status_code,
                "body": json.dumps({"error": response.text})
            }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
```

---

### 2. **API Gateway Setup**

#### **Steps to Create API Gateway**:
1. Open the AWS Management Console and navigate to **API Gateway**.
2. Create a new **HTTP API**.
3. Configure a **POST method** to trigger your Lambda function.
4. Deploy the API to a stage (e.g., `prod`).
5. Copy the API Gateway endpoint for testing and integration.

#### **Sample API Endpoint**:
```
https://your-api-id.execute-api.us-east-1.amazonaws.com/prod/schedule
```

---

### 3. **Testing with JSON**

#### **Example JSON Test Event**:
```json
{
  "summary": "Test Event",
  "start": {
    "dateTime": "2025-01-17T10:00:00-05:00",
    "timeZone": "America/New_York"
  },
  "end": {
    "dateTime": "2025-01-17T11:00:00-05:00",
    "timeZone": "America/New_York"
  },
  "reminders": {
    "useDefault": false,
    "overrides": [
      {
        "method": "popup",
        "minutes": 60
      }
    ]
  }
}
```

#### **Testing the Lambda Function**:
1. Go to the AWS Lambda Console.
2. Select your Lambda function.
3. Create a test event using the above JSON.
4. Execute the test and verify the response.

---

### 4. **GitHub Repository Setup**

#### **Repository Structure**:
```
project-root/
├── lambda_function.py       # Main Lambda function code
├── test_event.json          # Sample test event for local testing
├── requirements.txt         # Python dependencies (e.g., `requests`)
├── README.md                # Project documentation
└── deployment-package.zip   # Packaged Lambda deployment (optional)
```

#### **Steps to Create the GitHub Repository**:
1. **Initialize the Repository**:
   - Create a new repository on GitHub.
   - Clone it to your local machine.

2. **Add Files**:
   - Include the `lambda_function.py`, `requirements.txt`, and `test_event.json`.

3. **Write a Comprehensive README**:
   - Include:
     - Project overview.
     - Setup instructions.
     - Workflow diagram.
     - Example use cases.
     - Deployment instructions.

4. **Commit and Push**:
   ```bash
   git add .
   git commit -m "Initial commit: Google Calendar Automation"
   git push origin main
   ```

5. **Optional Enhancements**:
   - Add a `LICENSE` file.
   - Include deployment scripts or CI/CD pipelines for automated updates.

---

## Tips for Highlighting This Project
1. **README.md**:
   - Use visuals, like the workflow diagram and screenshots of API Gateway.
2. **Use Comments**:
   - Ensure your Python code has clear and concise comments.
3. **Include Real-World Use Cases**:
   - Show how this project could be integrated into a larger system (e.g., scheduling workflows).
4. **Demonstrate Testing**:
   - Include logs or screenshots of successful tests.

---

This project not only demonstrates your proficiency with AWS and Python but also highlights your ability to integrate cloud services with external APIs, a highly valuable skill in the tech industry.


