import json
from typing import List, Literal, Union, Annotated
from pydantic import BaseModel, Field

class Topic(BaseModel):
    topic_name: str = Field(..., description="A concise and catchy title for the podcast topic.")
    description: str = Field(..., description="A detailed, engaging description for the podcast topic, around 2-3 sentences long.")
    key_facts: list[str]

class PodcastTopics(BaseModel):
    main_topic: str = Field(..., description="A concise and catchy title for the podcast topic.")
    sub_topics: List[Topic]

    
