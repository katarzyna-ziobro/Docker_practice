FROM python:3.12-slim AS builder

WORKDIR /build
COPY  App/requirements.txt ./
RUN pip install --prefix=/build -r requirements.txt

FROM python:3.12-slim
WORKDIR /app
COPY --from=builder /build /usr/local

COPY App/Website ./Website
COPY App/Server.py ./

EXPOSE 8000

CMD ["python", "Server.py"] 