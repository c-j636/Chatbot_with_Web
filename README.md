LangGraph Agentic AI Chatbot with Web Search

An Agentic AI chatbot built using LangGraph, LangChain, and Streamlit, capable of autonomous reasoning, tool selection, and real-time web information retrieval.
This project integrates Groq’s high-speed LLMs with Tavily Search API to enable the chatbot to dynamically decide when to search the web and when to answer from context — creating a stateful, tool-augmented AI agent.

Features

Agentic Reasoning – Uses LangGraph to manage multi-step reasoning and state transitions.

Web Search Integration – Retrieves up-to-date information via Tavily API.

Groq LLM – Low-latency, high-performance model execution.

Tool-Oriented Architecture – Dynamically decides which tools to invoke using conditional graph edges.

Streamlit UI – Interactive, browser-based chatbot interface.

Secure API Handling – .env file for safe key storage.

Tech Stack

Python 3.10+

LangGraph & LangChain

Groq LLM API

Tavily Search API

Streamlit

FAISS (optional, for vector storage)
