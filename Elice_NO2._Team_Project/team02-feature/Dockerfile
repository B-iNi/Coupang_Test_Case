FROM jenkins/jenkins:lts

USER root

# 기본 패키지 설치
RUN apt-get update && apt-get install -y \
    tini \
    sudo \
    git \
    python3 python3-pip python3-venv \
    curl unzip git wget gnupg2 \
    software-properties-common apt-transport-https \
    libglib2.0-0 libnss3 libgconf-2-4 libfontconfig1 libxss1 \
    libappindicator1 libasound2 libatk-bridge2.0-0 libgtk-3-0 \
    xvfb chromium chromium-driver \
    && apt-get clean && rm -rf /var/lib/apt/lists/*


# Chrome & ChromeDriver 자동 설치
RUN CHROME_VERSION=$(google-chrome --version | awk '{print $3}' | cut -d. -f1-3) && \
    DRIVER_VERSION="136.0.7103.113" && \
    wget -q "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/${DRIVER_VERSION}/linux64/chromedriver-linux64.zip" -O /tmp/chromedriver.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    mv /usr/local/bin/chromedriver-linux64/chromedriver /usr/local/bin/chromedriver && \
    chmod +x /usr/local/bin/chromedriver && \
    rm -rf /tmp/chromedriver.zip

RUN python3 -m pip install --upgrade pip --break-system-packages
RUN pip install selenium pytest selenium_stealth --break-system-packages


# Node.js 18 설치
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && \
    apt-get install -y nodejs

# node / npm 버전 확인
RUN node -v && npm -v

# jenkins 사용자를 sudoers에 추가
RUN echo "jenkins ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers

USER jenkins

# 필요한 Jenkins 플러그인 설치 (예시: nodejs 플러그인)
RUN jenkins-plugin-cli --plugins "nodejs:1.5.0"

ENTRYPOINT ["tini", "--", "/usr/local/bin/jenkins.sh"]