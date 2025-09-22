# Podcast Transcript Agent

The Podcast Transcript Agent is a powerful tool that automates the creation of podcast transscripts from any PDF/Markdown/Text document. By leveraging a series of specialized AI agents, it can take a source document and generate a complete, conversational podcast transcript.

## Architecture

The Podcast Agent operates as a sequential process, where each step is handled by a dedicated sub-agent. The output of one agent becomes the input for the next, ensuring a smooth and logical workflow from topic extraction to the final script.

![Podcast Transcript Agent Architecture](assets/podcast_transcript_agent_architecture_v2.png)

## Sub-Agents

### 1. Podcast Topics Agent (`podcast_topics_agent`)

*   **Goal:** To analyze the source document and extract the core information needed to build a podcast episode.
*   **Process:** This agent reads the provided text and identifies:
    *   The main topic.
    *   A summary of the central argument and conclusion.
    *   The five most important subtopics, complete with descriptive titles, summaries, and key statistics.
*   **Output:** A structured `PodcastTopics` object containing the extracted information.

### 2. Podcast Episode Planner Agent (`podcast_episode_planner_agent`)

*   **Goal:** To create a high-level structure for the podcast episode.
*   **Process:** Using the topics and summaries from the previous step, this agent builds a 5-segment episode plan. The plan includes:
    *   A catchy episode title.
    *   An introduction to hook the listener.
    *   Five main segments for the core discussion.
    *   A conclusion to summarize the key takeaways.
*   **Output:** A `PodcastEpisodePlan` object that outlines the episode.

### 3. Podcast Transcript Writer Agent (`podcast_transcript_writer_agent`)

*   **Goal:** To write a complete, conversational podcast script.
*   **Process:** This is the final step in the pipeline. The agent takes the episode plan and the detailed factual information and writes a script featuring two personas:
    *   **Host:** Guides the conversation and engages the audience.
    *   **Expert:** Provides in-depth knowledge based on the source document.
*   **Output:** A `PodcastTranscript` object containing the full script with clear speaker labels.

## Setup and Usage

### Environment Variables

Before running the agent, you need to configure your environment. There are two ways to do this:

**1. API Key Authentication**

Create a `.env` file in the `src/podcast_transcript_agent` directory with the following content:

```bash
GEMINI_API_KEY="your-api-key"
```

Replace `"your-api-key"` with your actual Gemini API key.

**2. Vertex AI Authentication**

If you are using Vertex AI, you need to authenticate using `gcloud` and set the following environment variables. Create a `.env` file in the `src/podcast_transcript_agent` directory with the following content:

```bash
GOOGLE_GENAI_USE_VERTEXAI=TRUE
GOOGLE_CLOUD_PROJECT="your-gcp-project-id"
GOOGLE_CLOUD_LOCATION="your-gcp-region"
```

Replace `"your-gcp-project-id"` and `"your-gcp-region"` with your actual GCP project ID and region.

You also need to be authenticated with `gcloud`. If you haven't already, run the following command:

```bash
gcloud auth application-default login
```

### Installation

1.  **Installation:**

    First, create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

    Then, install the required dependencies from the `src/requirements.txt` file:

    ```bash
    pip install -r src/requirements.txt
    ```

2.  **Running the Agent:**

    You can run the agent using the example scripts in the `tests` directory.

    **With a PDF file (`test_paper.pdf`):**

    ```bash
    ./tests/run_with_pdf.sh
    ```

    **With a text file (`test_pyramid.txt`):**

    ```bash
    ./tests/run_with_txt.sh
    ```

    These scripts will run the agent with the provided test artifacts and output the final transcript to the console.