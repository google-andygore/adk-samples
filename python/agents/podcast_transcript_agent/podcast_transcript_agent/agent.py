from google.adk.agents import Agent, SequentialAgent

#from podcast_transcript_agent.models.podcast_topics import PodcastTopics
#from podcast_transcript_agent.models.podcast_plan import PodcastEpisodePlan
#from podcast_transcript_agent.models.podcast_transcript import PodcastTranscript

from .sub_agents.podcast_topics import podcast_topics_agent
from .sub_agents.podcast_episode_planner import podcast_episode_planner_agent
from .sub_agents.podcast_transcript_writer import podcast_transcript_writer_agent

from google.genai import types
from io import BytesIO
import base64

podcast_transcript_agent = SequentialAgent(
    name="podcast_transcript_agent",
    description="Executes a sequence of podcast generation steps",
    sub_agents=[podcast_topics_agent, podcast_episode_planner_agent, podcast_transcript_writer_agent]
)

root_agent = podcast_transcript_agent    
