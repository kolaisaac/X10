from flask import Flask, request
from datetime import datetime, timedelta
import requests
import json

app = Flask(__name__)

@app.route('/api', methods=['GET'])

def get_info():
    #Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    #Get current day of the week
    current_day = datetime.now().strftime('%A')

    #Get current time
    current_time = datetime.utcnow()
    current_time_str = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')

    #My GitHub repo info
    github_repo_url = 'https://github.com/kolaisaac/SageMakerRL-SML-Summit-2019'
    github_file_url = 'https://github.com/kolaisaac/SageMakerRL-SML-Summit-2019/blob/master/Sagemaker_RL_Lab_Summit_2019_One_Click_old.ipynb'

    #Status code
    status_code = 200

    #JSON response

    response_data = {
        'slack_name': 'blestisaac',
        'current_day': current_day,
        'utc_time': current_time_str,
        'track': 'backend',
        'github_repo_url': github_repo_url,
        'github_file_url': github_file_url,
        'status_code': status_code
    }

    #Using json.dumps to format the JSON with indentation

    response_json = json.dumps(response_data, indent=2)

    #Set content type
    return response_json, 200, {'Content-Type': 'application/json'}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)