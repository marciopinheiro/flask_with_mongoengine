FROM python:3.9.6

# Installing necessary components
RUN apt update

# Adjust Time Zone
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Add files
COPY ./ /var/www/app

# Go to working directory
WORKDIR /var/www/app

# Install requirements
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt