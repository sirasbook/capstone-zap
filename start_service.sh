docker build -t sirasj/zap-server-mr-robot .

docker run -v $(pwd):/zap/wrk -v $(pwd)/app/reports:/zap/wrk/app/reports -p 8000:8000 --rm sirasj/zap-server-mr-robot