FROM python:3.6.3
LABEL maintainer="peacengell@gmail.com"
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt

RUN curl -sL https://deb.nodesource.com/setup_10.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g vue-cli@2.9.3

CMD ["/bin/bash"]
ENTRYPOINT [ "python", "app.py" ]
EXPOSE 5000