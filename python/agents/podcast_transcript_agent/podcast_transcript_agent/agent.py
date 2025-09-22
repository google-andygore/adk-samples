from google.adk.agents import Agent, SequentialAgent
from . import prompt

from podcast_transcript_agent.models.podcast_topics import PodcastTopics
from podcast_transcript_agent.models.podcast_plan import PodcastEpisodePlan
from podcast_transcript_agent.models.podcast_transcript import PodcastTranscript
from google.genai import types
from io import BytesIO
import base64


podcast_topics_agent = Agent(
    name="podcast_topics_agent",
    model="gemini-2.5-flash",
    description="Extracts podcast topics from provided input",
    instruction= prompt.TOPIC_EXTRACTION_PROMPT,
    output_schema=PodcastTopics,
    output_key="podcast_topics"
)

podcast_episode_planner_agent = Agent(
    name="podcast_episode_planner_agent",
    model="gemini-2.5-flash",
    description="Plans the podcast episode based on extracted topics",
    instruction=prompt.PODCAST_EPISODE_PLANNER_PROMPT,
    output_schema=PodcastEpisodePlan,
    output_key="podcast_episode_plan"
)

podcast_transcript_writer_agent = Agent( 
    name="podcast_transcript_writer_agent",
    model="gemini-2.5-flash",
    description="Writes the podcast transcript based on the podcast plan",
    instruction=prompt.PODCAST_TRANSCRIPT_WRITER_PROMPT,
    output_schema=PodcastTranscript,
    output_key="podcast_episode_transcript"
 )

podcast_transcript_agent = SequentialAgent(
    name="podcast_transcript_agent",
    description="Executes a sequence of podcast generation steps",
    sub_agents=[podcast_topics_agent, podcast_episode_planner_agent, podcast_transcript_writer_agent]
)

root_agent = podcast_transcript_agent    
