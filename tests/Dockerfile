FROM ubuntu:22.04

# Install common tools that might fail
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    docker.io \
    nodejs \
    npm \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Create a broken environment for testing
RUN useradd -m testuser

# Install terminai
COPY . /app
WORKDIR /app
RUN pip3 install -e .

# Create test scenarios
RUN mkdir -p /test-scenarios

# Test 1: Missing file
RUN echo "cat /nonexistent-file.txt" > /test-scenarios/test1.sh

# Test 2: Permission denied
RUN touch /root/secret.txt && chmod 000 /root/secret.txt
RUN echo "cat /root/secret.txt" > /test-scenarios/test2.sh

# Test 3: Port already in use
RUN echo "python3 -m http.server 8080 & sleep 1 && python3 -m http.server 8080" > /test-scenarios/test3.sh

# Test 4: Missing dependency
RUN echo "pip3 install nonexistent-package-xyz" > /test-scenarios/test4.sh

# Test 5: Docker not running
RUN echo "docker ps" > /test-scenarios/test5.sh

RUN chmod +x /test-scenarios/*.sh

CMD ["/bin/bash"]