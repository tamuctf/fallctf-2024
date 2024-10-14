FROM node:22-alpine as builder

WORKDIR /app/editor
COPY editor/ .
RUN npm install
RUN npm run build

WORKDIR /app/grader
COPY grader/ .
RUN npm install

FROM nginx:1.27-alpine

WORKDIR /app
COPY --from=builder /app/editor/build /var/www/html
COPY --from=builder /app/grader grader
COPY nginx.conf /etc/nginx/nginx.conf

RUN apk add --no-cache nodejs python3 sudo && \
    adduser -S -s /sbin/nologin grader

EXPOSE 8000

COPY start.sh .
RUN chmod +x /app/start.sh

CMD ["/app/start.sh"]
