# TerminAI Test Scenarios

## Setup
```bash
cd tests
docker-compose up -d
docker-compose exec terminai-test bash
```

## Test Cases

### 1. Missing File
```bash
fixit "cat /nonexistent-file.txt"
```
Expected fix: Suggest creating the file or checking the path

### 2. Permission Denied
```bash
fixit "cat /root/secret.txt"
```
Expected fix: `sudo cat /root/secret.txt` or change permissions

### 3. Port Already in Use
```bash
fixit "bash /test-scenarios/test3.sh"
```
Expected fix: Kill process on port 8080 or use different port

### 4. Missing Python Package
```bash
fixit "python3 -c 'import requests'"
```
Expected fix: `pip3 install requests`

### 5. Docker Not Running
```bash
fixit "docker ps"
```
Expected fix: `sudo systemctl start docker` or similar

### 6. Wrong Command Syntax
```bash
fixit "grep --invalid-flag test.txt"
```
Expected fix: Correct grep syntax

### 7. Missing sudo
```bash
fixit "apt-get install vim"
```
Expected fix: `sudo apt-get install vim`

## Advanced Tests

### 8. Environment Variable Missing
```bash
fixit "echo $UNDEFINED_VAR | grep something"
```

### 9. Network Issue
```bash
fixit "curl https://invalid-domain-xyz.com"
```

### 10. Memory/Resource Limit
```bash
fixit "python3 -c 'a = [0] * 10**10'"
```