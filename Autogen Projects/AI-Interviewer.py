from autogen_agentchat.agents import AssistantAgent, UserProxyAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console
import asyncio
from autogen_agentchat.base import TaskResult
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")


async def team_config(job_position = "AI/ML Engineer"):
    """
    Configure the team for the interview process.
    
    Args:
        job_position (str): The job position for which the interview is being conducted.
    """
    


    ### Define the Model Client
    model_client = OpenAIChatCompletionClient(
        model="gemini-2.0-flash",
        api_key=api_key,
    )


    ### Define the Agents
    ## 1. Interviewer Agent
    interviewer = AssistantAgent(
        name="Interviewer",
        model_client=model_client,
        system_message=f"""
        You are an Professional interviewer for a Entry Level {job_position} position. 
        Ask one clear question at a time and wait for user to respond Be professional and engaging.
        Your Job is to continue ask question, dont pay attention to career coach response.
        make sure to ask questions that based on candidate's answer and expertise
        Ask 3 questions in total Covering technical skills, problem-solving abilities, and cultural fit.
        After asking 3 questions, conclude the interview with based on the answers whether to hire you or not and then say 'TERMINATE' at the end of the interview.
        """
    )

    ## 2. Interviewee Agent
    candidate = UserProxyAgent(
        name="Interviewee",
        description=f"An applicant for the {job_position} position.",
        input_func= input
    )

    ## 3. Career Coach Agent
    career_coach = AssistantAgent(
        name="Career_Coach",
        model_client=model_client,
        system_message=f"""
        You are a Career Coach specializing in preparing candidates for {job_position} interviews.
        Provide feedback on the interviewee's responses, focusing on strengths and areas for improvement.
        After the interview, summarize the candidate's performance and suggest areas for improvement by providing actionable advice.
        Make Sure to add the contents in less than 50 words which is more important for the candidate to improve.
        """
    )

    ### Define the Team
    team = RoundRobinGroupChat(
        participants=[interviewer, candidate, career_coach],
        termination_condition=TextMentionTermination("TERMINATE"),
        max_turns=10,
    )

    return team

async def team_setup(team):
    """
    Set up the team for the interview process.
    """
    ### Run the Interview
    async for message in team.run_stream(task= "Start the interview with first question?"):
        if isinstance(message, TaskResult):
            message=  f"Task Result: {message.stop_reason}"
            yield message
        else:
            message=  f"{message.source}: {message.content}"
            yield message


async def main():
    """
    Main function to run the AI Interviewer.
    """
    job_position = "Enrty Level AI/ML Engineer"
    team = await team_config(job_position)
    
    print("Setting up the interview team...")
    async for retunedMsg in team_setup(team):
        print('-'*50)
        print(retunedMsg)
    

if __name__ == "__main__":
    asyncio.run(main())

