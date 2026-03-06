# 🌦️ Weather Advisor Agent

> An AI-powered weather assistant that goes beyond forecasts — it tells you what to *do* with the weather.

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Claude API](https://img.shields.io/badge/LLM-Claude%20API-D97757?logo=anthropic)](https://anthropic.com)
[![smolagents](https://img.shields.io/badge/Framework-smolagents-FFD21E)](https://github.com/huggingface/smolagents)

---

## What it does

Most weather apps show you numbers. This agent tells you what those numbers mean for your day.

Ask it things like:
- *"Do I need an umbrella in Hamburg tomorrow?"*
- *"What should I wear in Munich this weekend?"*
- *"Is it beach weather in Barcelona next Friday?"*

The agent translates your natural language question into location coordinates, fetches live weather data, and responds with concrete advice on clothing, gear, and accessories.

**Example output:**

```
User: I'm heading to Hamburg tomorrow for a client meeting and then a run in the park.

Agent: Tomorrow in Hamburg: 8°C, overcast with rain from around 14:00.

For your meeting: A light wool blazer over a base layer will keep you sharp
without bulk. Bring a compact umbrella — not a hood, you'll want your hands free.

For your run: Push it to the morning if you can, ideally before 11:00.
Wind picks up to ~25 km/h by evening, so finish before 18:00.
```

---

## Architecture

The agent uses a **ReAct loop** (Reason → Act → Observe) via smolagents:

```
User Query (natural language)
        │
        ▼
  smolagents ReAct Loop
        │
        ├──► Geocoding Tool  ──► Location → Coordinates
        │
        ├──► Weather Tool (Open-Meteo API) ──► Live + forecast data
        │
        └──► Claude API (Anthropic)
                    │
                    ▼
        Contextual recommendations
        (clothing, gear, timing, warnings)
```

---

## Tech Stack

| Layer | Technology |
|---|---|
| Agent Framework | [smolagents](https://github.com/huggingface/smolagents) |
| LLM | Claude API (Anthropic) |
| Weather Data | [Open-Meteo API](https://open-meteo.com) — free, no key required |
| Language | Python · `requests`, `python-dotenv` |

---

## Project Structure

```
weather-advisor-agent/
├── agent.py           # Main agent logic — ReAct loop + tool definitions
├── requirements.txt
├── .env               # API keys (not committed)
└── .gitignore
```

---

## Getting Started

### Prerequisites
- Python 3.11+
- An Anthropic API key → [Get one here](https://console.anthropic.com)

### Installation

```bash
# Clone the repo
git clone https://github.com/SebastiansJourney/weather-advisor-agent.git
cd weather-advisor-agent

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Configuration

Create a `.env` file in the root directory:

```env
ANTHROPIC_API_KEY=your_api_key_here
```

### Run

```bash
python agent.py
```

---

## Notes

- No weather API key needed — Open-Meteo is fully free and open-source
- Costs fractions of a cent per query via the Anthropic API

---

## Planned Improvements

- [ ] Multi-day planning view
- [ ] Activity-specific profiles (cycling, hiking, commuting)
- [ ] Streamlit UI for non-technical users
- [ ] Calendar integration via MCP

---

## Project Background

Built as part of the **AIPM Bootcamp** (neuefische, Cohort 1 · 2025/26).

A one-day build challenge — zero to deployed AI agent in a single session. Uses the [smolagents](https://github.com/huggingface/smolagents) framework by Hugging Face for ReAct loop orchestration, with Open-Meteo for weather data (no API key required) and Claude for reasoning and natural language generation.

Demonstrates: agentic tool-calling architecture, ReAct loop design, prompt engineering for consistent contextual outputs, and rapid prototyping with minimal dependencies.

---

## Author

**Sebastian** · AIPM Bootcamp · neuefische 2025/26
[GitHub](https://github.com/SebastiansJourney) · [LinkedIn](https://www.linkedin.com/in/sebastian-plum-aipm)
