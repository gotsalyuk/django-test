FROM python:3.9
ENV CORE_HOST=0.0.0.0
ENV CORE_PORT=8000


WORKDIR /app
COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD python manage.py runserver $CORE_HOST:$CORE_PORT
