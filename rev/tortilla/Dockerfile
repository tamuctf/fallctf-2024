FROM tobix/pywine:3.11@sha256:b7f4981c1895e0f14f0a549e52f41d030a536902f763069127463fc94656b60d 

WORKDIR /app

COPY src/ .
COPY requirements.txt .

RUN wine pip install -r requirements.txt

RUN wine pyinstaller --add-data "data\*;data\\" --noconsole -F game.py
