# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variables
ENV NAME World
ENV FLASK_ENV production
ENV FLASK_APP run.py

# Run gunicorn when the container launches
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "run:app", "--log-level", "info", "--access-logfile", "-", "--error-logfile", "-"]
