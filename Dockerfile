FROM python:3.10-slim


# Recive build arguments
ARG PIPENV_EXTRA_ARG

# Change working directory 
WORKDIR /app/

# Copy project files
COPY ./ ./

# install dependencies
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile $PIPENV_EXTRA_ARG

# Dima suggest use this method:
# CMD ["python", "manage.py", "runserver" "0.0.0.0:80"]
CMD sleep 3 \
    && python src/manage.py migrate \
    && python src/manage.py runserver 0.0.0.0:80
# but we also can use simply this:
# CMD python manage.py runserver 0.0.0.0:80