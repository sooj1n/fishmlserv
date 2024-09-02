FROM python:3.11 

WORKDIR /code

#COPY . /code/
#COPY ./requirements.txt /code/requirements.txt
COPY src/fishmlserv/main.py /code/

#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install git+https://github.com/sooj1n/fishmlserv.git@0.7.0/MANIFEST
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
