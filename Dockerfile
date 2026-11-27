FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends g++ python3-pytest && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY . .
RUN g++ -std=c++17 -O2 -Wall -Wextra -Werror src/fast_stats.cpp -o /usr/local/bin/fast_stats
ENV PYTHONPATH=/app
CMD ["pytest", "-v"]