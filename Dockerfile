FROM php:apache
WORKDIR /var/www/html

COPY . /var/www/html

expose 80
