FROM alpine


RUN   apk add --update --no-cache \
      python3 \
      py3-pip \
      vim \
      && rm -rf /var/cache/apk/*



WORKDIR /app
COPY . /app

RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD [ "python3", "app.py" ]