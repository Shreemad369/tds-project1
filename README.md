# TDS Project 1: Automation Agent with LLM Integration

## Description
This project automates routine tasks using a Flask-based API that integrates with GPT-4o-Mini via AI Proxy.

## Endpoints
1. `/run?task=<task description>`: Executes a plain-English task.
2. `/read?path=<file path>`: Reads and returns the content of a file.

## How to Run Locally
1. Clone this repository:
git clone https://github.com/Shreemad369/tds-project1.git
cd tds-project1
2. Install dependencies: pip install -r requirements.txt
3. Run the application: python app.py
 
## How to Run with Docker
1. Build the Docker image: docker build -t shreemad369/tds-project1
2. Run the container: docker run -e AIPROXY_TOKEN=$AIPROXY_TOKEN -p 8000:8000 shreemad369/tds-project1

Visit `http://localhost:8000`.

## License
This project is licensed under the MIT License.




