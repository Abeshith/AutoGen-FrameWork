from autogen_ext.code_executors.docker import DockerCommandLineCodeExecutor
from config.constants import WORK_DIR, TIMEOUT, IMAGE
def get_docker_executor():
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