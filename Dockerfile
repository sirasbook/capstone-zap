FROM owasp/zap2docker-stable

USER root

WORKDIR /app
COPY . .

RUN apt update -y
RUN apt upgrade -y

SHELL ["/bin/bash", "-c"]
RUN mkdir /zap/wrk && python3 -m pip install -r requirement.txt
RUN chmod +x ./app/zap/start-baseline.sh
RUN chmod +x ./app/zap/start-fullscan.sh

CMD ["python", "main.py"]