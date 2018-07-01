FROM python:2.7-slim
ADD app.py 
CMD [ "python", "./app.py" ]
