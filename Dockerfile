FROM python:3.11 

WORKDIR /code

#COPY . /code/
#COPY ./requirements.txt /code/requirements.txt
COPY src/fishmlserv/main.py /code/

RUN ls
RUN pip install --no-cache-dir --upgrade git+https://github.com/sooj1n/fishmlserv.git@0.7/MANIFEST

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8765"]
