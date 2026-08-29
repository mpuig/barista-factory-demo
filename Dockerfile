FROM node:22-alpine AS frontend
WORKDIR /src/web
COPY web /src/web
RUN node build.mjs

FROM python:3.12-slim
WORKDIR /app
COPY app /app/app
COPY --from=frontend /src/web/dist /app/web/dist
EXPOSE 8080
ENV BARISTA_DEMO_DB=/data/demo.sqlite3
VOLUME ["/data"]
CMD ["python", "-m", "app.server"]
