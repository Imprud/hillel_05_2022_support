FROM python:3.10-slim

# Change working directory 
WORKDIR /app/

# Copy project files
COPY . .

# install dependencies
RUN pip install pipenv \
    && pipenv install --system --deploy --ignore-pipfile --dev

# Dima suggest use this method:
# CMD ["python", "manage.py", "runserver" "0.0.0.0:80"]
CMD sleep 3 \
    && python manage.py migrate \
    && python manage.py runserver 0.0.0.0:80
# but we also can use simply this:
# CMD python manage.py runserver 0.0.0.0:80