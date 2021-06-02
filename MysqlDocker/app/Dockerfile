FROM mysql

ENV MYSQL_DATABASE=mysqlsampledata \
    MYSQL_ROOT_PASSWORD=root_password


ADD bdd.sql /docker-entrypoint-initdb.d

EXPOSE 3306
