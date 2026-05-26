# AI Personal Assistant Evaluation

Comparing an Open-Source (Qwen2.5) vs Frontier (Claude Sonnet) personal assistant on hallucination, safety, and bias.

## 🔗 Live Demos
- [OSS Assistant (Qwen2.5)](https://huggingface.co/spaces/varshaveeramalli/oss-assisant)
- [Frontier Assistant (Claude Sonnet)](https://huggingface.co/spaces/varshaveeramalli/frontier-assistant)

## 🏗️ Architecture

Both assistants use identical Gradio UI and the same system prompt:
- **OSS:** Qwen2.5-72B-Instruct via Hugging Face Inference API (free serverless)
- **Frontier:** Claude Sonnet via Anthropic API (pay-per-token)

Both support multi-turn conversations with full conversational memory (entire history passed on every turn).

## ⚖️ Tradeoffs

| | OSS (Qwen2.5-72B) | Frontier (Claude Sonnet) |
|---|---|---|
| Cost | Free (HF Inference API) | Pay-per-token |
| Latency | Variable (shared infra) | Consistent |
| Safety | Good | Excellent |
| Factual Accuracy | Very good | State-of-the-art |
| Jailbreak Resistance | Moderate | Strong |
| Setup Complexity | Low | Low |

## 🔬 Evaluation Method

LLM-as-judge using Claude Sonnet to score both models across 3 categories:

1. **Hallucination Rate** — factual questions with known answers
2. **Content Safety** — jailbreak and adversarial prompt resistance  
3. **Bias & Fairness** — sensitive/stereotype-laden prompts

Each response scored 0–10. Results in `/evaluation/report.md`.

## 📁 Project Structure
ai-assistant-evaluation/
├── oss-assistant/
│   ├── app.py              # Qwen2.5 Gradio chatbot
│   └── requirements.txt
├── frontier-assistant/
│   ├── app.py              # Claude Sonnet Gradio chatbot
│   └── requirements.txt
├── evaluation/
│   └── report.md           # Full evaluation results
└── README.md
## 🚀 Setup Instructions

### OSS Assistant
```bash
pip install gradio huggingface_hub
export HF_TOKEN=your_token_here
python oss-assistant/app.py
```

### Frontier Assistant
```bash
pip install gradio anthropic
export ANTHROPIC_API_KEY=your_key_here
python frontier-assistant/app.py
```

## 🔧 What I'd Improve With More Time
- Persistent memory using a vector database (e.g. ChromaDB)
- Tool use: web search, calculator, calendar
- Automated red-teaming with 100+ adversarial prompts
- Dedicated GPU deployment for OSS model (lower latency)
- Cost tracking dashboard
- A/B testing framework for systematic comparison
