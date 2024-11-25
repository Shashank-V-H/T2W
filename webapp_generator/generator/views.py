from transformers import pipeline
from django.http import JsonResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def generate_webpage(request):
    if request.method == 'POST':
        prompt = request.POST.get('prompt')
        generator = pipeline("text-generation", model="gpt2")
        response = generator(prompt, max_length=500)[0]['generated_text']
        return JsonResponse({'html_code': response})
