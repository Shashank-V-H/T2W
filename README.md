# Text-to-Web Generator  

**Live Demo:** [t2w.pythonanywhere.com](http://t2w.pythonanywhere.com/)  
**Model:** [Hugging Face - Llama3 Fine-Tuned](https://huggingface.co/Shashank-V-H/llama-3-8b-fine-tuned-web-app-generator)  

## Overview  
The **Text-to-Web Generator** is an AI-powered tool that converts natural language prompts into responsive web pages. It leverages a fine-tuned **Llama3** model optimized with **quantization and Unsloth**, deployed on **Hugging Face** with real-time inference APIs.  

## Features  
- **AI-driven Code Generation**: Converts text prompts into HTML, CSS, and JavaScript code.  
- **Optimized Performance**: Uses model quantization and Unsloth for faster inference.  
- **Seamless Deployment**: Hosted on PythonAnywhere with Django and Bootstrap for UI.  
- **Real-time API**: Fetches generated code dynamically from Hugging Face APIs.  

## Tech Stack  
- **AI/ML**: PyTorch, Transformers, Llama3, Hugging Face, Unsloth, Quantization  
- **Backend**: Django, API Development  
- **Frontend**: Bootstrap, JavaScript, HTML/CSS  
- **Deployment**: PythonAnywhere, Hugging Face  

## How It Works  
1. **Enter a prompt** describing the desired webpage (e.g., "A portfolio page with a contact form").  
2. The model processes the input and generates **HTML, CSS, and JavaScript**.  
3. The generated code is displayed and can be copied or downloaded.  

## Installation & Setup  
1. Clone the repository:  
   ```bash
   git clone https://github.com/Shashank-V-H/text-to-web-generator.git
   cd text-to-web-generator
   ```  
2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  
3. Run the Django server:  
   ```bash
   python manage.py runserver
   ```  
4. Open **http://127.0.0.1:8000/** in your browser.  
