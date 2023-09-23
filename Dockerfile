# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose the port that your application will run on
# Replace 8000 with the actual port your app uses if needed
EXPOSE 8000

# Define the command to run your application
CMD ["python", "main.py"]