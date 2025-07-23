import streamlit as st
from teams.dsa_solver import create_dsa_solver_team
from config.docker_utils import start_docker_container, stop_docker_container
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult
import asyncio

st.set_page_config(page_title="DSA Solver Agent", page_icon=":robot_face:")
st.title("DSA Solver Agent")
st.write("This application allows you to interact with a DSA Solver Agent that can solve coding problems and execute code.")


task = st.text_input("Enter your coding problem:", placeholder  ="Write a Python code to find an Armstrong number between 1 - 100.")

async def run(team, docker, task):
    try:
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                yield msg
            elif isinstance(message, TaskResult):
                print(msg:= f"Task Result: {message.stop_reason}")
                yield msg
        print("Task completed.")
    except Exception as e:
        print(f"Error during code execution: {e}")
        yield f"Error: {e}"
    finally:
        await stop_docker_container(docker)
        


if st.button("RUN"):
    st.write("Running the DSA Solver Agent...")

    team, docker = create_dsa_solver_team()

    async def collect_messages():
        async for msg in run(team, docker, task):
            if isinstance(msg, str):
                if msg.startswith("User:"):
                    with st.chat_message("user", avatar="👤"):
                        st.markdown(msg)
                elif msg.startswith("ProblemSolverAgent:"):
                    with st.chat_message("assistant", avatar="🧠"):
                        st.markdown(msg)
                elif msg.startswith("CodeExecutorAgent:"):
                    with st.chat_message("assistant", avatar="🤖"):
                        st.markdown(msg)

            elif isinstance(msg, TaskResult):
                with st.chat_message("stopper", avatar="🚫"):
                    st.markdown(f"Task Result: {msg.result}")


    asyncio.run(collect_messages())



