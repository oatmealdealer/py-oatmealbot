# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.9.1-slim-buster

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV PIPENV_VENV_IN_PROJECT=1

# Install pip requirements
# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt
RUN python -m pip install pipenv
COPY Pipfile .
COPY Pipfile.lock .

WORKDIR /app
COPY . /app

# Switching to a non-root user, please refer to https://aka.ms/vscode-docker-python-user-rights
RUN useradd appuser && chown -R appuser /app
USER appuser
RUN pipenv install --deploy --ignore-pipfile

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD ["pipenv", "run", "python", "-m", "bot"]
