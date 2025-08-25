# politics-ai

> An open-source, locally runnable AI chatbot focused on answering political concepts, news, and policy positions with clear attribution and configurable safety rails.

This repository contains a service OPEN AI API for chatting with an AI about politics. It currently supports only OpenAI providers, has safety guardrails, and can optionally use retrieval for factual grounding.

---

## Table of Contents
- [About](#about)
- [.env & Config Files](#env--config-files)
- [Steps to Run / Debug](#steps-to-run--debug)
- [Sample Screenshots](#sample-screenshots)

---

## About

**politics-ai** is designed to:
- Provide clear, accessible explanations of political topics.
- Support Open AI LLM providers via a single abstraction layer.
- Enforce configurable moderation and safety rules.
- Run locally (offline) using OpenAI API key.

## .env & Config Files

### `.env` file
The `.env` file is used to store runtime environment variables. Copy from `.env.example` and update OPEN_API_KEY.

### `.yaml` config files
The config files in /config folder contains model parameters and some static prompts used to give initial instructions to the chatbot

## Steps to Run / Debug
- Make /src folder a sources root folder in pycharm/vscode (it's also specified as PYTHONPATH in env file)
- Activate the virtual environment
- Setup the Run / Debug configuration to point to file main.py or you can directly execute this file from IDE
