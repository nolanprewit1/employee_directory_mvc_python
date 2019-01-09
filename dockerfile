FROM alpine:latest
RUN apk add python3
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN pip3 install --upgrade pip
ENTRYPOINT ["python3"]
CMD ["app.py"]