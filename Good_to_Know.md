# Good to Know

## Command
### Images
- docker images : list images
- docker pull (image name):(image tag) : pull images
- docker rmi (image name):(image tag) : remove images
- docker inspect (image name, container name) : show info
- docker build -t (image name) (path) : create our own Docker image

### Containers
- docker ps : list containers
  - -a : all status
- docker run --name (container name) -d -p (host port):(container port) (image) : build and start container
  - -d : run on background
  - -p : manaul port mapping
  - -P : auto port mapping 
  - -e : export variable
  - -v (local path directory):(container path directory) : bind mount(mostly used to inject data from host to container)1
  - -v (volume name):(container path directory) : volume mount(mostly used to preserve data from container to host)
- docker start/stop/restart/rm (container name or id) : start/stop/restart/rm(can rm only when it in stopped stage) container
  - Must stop before rm
  - Must have existing container before start
- docker logs (container name or ID) : show the stdout and stderr logs from a container (useful for troubleshooting)

### Execute
- docker exec (container name) (command) : run command in container
- docker exec -it (container name) /bin/bash : like ssh to instance but this is in container

### Volume
- docker volume : see the option in Docker Volume

## Dockerhub
- docker login : login using Docker account
- docker push (image name) : push image to dockerhub

## Tips
- If you want any user to use docker command(by default only root user can use it), add that user to the docker group
- Docker directory : /var/lib/docker