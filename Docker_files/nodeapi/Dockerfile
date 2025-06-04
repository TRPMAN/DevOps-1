FROM node:14 AS nodeapi-build
ARG GIT_REPO
WORKDIR /usr/src/app
RUN git clone ${GIT_REPO}
RUN ls
RUN cd emartapp/nodeapi/ && npm install

FROM node:14
WORKDIR /usr/src/app/
COPY --from=nodeapi-build /usr/src/app/emartapp/nodeapi/ ./
RUN ls
EXPOSE 5000
CMD ["/bin/sh", "-c", "cd /usr/src/app/ && npm start"]