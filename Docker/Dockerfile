FROM python:3.12-slim AS builder

WORKDIR /build
COPY  WebServer/requirements.txt ./
RUN pip install --prefix=/build -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /build /usr/local

COPY WebServer/Website ./Website
COPY WebServer/Server.py ./

EXPOSE 8000

CMD ["python", "Server.py"] 