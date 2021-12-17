FROM python:3.8.5

# make a directory for the repo
RUN mkdir /repo

# go to the directory where we are going to upload the repo
WORKDIR /repo

COPY a.0_RHOBTB2_direct_output.json .
COPY c3_output.json .
COPY main.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
