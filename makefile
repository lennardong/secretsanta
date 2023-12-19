
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

all_local: frontend_build local_cleanup local_build local_run
all_gcp: frontend_build gcp_build gcp_deploy

################################################################################
# DOCKER LOCAL
################################################################################

# Build Docker image
local_build:
	docker build -t $(DOCKER_IMAGE):$(DOCKER_TAG) .

local_run:
	docker run -p 8080:8080 -e PORT=8080 $(DOCKER_IMAGE):$(DOCKER_TAG)

local_cleanup:
	docker ps -a | grep "$(DOCKER_IMAGE)" | awk '{print $$1}' | xargs -r docker stop
	docker ps -a | grep "$(DOCKER_IMAGE)" | awk '{print $$1}' | xargs -r docker rm
	docker images "$(DOCKER_IMAGE):$(DOCKER_TAG)" | grep -q . && docker rmi "$(DOCKER_IMAGE):$(DOCKER_TAG)" || true


################################################################################
# GCP DEPLOY
################################################################################

# Deploy to Cloud Run
# 1) build using cloud build 
# 2) push to container registry 
# 3) deploy to Cloud Run

# REF for buildx due to M1 : https://stackoverflow.com/questions/66127933/cloud-run-failed-to-start-and-then-listen-on-the-port-defined-by-the-port-envi

gcp_build:
	docker buildx build --platform linux/amd64 -t $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) . && \
	docker push $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) && \
	docker rmi "$(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG)"

gcp_deploy:
	gcloud services enable run.googleapis.com && \
	gcloud run deploy $(SERVICE_NAME) \
		--image $(REGION)-docker.pkg.dev/$(PROJECT_ID)/$(ARTEFACT_REPO)/$(IMAGE_NAME):$(DOCKER_TAG) \
		--platform managed \
		--region $(REGION) \
		--allow-unauthenticated

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
