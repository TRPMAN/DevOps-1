FROM mysql:8.0.33
LABEL "Project"="Web_Containerization"
LABEL "Name"="Man"

# !!! Mistake: this is how to variable
ENV MYSQL_ROOT_PASSWORD=${MYSQL_ROOT_PASSWORD}
# !!! Mistake: spelling mistake
ENV MYSQL_DATABASE=${MYSQL_DATABASE}

# This is from mysql image documentation told to add any .sql file in this directory
ADD db_backup.sql docker-entrypoint-initdb.d/db_backup.sql