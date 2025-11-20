from flask import Flask, render_template # render_template 모듈 추가
import os

app = Flask(__name__)
# CI/CD 파이프라인이 정상 작동했는지 확인하기 위한 메시지
MESSAGE = os.environ.get('APP_MESSAGE', 'Hello from Jenkins CI/CD Pipeline!')

@app.route('/')
def hello():
    # render_template을 사용하여 templates/index.html 파일을 반환
    # os.environ.get('BUILD_ID')로 컨테이너 환경 변수를 읽어옵니다.
    build_id = os.environ.get('BUILD_ID', 'N/A')
    # Flask Template Engine (Jinja2)를 통해 변수(message)를 전달
    build_message = f"Deployment via Jenkins Build #{os.environ.get('BUILD_ID', 'N/A')} | Version: 1.0"
    return render_template('index.html', message=build_message)

if __name__ == '__main__':
    # Docker 내부에서 접근 가능한 호스트와 포트 설정
    app.run(debug=True, host='0.0.0.0', port=8000)
