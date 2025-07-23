import streamlit as st
import asyncio
import os
from config.docker_utils import start_docker_container, stop_docker_container, GetDockerCommandLineExecutor
from models.google_model_client import GetModelClient
from teams.analyzer_gpt import GetAnalyzerGPTTeam
from autogen_agentchat.messages import TextMessage
from autogen_agentchat.base import TaskResult



st.set_page_config(page_title="Analyzer GPT", page_icon=":robot_face:")
st.title("Analyzer GPT - Digital Data Analysis Agent")
st.write("This application allows you to interact with Data Analyzer, a digital data analysis agent that can analyze datasets and execute code.")


uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'autogen_state' not in st.session_state:
    st.session_state.autogen_state = None

task = st.chat_input("Enter your analysis task:")

async def run_analysis(docker, model_client,task):

    await start_docker_container(docker)
    team = GetAnalyzerGPTTeam(docker, model_client) 

    if st.session_state.autogen_state is not None:
        await team.load_state(st.session_state.autogen_state)
        

    try:
        async for message in team.run_stream(task=task):
            
            if isinstance(message, TextMessage):
                print(msg:= f"{message.source}: {message.content}")
                st.session_state.messages.append(msg)

                if msg.startswith('user'):
                    with st.chat_message("user", avatar="👤"):
                        st.markdown(msg)
                elif msg.startswith('DataAnalyserAgent'):
                    with st.chat_message("assistant", avatar="🧠"):
                        st.markdown(msg)
                elif msg.startswith('CodeExecutorAgent'):
                    with st.chat_message("assistant", avatar="🤖"):
                        st.markdown(msg)
                st.markdown(msg)
                st.session_state.messages.append(msg)

            elif isinstance(message, TaskResult):
                print(msg:= f"Stop Reason: {message.stop_reason}")
                st.markdown(msg)
                st.session_state.messages.append(msg)

        st.session_state.autogen_state = await team.save_state()
        return None  
    
    except Exception as e:
        print(f"Error during analysis: {e}")
        return f"Error: {e}"
    
    finally:
        await stop_docker_container(docker)

if st.session_state.messages:
    for msg in st.session_state.messages:
        st.markdown(msg)
            

if task:
    if uploaded_file is not None and task:

        if not os.path.exists('temp'):
            os.makedirs('temp', exist_ok=True)

        with open('temp/data.csv', 'wb') as f:
            f.write(uploaded_file.getbuffer())

    model_client = GetModelClient()
    docker = GetDockerCommandLineExecutor()

    error = asyncio.run( run_analysis(docker, model_client, task) )

    if error:
        st.error("An error occurred during analysis: ", error)
    
    if os.path.exists('temp/output.png'):
        st.image('temp/output.png', caption='Analysis Result', use_column_width=True)

else:
    st.warning("Please upload a CSV file and enter a task to run the analysis.")