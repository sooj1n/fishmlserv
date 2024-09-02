# fishmlserv

### Deploy

![image](https://github.com/user-attachments/assets/6b7e8b51-fdcd-4027-8aaa-bfc0d8be369d)

### RUN
- dev
- http://localhost:8000/docs

```bash
$ uvicorn --help
$ uvicorn src.fishmlserv.main:app --reload
```

- prd
```bash
$ uvicorn src.fishmlserv.main:app --host 0.0.0.0 --port 8949
```
- Docker
```bash
$ sudo docker build -t fishmlserv:0.4.0 .
$ sudo docker run -d --name fmlserv-040 -p 8877:8765 fishmlserv:0.4.0
```

- Fly.io
```bash
$ fly launch --no-deploy
$ flyctl launch --name mariofish
$ flyctl scale memory 256
$ flyctl deploy
```

- Ref
```bash
https://curlconverter.com/python
```
