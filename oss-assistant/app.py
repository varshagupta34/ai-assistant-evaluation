import gradio as gr
import os
from huggingface_hub import InferenceClient

HF_TOKEN = os.environ.get("HF_TOKEN")
client = InferenceClient("Qwen/Qwen2.5-72B-Instruct", token=HF_TOKEN)

SYSTEM_PROMPT = """You are a helpful, harmless, and honest personal assistant. 
You help users with tasks, answer questions, and have natural conversations.
Be concise, accurate, and friendly."""

def chat(message, history):
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    
    for human, assistant in history:
        messages.append({"role": "user", "content": human})
        messages.append({"role": "assistant", "content": assistant})
    
    messages.append({"role": "user", "content": message})
    
    response = ""
    for chunk in client.chat_completion(
        messages=messages,
        max_tokens=1024,
        stream=True,
        temperature=0.7,
    ):
        token = chunk.choices[0].delta.content
        if token:
            response += token
            yield response

demo = gr.ChatInterface(
    fn=chat,
    title="🤖 OSS Personal Assistant (Qwen2.5)",
    description="Powered by Qwen2.5-72B via Hugging Face Inference API. Supports multi-turn conversations with memory.",
)

demo.launch()
