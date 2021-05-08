FROM python:3.7.10-buster

RUN mkdir /app
WORKDIR /app
ADD requirements.txt /app/
RUN pip3 install -r requirements.txt
ADD . /app/ 
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "application.py" ]