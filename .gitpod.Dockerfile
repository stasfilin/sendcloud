FROM gcr.io/cloud-marketplace-containers/google/bazel:latest

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y python3.8 python3.8-distutils python3.8-pip
