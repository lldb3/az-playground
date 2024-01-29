import azure.functions as func
import json
import requests

workspace_id = 'YOUR_WORKSPACE_ID'
workspace_key = 'YOUR_WORKSPACE_KEY'
log_type = 'YOUR_LOG_TYPE'

def send_to_log_analytics(data):
    headers = {
        'Content-Type': 'application/json',
        'Log-Type': log_type,
        'Authorization': f'SharedKey {workspace_id}:{workspace_key}'
    }

    url = f'https://{workspace_id}.ods.opinsights.azure.com/api/logs?api-version=2016-04-01'

    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to send data to Log Analytics. Status code: {response.status_code}, Response: {response.text}")

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            "Invalid JSON payload",
            status_code=400
        )

    # Process the JSON payload here if needed

    # Send data to Log Analytics
    send_to_log_analytics(req_body)

    return func.HttpResponse("OK")
