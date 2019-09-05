FROM python:3.7

ADD ./requirements.txt /vulnPreview/requirements.txt
ADD ./test-github.py /vulnPreview/test-github.py

WORKDIR /vulnPreview

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]