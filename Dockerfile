FROM python:3.9.16-alpine3.17

WORKDIR /project
COPY . .
RUN  pip install -U pip && \
     python parse_lock_file.py > requirements.txt && pip install -r requirements.txt

EXPOSE 8000
ENTRYPOINT "./run.sh"