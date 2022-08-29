This repo practices a face classification to server and packaging.

Run with cpu
```
DOCKER_BUILDKIT=1 docker build -t classification_cpu -f cpu.Dockerfile .
```

```
docker run --rm -it -p 8045:8045 classification_cpu
```

Run with gpu
```
DOCKER_BUILDKIT=1 docker build -t classification_gpu -f gpu.Dockerfile .
```

```
docker run --gpus=all --rm -it -p 8045:8045 classification_gpu
```

If you want test with streamlit, let's create a new terminal, and run:
```
streamlit run streamlit/streamlit.py
```