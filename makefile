
$(info Current directory: $(CURDIR))

# Docker image name and tag
DOCKER_IMAGE := santa-image
DOCKER_TAG := latest

# GCP Variables
PROJECT_ID := secretsanta-407502
IMAGE_NAME := santa-image
SERVICE_NAME := santa-service
REGION := asia-southeast1
ARTEFACT_REPO := secretsanta-repo

all_local: frontend_build docker_build_local docker_run_local

################################################################################
# DOCKER
################################################################################

# Build Docker image
docker_build_local:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

# Run Docker container
# docker_run_local:
# 	docker run -p 8080:8080 -e PORT=8080 --name secretsanta_container $(DOCKER_IMAGE):$(DOCKER_TAG)
# 	# docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG) 
# 	# docker_run_local:
# 	# NOTE: adding the --name flag causes an error

docker_run_local:
	docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG)


# Clean up images and containers
docker_clean_local:
	docker stop $$(docker ps -a | grep "$(DOCKER_IMAGE)" | awk '{print $$1}') && \
	docker rm $$(docker ps -a | grep "$(DOCKER_IMAGE)" | awk '{print $$1}') && \
	docker rmi "$(DOCKER_IMAGE):$(DOCKER_TAG)"

# Push Docker image to Google Container Registry

################################################################################
# GCP
################################################################################

# Deploy to Cloud Run
# 1) build using cloud build 
# 2) push to container registry 
# 3) deploy to Cloud Run

gcp_build_img:
	docker build -t $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) . && \
	docker push $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) && \
	docker rmi "$(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG)"

gcp_pushToCloudRun:
	gcloud services enable run.googleapis.com && \
	gcloud run deploy $(SERVICE_NAME) \
		--image $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) \
		--platform managed \
		--region $(REGION) \
		--allow-unauthenticated


# gcloud builds submit --tag gcr.io/$(PROJECT_ID)/$(DOCKER_IMAGE):$(DOCKER_TAG) .
############################################################################### 
# PYTHON
################################################################################

# Install dependencies
python_install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

# Lint code
python_lint:
	python -m pylint --disable=R,C --extension-pkg-allow-list=cv2 *.py

# Format code
python_format:
	python -m black *.py

# Run tests
python_test:
	python -m pytest -vv --cov=vision --pyargs -k test_vision

python_test_server:
	source venv/bin/activate &&\
	uvicorn main:app --reload


############################################
# FRONT END 
############################################

frontend_build:
	cd frontend &&\
	npm run build

frontend_dev:
	cd frontend &&\
	npm run dev

# Run tests
# test:
# 	python -m pytest -vv --pyargs -k test_
