FROM python:slim-buster

ARG port

RUN apt-get update -y; apt-get install socat -y

COPY flag.txt /jail/flag.txt
COPY jail.py /jail/jail.py

RUN chmod +x /jail/jail.py

WORKDIR /jail

RUN echo "exec socat -s TCP-LISTEN:$port,reuseaddr,fork EXEC:\"python3 /jail/jail.py\",stderr" > /jail/docker_entrypoint.sh

ENTRYPOINT ["sh", "/jail/docker_entrypoint.sh"]
