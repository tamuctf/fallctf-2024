FROM ubuntu:20.04

ARG port \
    mailgun_api_key \
    mailgun_domain \
    secret_key


ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev curl wget texlive-latex-base texlive-latex-recommended texlive-latex-extra

WORKDIR /app

RUN pip3 install flask requests uuid pdflatex

COPY ./app /app

RUN chmod 555 /app
RUN chmod -R 555 /app/static /app/templates

USER 1000:1000

ENV PORT=$port \
    MAILGUN_API_KEY=$mailgun_api_key \
    MAILGUN_DOMAIN=$mailgun_domain \
    SECRET_KEY=$secret_key

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]