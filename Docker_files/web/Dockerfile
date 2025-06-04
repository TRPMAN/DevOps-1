FROM nginx
LABEL "Project"="Web_Containerization"
LABEL "Name"="Man"

# Remove the dufault conf and replace it with our conf
RUN rm -rf /etc/nginx/conf.d/default.conf
COPY nginvproapp.conf /etc/nginx/conf.d/vproapp.conf