# REFERENCE: https://fastapi.tiangolo.com/deployment/docker/


FROM python:3.9


WORKDIR /code


# LAYER 1: dependiencies
COPY ./requirements.txt /code/requirements.txt

# INSTALL DEPENDENCIES
# - The --no-cache-dir option tells pip to not save the downloaded packages locally, 
# as that is only if pip was going to be run again to install the same packages, 
# but that's not the case when working with containers.
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./ /code/app

# RUN UVICORN SERVER
# note: 
# - CMD takes a list of strings, each is a what you would type in commandline separated by spaces
# - CMD will be run from curr working directory (i.e. /code, set by WORKDIR
# - Program will be started at `/code` and inside of it is the directory `./app`, uvicorn will see and import app 
# - from app.main 
CMD ["uvicorn", "app.main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]
