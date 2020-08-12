FROM python:3.6

WORKDIR /app

ADD . /app

RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

EXPOSE 9876

CMD ["python","app.py"]