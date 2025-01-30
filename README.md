# Text-to-Web Generator  

**Live Demo:** [t2w.pythonanywhere.com](http://t2w.pythonanywhere.com/)  

## Overview  
The **Text-to-Web Generator** is an AI-powered tool that converts natural language prompts into responsive web pages. It utilizes **Llama3 via Together.ai API** to generate **HTML, CSS, and JavaScript** based on user input.  

## Features  
- **AI-driven Code Generation**: Uses **Together.ai API** to convert text prompts into web code.  
- **Fast and Scalable**: Cloud-based inference ensures quick and efficient responses.  
- **Seamless Deployment**: Built with Django and Bootstrap for a user-friendly interface.  
- **Real-time API**: Fetches generated code dynamically from Together.ai.  

## Tech Stack  
- **AI/ML**: Together.ai API, Llama3  
- **Backend**: Django, API Integration  
- **Frontend**: Bootstrap, JavaScript, HTML/CSS  
- **Deployment**: PythonAnywhere  

## How It Works  
1. **Enter a prompt** describing the desired webpage (e.g., "A portfolio page with a contact form").  
2. The system sends the prompt to **Together.ai API** and retrieves the generated **HTML, CSS, and JavaScript**.  
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
3. Set up your **Together.ai API key**:  
   ```bash
   export TOGETHER_API_KEY="your-api-key-here"
   ```  
4. Run the Django server:  
   ```bash
   python manage.py runserver
   ```  
5. Open **http://127.0.0.1:8000/** in your browser.  

