import requests
import json
import time
from django.http import JsonResponse
from django.shortcuts import render
import logging
import zipfile
import io
from django.http import HttpResponse

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Together.AI API constants
TOGETHER_AI_API_URL = "https://api.together.xyz/v1/chat/completions"
TOGETHER_API_KEY = "3460fb4d7e4663f65203cdad6290169cafb2bdb89584278a59b161eea88479d7"

# Standard test prompts for benchmarking
test_prompts = [
    "Create a simple webpage with a contact form.",
    "Design a responsive navbar with dropdowns.",
    "Create a webpage with a product gallery using flexbox.",
    "Create a webpage with an interactive login form.",
    "Generate a page with a responsive footer."
]

def index(request):
    return render(request, 'index.html')

def generate_webpage(request):
    if request.method == 'POST':
        try:
            # Parse the incoming request payload
            data = json.loads(request.body.decode('utf-8'))
            prompt = data.get('prompt', '')

            # Advanced prompt engineering
            refined_prompt = (
                f"{prompt}\n\n"
                "Respond with only the required code in the following format:\n"
                "1. Start with HTML code block enclosed within `<html>` tags.\n"
                "2. Follow with CSS code enclosed within `<style>` tags.\n"
                "3. Finally, provide JavaScript code enclosed within `<script>` tags.\n"
                "Do not include any explanatory text, comments, or descriptions."
            )

            # Prepare the payload for Together.AI API
            payload = {
                "model": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "messages": [
                    {"role": "user", "content": refined_prompt}
                ]
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {TOGETHER_API_KEY}"
            }

            # Make the API request
            start_time = time.time()
            response = requests.post(TOGETHER_AI_API_URL, json=payload, headers=headers)
            end_time = time.time()

            # Log the response for debugging
            latency = end_time - start_time
            logging.debug(f"API Response: {response.text}")
            logging.debug(f"Latency: {latency} seconds")

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
        return JsonResponse({'html_code': generated_code, 'latency': latency})
    else:
        return JsonResponse({'html_code': 'Invalid request method. Use POST.'})

def benchmark_api(request):
    """
    Function to benchmark the performance of the API using predefined test prompts.
    """
    results = []
    for prompt in test_prompts:
        try:
            # Prepare the prompt
            refined_prompt = (
                f"{prompt}\n\n"
                "Respond with only the required code in the following format:\n"
                "1. Start with HTML code block enclosed within `<html>` tags.\n"
                "2. Follow with CSS code enclosed within `<style>` tags.\n"
                "3. Finally, provide JavaScript code enclosed within `<script>` tags.\n"
                "Do not include any explanatory text, comments, or descriptions."
            )

            # Prepare the payload for Together.AI API
            payload = {
                "model": "Qwen/Qwen2.5-72B-Instruct-Turbo",
                "messages": [
                    {"role": "user", "content": refined_prompt}
                ]
            }
            headers = {
                "accept": "application/json",
                "content-type": "application/json",
                "authorization": f"Bearer {TOGETHER_API_KEY}"
            }

            # Make the API request and measure latency
            start_time = time.time()
            response = requests.post(TOGETHER_AI_API_URL, json=payload, headers=headers)
            end_time = time.time()
            latency = end_time - start_time

            # Log the response and latency
            if response.status_code == 200:
                response_data = response.json()
                if "choices" in response_data:
                    generated_code = response_data["choices"][0]["message"]["content"]
                else:
                    generated_code = "Error: No valid output from the API."
            else:
                generated_code = f"Error: {response.status_code} - {response.text}"

            # Append the result for this prompt
            results.append({
                "prompt": prompt,
                "latency": latency,
                "generated_code": generated_code
            })

        except Exception as e:
            logging.error(f"Error during API benchmark for prompt {prompt}: {e}")
            results.append({"prompt": prompt, "latency": None, "generated_code": f"Error: {str(e)}"})

    # Return benchmark results as JSON
    return JsonResponse({'benchmark_results': results})


def download_zip(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            html_code = data.get('html_code', '')

            # Split the code into HTML, CSS, and JS
            html_part, css_part, js_part = parse_generated_code(html_code)

            # Create a ZIP file in memory
            zip_buffer = io.BytesIO()
            with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
                zip_file.writestr('index.html', html_part)
                zip_file.writestr('styles.css', css_part)
                zip_file.writestr('script.js', js_part)

            zip_buffer.seek(0)  # Move to the start of the file

            # Set proper HTTP response for file download
            response = HttpResponse(zip_buffer.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename=generated_webpage.zip'
            return response
        except Exception as e:
            logging.error(f"Error during ZIP generation: {e}")
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method. Use POST.'}, status=400)

def parse_generated_code(code):
    # Extract the HTML, CSS, and JS parts from the generated code
    html_part = code.split('<style>')[0].strip()
    css_part = code.split('<style>')[1].split('</style>')[0].strip()
    js_part = code.split('<script>')[1].split('</script>')[0].strip()
    return html_part, css_part, js_part
