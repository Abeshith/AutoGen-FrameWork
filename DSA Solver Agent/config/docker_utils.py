async def start_docker_container(docker):
    """
    Starts the Docker container for code execution.
    """
    print("Starting Docker container...")
    await docker.start()

async def stop_docker_container(docker):
    """
    Stops the Docker container for code execution.
    """
    print("Stopping Docker container...")
    await docker.stop()
    print("Docker container stopped.")