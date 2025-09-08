# Use the official PostgreSQL image from the Docker Hub as the base image.
# We're using the latest version of the "alpine" variant, which is smaller and more secure.
FROM postgres:16

# The following environment variables are used to configure the PostgreSQL instance.
# These will set up the initial database, user, and password for the server.
# It is highly recommended to override these with your own values in the 'docker run' command.
# For example:
# docker run -e POSTGRES_USER=myuser -e POSTGRES_PASSWORD=mypassword ...

# Sets the password for the default 'postgres' user.
# NOTE: Do not hardcode sensitive data in the Dockerfile. Pass POSTGRES_PASSWORD as an environment variable at runtime.
# Example: docker run -e POSTGRES_PASSWORD=yourpassword ...

# Sets the name of the initial database to be created.
# This database will be owned by the user defined by POSTGRES_USER.
ENV POSTGRES_DB=mydatabase

# Sets the name of the user to be created.
# This user will have superuser access to the 'mydatabase' database.
ENV POSTGRES_USER=myuser

# By default, PostgreSQL listens on port 5432.
# EXPOSE indicates that the container listens on the specified network port at runtime.
# This doesn't publish the port, but acts as a form of documentation and a hint to container orchestrators.
EXPOSE 5432



# The official PostgreSQL image automatically runs any SQL scripts
# found in this directory when the container is first created.
# This is a great way to automatically initialize your database schema and data.
# For example, you can add a 'schema.sql' or 'init-data.sql' file here.
COPY ./init.sql /docker-entrypoint-initdb.d/
