FROM python:3.9

WORKDIR /app

# COPY files
COPY app.py /app
COPy main.py /main.py
COPY requirements.txt /app
COPY model /app/model
COPY ms /app/ms
copy code /app/code

# Install dependencies
RUN pip3 install -r requirements.txt

# Run the application
EXPOSE 8000
# ENTRYPOINT [  "gunicorn", "-b", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "--timeout", "120"]
CMD [  "uvicorn", "main.py", "-b", "0.0.0.0:8000"]
# CMD ["app:app"]
