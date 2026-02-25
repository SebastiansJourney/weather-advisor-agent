# 🌤️ Weather Advisor Agent

An AI-powered weather advisor that combines real-time and forecast weather data to give you practical, conversational recommendations — not just numbers.

Ask it things like:
- *"Do I need an umbrella in Hamburg tomorrow?"*
- *"What should I wear in Munich this weekend?"*
- *"Is it beach weather in Barcelona next Friday?"*

The agent translates your natural language question into location coordinates, fetches live weather data, and responds with concrete advice on clothing, gear, and accessories.

## 🛠️ Tech Stack

- **[smolagents](https://github.com/huggingface/smolagents)** — agent framework handling tool calling and the ReAct loop
- **[Open-Meteo API](https://open-meteo.com/)** — free, no-key-required weather data
- **[Anthropic Claude](https://www.anthropic.com/)** — LLM for reasoning and natural language responses
- **Python** — `requests`, `python-dotenv`

## 🚀 How to Run

1. Clone the repo
2. Create a virtual environment and install dependencies:
```bash
   pip install -r requirements.txt
```
3. Add your Anthropic API key to `.env`:
```
   ANTHROPIC_API_KEY=your_key_here
```
4. Run the agent:
```bash
   python agent.py
```

## 📁 Project Structure
```
weather-advisor-agent/
├── .env               # API keys (not committed)
├── .gitignore
├── README.md
├── requirements.txt
└── agent.py           # Main agent logic
```

## ⚠️ Notes

- No weather API key needed — Open-Meteo is fully free and open-source
- Costs fractions of a cent per query via Anthropic API