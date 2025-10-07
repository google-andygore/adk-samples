# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from typing import List
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