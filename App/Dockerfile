#Build and run WebApp

FROM python:3.12-slim AS builder

WORKDIR /build
COPY  App/requirements.txt ./
RUN pip install --prefix=/build -r requirements.txt


FROM python:3.12-slim
RUN adduser --system --uid 1001 appuser

WORKDIR /app
COPY --from=builder /build /usr/local

COPY --chown=appuser:appuser  App/Website ./Website
COPY --chown=appuser:appuser  App/src/*.py .

USER appuser

EXPOSE 8000

CMD ["python", "Server.py"] 