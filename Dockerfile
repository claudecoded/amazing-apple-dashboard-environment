# Use an official lightweight Python image
FROM python:3.10-slim

# Set system environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Install pipenv and system dependencies
RUN pip install --no-cache-dir pipenv

# Copy dependency files first to leverage Docker caching layers
COPY Pipfile Pipfile.lock ./

# Install project dependencies system-wide inside the container
RUN pipenv install --system --deploy

# Copy the rest of the application source code
COPY . /app

# Expose the default Dash web framework port
EXPOSE 8050

# Command to execute the dashboard application
CMD ["python", "app.py"]
