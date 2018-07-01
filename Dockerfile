FROM python:2.7-slim
ADD python app.py 
RUN pip-install
CMD [ "python", "./python app.py" ]
