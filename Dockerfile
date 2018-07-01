FROM python:2.7-slim
ADD app.py 
RUN pip-install
CMD [ "python", "./app.py" ]
