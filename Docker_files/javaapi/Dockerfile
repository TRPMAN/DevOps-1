FROM openjdk:8 AS BUILD_IMAGE
ARG GIT_REPO
WORKDIR /usr/src/app/
RUN apt update && apt install maven -y
RUN git clone ${GIT_REPO}
WORKDIR /usr/src/app/emartapp/javaapi/
RUN mvn install -DskipTests

FROM openjdk:8
WORKDIR /usr/src/app/
COPY --from=BUILD_IMAGE /usr/src/app/emartapp/javaapi/target/book-work-0.0.1-SNAPSHOT.jar ./book-work-0.0.1.jar
EXPOSE 9000
ENTRYPOINT ["java","-jar","book-work-0.0.1.jar"]