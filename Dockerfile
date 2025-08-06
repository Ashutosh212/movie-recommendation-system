FROM python:3.12-slim

LABEL version="1.0" maintainer="ashutoshbharti718@gmail.com"

ENV OPENAI_API_KEY=""

WORKDIR /recommender_system_project

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8501

CMD ["./start.sh"]
