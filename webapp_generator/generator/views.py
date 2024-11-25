import requests
import json
from django.http import JsonResponse
from django.shortcuts import render
import logging

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Together.AI API constants
TOGETHER_AI_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = "3460fb4d7e4663f65203cdad6290169cafb2bdb89584278a59b161eea88479d7"

def index(request):
    return render(request, 'index.html')

def generate_webpage(request):
    if request.method == 'POST':
        try:
            # Parse the incoming request payload
            data = json.loads(request.body.decode('utf-8'))
            prompt = data.get('prompt', '')

            # Prepare the payload for Together.AI API
            payload = {
                "model": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {TOGETHER_API_KEY}"
            }

            # Make the API request
            response = requests.post(TOGETHER_AI_API_URL, json=payload, headers=headers)
            
            # Log the response for debugging
            logging.debug(f"API Response: {response.text}")

            # Parse the API response
            if response.status_code == 200:
                response_data = response.json()
                if "choices" in response_data:
                    generated_code = response_data["choices"][0]["message"]["content"]
                else:
                    generated_code = "Error: No valid output from the API."
            else:
                generated_code = f"Error: {response.status_code} - {response.text}"

        except Exception as e:
            logging.error(f"Error during API call: {e}")
            generated_code = f"Error: {str(e)}"

        # Return the generated code as JSON
        return JsonResponse({'html_code': generated_code})
    else:
        return JsonResponse({'html_code': 'Invalid request method. Use POST.'})

