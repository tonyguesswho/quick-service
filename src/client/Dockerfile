FROM node:16-alpine

# set working directory
WORKDIR /usr/src/app

# add `/usr/src/app/node_modules/.bin` to $PATH
ENV PATH /usr/src/app/node_modules/.bin:$PATH

# install and cache app dependencies
COPY ./package.json .
COPY ./yarn.lock .
COPY ./src .
COPY ./public .
RUN yarn install

CMD ["yarn", "start"]