FROM python:3.12-slim
WORKDIR /app
COPY app /app/app
EXPOSE 8080
ENV BARISTA_DEMO_DB=/data/demo.sqlite3
VOLUME ["/data"]
CMD ["python", "-m", "app.server"]
