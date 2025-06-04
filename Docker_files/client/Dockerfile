FROM node:14 AS web-build
ARG GIT_REPO
WORKDIR /usr/src/app
RUN git clone ${GIT_REPO}
RUN cd emartapp/client/ && npm install && npm run build --prod

FROM nginx:latest
COPY --from=web-build /usr/src/app/emartapp/client/dist/client/ /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 4200
