FROM ubuntu:20.04

ARG port

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev curl wget

WORKDIR /app

RUN pip3 install flask

COPY ./app /app

# RUN mkdir -p /app/static/styles /app/templates

# COPY /app/app.py app.py
# COPY /app/static/robots.txt static/robots.txt
# COPY /app/static/styles/style-cookies.css /static/styles/style-cookies.css 
# COPY /app/static/styles/style.css /static/styles/style.css 

RUN chmod 555 /app
RUN chmod -R 555 /app/static /app/templates

USER 1000:1000

ENV PORT=$port

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]