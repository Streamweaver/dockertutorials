FROM ubuntu:14.04
MAINTAINER Scott Turnbull "streamweaver@gmail.com"

RUN apt-get update && apt-get install -y nginx

VOLUME /usr/share/nginx/html
EXPOSE 80

COPY . /usr/share/nginx/html

WORKDIR /usr/share/nginx/html
ENTRYPOINT ["/usr/sbin/nginx", "-g", "daemon off;"]