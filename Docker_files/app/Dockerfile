# Multi-stage
# First Stage: Clone source code, switch branch and build the artifact
FROM maven:3.9.9-eclipse-temurin-21-jammy AS BUILD_IMAGE
ARG GIT_REPO
RUN git clone ${GIT_REPO}
RUN cd vprofile-project && git checkout containers && mvn install
# This build stage will be terminated after the container image is successfully built.

# Next Stage: Remove the exist file on tomcat and copy the artifact from BUILD_IMAGE to tomcat
FROM tomcat:10-jdk21
LABEL "Project"="Web_Containerization"
LABEL "Name"="Man"
RUN rm -rf /usr/local/tomcat/webapps/*
COPY --from=BUILD_IMAGE vprofile-project/target/vprofile-v2.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080
# Default script to run tomcat
CMD ["catalina.sh","run"]