FROM python:3.9-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

ENV DATA_FILE_PATH="data/visiters.txt"
ENV YOUR_NAME="Vladimir"

ENV FLASK_APP = "app.py"
ENV FLASK_ENV = development
ENV FLASK_DEBUG = 0

EXPOSE 5000

# VOLUME [ "/data" ]

ENTRYPOINT [ "python", "app.py" ]
