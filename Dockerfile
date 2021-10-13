FROM python:3
RUN  mkdir WORK_REPO
RUN  cd  WORK_REPO
WORKDIR  /WORK_REPO
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir requests
ADD sample.py .
CMD ["python", "-u", "sample.py"]