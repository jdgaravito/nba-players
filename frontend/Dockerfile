# pull official base image
FROM node:16-slim

# set working directory
RUN mkdir -p /home/node/app
WORKDIR /home/node/app

# copy package.json
COPY ./package*.json .

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc \
  && apt-get clean
#install svelte-kit dependencies
RUN npm install
# add app
COPY . .
