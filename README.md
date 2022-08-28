This repo practices a face classification to server with chain.

```
DOCKER_BUILDKIT=1 docker build -t classification_cpu -f cpu.Dockerfile .
```

```
docker run --rm -it -p 11234:8001 classification_cpu
```

```
DOCKER_BUILDKIT=1 docker build -t classification_gpu -f gpu.Dockerfile .
```

```
docker run --rm -it -p 11234:8001 classification_gpu
```