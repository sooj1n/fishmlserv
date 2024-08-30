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
