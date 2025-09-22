import json
from typing import List, Literal, Union, Annotated
from pydantic import BaseModel, Field
from podcast_transcript_agent.models.podcast_transcript import PodcastSpeaker

class ScriptPoint(BaseModel):
    """Represents a single line of dialogue from a specific speaker."""
    speaker: str
    dialogue: str
    
class Segment(BaseModel):
    """A model for a 'main_segment', which includes a title."""
    title: str
    script_points: List[str]
class PodcastEpisodePlan(BaseModel):
    """Represents the entire episode, containing a title and a list of segments."""
    episode_title: str
    speakers: List[PodcastSpeaker]
    segments: List[Segment]
    
    
    