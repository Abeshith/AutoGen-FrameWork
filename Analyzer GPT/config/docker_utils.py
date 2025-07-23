from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR, TIMEOUT, IMAGE

def GetDockerCommandLineExecutor():
    """
    Initializes and returns the DockerCommandLineCodeExecutor.
    """
    docker = DockerCommandLineCodeExecutor(
        image=IMAGE,
        work_dir=WORK_DIR,
        timeout=TIMEOUT,
    )
    print("DockerCommandLineCodeExecutor initialized with image:", IMAGE)
    return docker


async def start_docker_container(docker):
    """
    Starts the Docker container using the provided executor.
    """
    print("Starting Docker container...")
    await docker.start()
    print("Docker container started.")


async def stop_docker_container(docker):
    """
    Stops the Docker container using the provided executor.
    """
    print("Stopping Docker container...")
    await docker.stop()
    print("Docker container stopped.")