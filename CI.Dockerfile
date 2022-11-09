FROM python:3-slim
WORKDIR /usr/src/app
COPY http.rqs.txt ./
RUN python -m pip install --no-cache-dir -r  http.rqs.txt
COPY ./app.py ./
CMD [ "python", "./app.py" ]