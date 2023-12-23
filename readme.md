# SecretSanta Matchmaker

**Backstory**

This is a fun holiday project to help SecretSanta Matchmaking for extended families and friends.
(After a heavy stretch of research and papers with serious sounding names (“... albation study of ...”), I felt it was time to bring some fun back into technology.) 

**🎄 What's Secret Santa?**
- Its a gift-pairing tool that matches up people while respecting do's and do-not's.
- Think:
- ... Wolverine shouldn't be paired with Cyclops (relationship too cool),
- ... Peter Parker shouldn't be paired with Mary Jane (relationship too warm).

**🔧 What was being explored?**
- I was curious to explore the JAMstack idea a nudge further.
- This project blends the fun of svelte with the familiarity of a python backend.
- It also does away with microservices and manages it as a single monolothic deploy. 

**💻️ Keen to Try It?** 
- App Website - https://santa-service-mp4xuvosiq-as.a.run.app/static/ (its janky)

## Stack

* Backend: Python, FastAPI, Uvicorn
* Frontend: Svelte
* Infrastructure: Docker -> Google Artifact Registry -> Google Cloud Run

**Project Structure**

* `core` - contains the core logic for the app
* `frontend` - contains the frontend code
* `archive` - contains the old code that was used to build the app
* `tests` - contains basic pytests for the app logic
* `tests_bruno` - contains the tests for the API endpoints

**Other Notes**
* Serving Static Assets - FastAPI used to serve the static assets from Svelte. 
* Dev/Build: Makefiles used for most of the dev and build processes. Look through it for details
* Deploying to GCP: this was a real gotcha. in Dockerfile, make sure to specify the OS as linux/amd64. Otherwise, the build will fail with a cryptic error message.
* Bruno: a really simple and effective tool for testing APIs. Highly recommended for future projects. 

## Future Roadmaps

**Features to add**
* Admin Saver: Add a way to send out the assignments to the participants
* Value Add: add a way for participants to add their wishlists
* Engagement: Implement a bot-driven approach to participation, maybe in WA or a Telegram Chat
* Make it Interactive: Implement a graph visualization of the match-making process
* UI: make it MORE 90's CRT with frames or move to a more contemporary aesthetic.
* URL: link it as a subdomain to my personal website

**Technologies / Approaches to try**
* Think Different: Approach match-making as a graph problem, maybe using a graph database like Neo4J
* Make it TypeSafe: Use Typescript for the frontend
* Go "Cloudless": Use a CI/CD pipeline to deploy a custom VM on Digital Ocean or similar
* GraphQL: might as well try to implement this using GraphQL instead of REST

