# Tweet Generator 

This project will make tweets! 

(And now it is dockerized!!)

1. [Build the Image](#build-the-image)
1. [Run the Container](#build-the-container)
1. [Access via Browser](#access-via-browsers)

## Command Reference

### To use Docker Compose

```bash
docker-compose up --build 
```

### 1. Build the Image

```bash
docker build -t tweet-generator .
```

### 2. Run the Container

```bash
docker run -p 8080:5000 tweet-generator
```

### 3. Access via Browser

http://localhost:8080/