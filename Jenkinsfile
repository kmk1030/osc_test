pipeline {
    agent any
    
    // 환경 변수 설정 (이미지 이름과 태그)
    environment {
        IMAGE_NAME = 'osc-web-app'
//        DOCKER_CREDENTIAL_ID = 'docker-hub-credentials' // Docker Hub 사용 시 필요 (선택 사항)
        APP_PORT = 8000 // 앱 내부 포트
        HOST_PORT = 80 // EC2 외부 노출 포트
    }

    stages {
        // 1. 소스 코드 가져오기
        stage('Checkout') {
            steps {
                echo 'Checking out code...'
                // Jenkins Job 설정에서 Git URL을 지정했으므로, 이 단계에서 코드를 가져옵니다.

            }
        }
        
        // 2. 도커 이미지 빌드 (CI)
        stage('Build Docker Image') {
            steps {
                script {
                    def tag = "latest-${env.BUILD_ID}" // 빌드 번호를 태그로 사용
                    echo "Building Docker image: ${IMAGE_NAME}:${tag}"
                    
                    // Dockerfile을 사용하여 이미지 빌드
                    sh "docker build -t ${IMAGE_NAME}:${tag} ."
                }
            }
        }
        
        // 3. 배포 (CD)
        stage('Deploy Application') {
            steps {
                script {
                    def tag = "latest-${env.BUILD_ID}"
                    echo "Deploying application to EC2 host..."

                    // 3-1. 기존 컨테이너 중지 및 제거
                    sh "docker stop ${IMAGE_NAME} || true"
                    sh "docker rm ${IMAGE_NAME} || true"

                    // 3-2. 새로운 이미지로 컨테이너 실행
                    // EC2 외부 80 포트를 앱 내부 8000 포트와 연결
                    sh """
                        docker run -d \
                          -p ${HOST_PORT}:${APP_PORT} \
                          --name ${IMAGE_NAME} \
                          -e APP_MESSAGE='Deployment via Jenkins Build #${env.BUILD_ID}' \
                          ${IMAGE_NAME}:${tag}
                    """
                    echo "Application deployed successfully. Access via http://[Public IP]:80"
                }
            }
        }
    }
}
