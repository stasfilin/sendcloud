FROM gcr.io/cloud-marketplace-containers/google/bazel:latest

RUN apt-get update && apt-get install -y \
    python3-pip
