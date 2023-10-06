# # Most of the time, Alpine is a great base image to start with.
# # If we're building a container for Python, we use something different.
# # Learn why here: https://pythonspeed.com/articles/base-image-python-docker-images/
# # TLDR: Alpine is very slow when it comes to running Python!

# # STEP 1: Install base image. Optimized for Python.
# FROM python:3.7-slim-buster

# # STEP 2: Copy the source code in the current directory to the container
# # Store it in a folder named /app.
# ADD Code/ /app

# # STEP 3: Set working directory to /app so we can execute commands in it
# WORKDIR /app

# # STEP 4: Install required dependencies
# RUN pip install -r requirements.txt

# # STEP 5: Declare environment variables
# ENV FLASK_APP=app.py
# ENV FLASK_ENV=development

# # STEP 6: Expose the port that Flask is running on
# EXPOSE 5000

# # STEP 7: Run Flask!
# CMD ["flask", "run", "--host=0.0.0.0"]


# STEP 1: Install base image. Optimized for Python.
FROM python:3.9-slim-buster

# STEP 2: Set the working directory in the container to /app. This will create the directory as well.
WORKDIR /app

# STEP 3: Copy the source code and other necessary files in the current directory to the container.
# First, copy root application files
COPY app.py .
COPY requirements.txt .


# Then, copy the source directory
COPY source/ source/

# STEP 3.5: Install GDAL native library and development headers
RUN apt-get update && apt-get install -y \
    libgdal-dev \
    gdal-bin \
&& apt-get clean \
&& rm -rf /var/lib/apt/lists/*

# STEP 4: Install required dependencies
RUN pip install -r requirements.txt

# STEP 5: Declare environment variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# STEP 6: Expose the port that Flask is running on
EXPOSE 5000

# STEP 7: Run Flask!
CMD ["flask", "run", "--host=0.0.0.0"]
