from flask import Flask
import os

app = Flask(__name__)
# CI/CD 파이프라인이 정상 작동했는지 확인하기 위한 메시지
MESSAGE = os.environ.get('APP_MESSAGE', 'Hello from Jenkins CI/CD Pipeline!')

@app.route('/')
def hello():
    return f"<h1>{MESSAGE}</h1><h2>Version: 1.0</h2>"

if __name__ == '__main__':
    # Docker 내부에서 접근 가능한 호스트와 포트 설정
    app.run(debug=True, host='0.0.0.0', port=8000)
