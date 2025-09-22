import json
from typing import List, Literal, Union, Annotated
from pydantic import BaseModel, Field


class SpeakerDialogue(BaseModel):
    speaker_id: str
    text: str

class PodcastSegment(BaseModel):
    segment_title: str
    title: str
    start_time: float
    end_time: float
    speaker_dialogues: List[SpeakerDialogue]

class PodcastSpeaker(BaseModel):
    speaker_id: str
    name: str
    role: str
    
class PodcastMetadata(BaseModel):
    episode_title: str
    duration_seconds: int
    summary: str

class PodcastTranscript(BaseModel):
    metadata: PodcastMetadata  
    speakers: List[PodcastSpeaker]
    segments: List[PodcastSegment]