FROM php:apache
WORKDIR .

COPY . .

expose 80
