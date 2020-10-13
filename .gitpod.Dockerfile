FROM gcr.io/cloud-marketplace-containers/google/bazel:latest

RUN apt-get update && apt-get upgrade -y python3 && apt-get install -y \
    python3-pip
