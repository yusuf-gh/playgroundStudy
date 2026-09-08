# Command for installing the terminal version of docker as well as "colima" to use the built-in virtualization 
# on macOS. This will give you maximum operating speed.

```brew install docker colima```

# After the installation run this

```colima start --vm-type=vz --vz-rosetta```

# This process may take a couple of minutes the first time you run it, 
# as Colima will create and configure a Linux virtual machine inside your Mac.
# so after running this command the colima already started and you can use the all the docker commands

## 🎯 Commands `docker...`

### 🔎 Info & Status
- `info` — displays system-wide information regarding containers, images, and current statuses.
- `version` — shows the Docker client and server versions.

### 📦 Container Management
- `start -ai <container name>` — *flags* `attach` + `interactive` to start a container in interactive mode and attach it to current terminal window
- `ps` — lists all currently *running* containers.
- `ps -a` — lists *all* containers (both running and stopped).
- `run <image_name>` — pulls the image (if not found locally) and starts a new container.
- `run -d -p <host_port>:<container_port> <image_name>` — runs a container in the background (detached mode) and maps ports.
- `start <container_id/name>` — starts one or more stopped containers.
- `stop <container_id/name>` — gracefully stops a running container.
- `rm <container_id/name>` — removes a stopped container.

### 🖼 Image Management
- `images` (or `image ls`) — lists all locally downloaded images.
- `pull <image_name>` — downloads an image from Docker Hub without running it.
- `rmi <image_id/name>` — removes a local image.
- `build -t <tag_name> .` — builds a custom Docker image from the `Dockerfile` in the current directory.

### 📊 Logs & Debugging
- `logs <container_id/name>` — fetches the logs (console output) of a specific container.
- `logs -f <container_id/name>` — follows log output in real-time.
- `exec -it <container_id/name> bash` (or `sh`) — opens an interactive terminal session inside a running container.

### 🧹 System Cleanup
- `system prune` — removes all stopped containers, unused networks, and dangling build cache.
- `system prune -a --volumes` — deep clean: removes all stopped containers, unused images, and data volumes to free up disk space.

