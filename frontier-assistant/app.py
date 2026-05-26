import gradio as gr
import anthropic
import os

client = anthropic.Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """You are a helpful, harmless, and honest personal assistant.
You help users with tasks, answer questions, and have natural conversations.
Be concise, accurate, and friendly."""

def chat(message, history):
    messages = []
    
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": message})
    
    response = ""
    with client.messages.stream(
        model="claude-sonnet-4-5",
        max_tokens=1024,
        system=SYSTEM_PROMPT,
        messages=messages,
    ) as stream:
        for text in stream.text_stream:
            response += text
            yield response

demo = gr.ChatInterface(
    fn=chat,
    title="🚀 Frontier Assistant (Claude Sonnet)",
    description="Powered by Anthropic Claude Sonnet. Supports multi-turn conversations with memory.",
)

demo.launch()
