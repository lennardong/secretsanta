# Secret Santa 

This is a fun repo to work through the secret santa problem. 

## Backend Infrastructure

**For infrastructure, you’re going to 1) deploy as source to a 2) container service** 

We'll be using GCP, but the concept is the same for AWS, Azure or other solutions like DigitalOcean / Heroku.

Lets break it down. 

### "Deploy to a Container Service"
> What is a container service? What alternatives are there?

Its helpful to think of this as a ladder that goes from self-managed to fully managed. Let's climb this ladder, starting from the most basic and progressing towards fully automated solutions.

- **Infrastructure as a Service (IaaS), The Barebones Approach:** Here, you rent a virtual machine (VM) and essentially receive a bare shell with an operating system installed. This means you're responsible for setting up everything, from web servers like Nginx and Apache to your application itself. It's like renting an empty room and being responsible for all the furniture and decorations.
- **Container as a Service (CaaS), Autoscale and Simplified Management:** CaaS takes care of the underlying infrastructure, allowing you to focus on your application. It provides a platform for running containerized applications, offering automatic scaling and resource management. This is like renting a furnished apartment – the basics are taken care of, but you're still responsible for the upkeep and customization.
- **Function as a Service (FaaS), Leave the Heavy Lifting to the Cloud:** FaaS takes things a step further. You don't even need to manage the application layer; you simply provide the logic in the form of small, focused functions. The FaaS platform handles everything else, from execution to scaling. Think of it like ordering takeout – you just tell the restaurant what you want, and they prepare and deliver it to you.

### "Deploy as Source"

> Deploy from source? What does that mean, what are the alternatives?

At the end of the day for CaaS, the code still gets packaged into a container and served on a CaaS solution. The main difference lies in *how* the application is prepared and packaged for deployment:

**Deploying from source:**

- **Cloud Build handles the packaging:** Google Cloud Build takes your source code and builds a container image using Buildpacks or a Dockerfile. The buildpack is a fast pre-configured solution (see [https://buildpacks.io/](https://buildpacks.io/)) while a Dockerfile allows fine-grained user configuration. 
- **Cloud Run serves the container:** Once the image is built, Cloud Run pulls it from Artifact Registry or Cloud Storage and serves it to users.

**Deploying from container:**

- **User builds the container:** You build the container image using Docker and push it to Google Container Registry.
- **Cloud Run serves the container:** Cloud Run simply pulls the pre-built image from Container Registry and serves it to users.

### Summary

For SecretSanta, you'll be using CaaS deployed from source because it offers a streamlined workflow with automatic builds and updates, allowing you to focus on developing and testing the application efficiently while still getting some experience of the full application process. 

(Additionally, the flexibility of Buildpacks and Dockerfiles provides us with the control and customization you may need for future iterations of the application!)