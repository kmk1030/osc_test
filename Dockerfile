# Dockerfile 생성
# Python 3.9 Slim 기반 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 파일 복사
COPY app.py .

# 앱이 사용할 포트 명시 (Jenkinsfile에서 이 포트를 외부로 노출할 것입니다.)
EXPOSE 8000

# 앱 실행 명령어
CMD ["python", "app.py"]
