# Build-an-LLM-Powered-Prompt-Router-for-Intent-Classification
# Build an LLM-Powered Prompt Router for Intent Classification

## Overview
This project implements a prompt routing system that classifies user queries into different intents and routes them to specialized expert personas. The router analyzes the user input and determines whether the request is related to coding, data analysis, writing assistance, career advice, or if the intent is unclear.

The system is designed as a backend service demonstrating prompt engineering, intent classification, logging, and containerized deployment.

## Features
- Intent classification for user prompts
- Routing to expert personas:
  - Code Expert
  - Data Analyst
  - Writing Coach
  - Career Advisor
- Handles unclear or ambiguous inputs
- Logs routing decisions for debugging and analysis
- Containerized deployment using Docker
- Simple command-line interface for testing

## Supported Intents
The system detects the following intents:

- `code` – Programming and debugging related queries
- `data` – Data analysis and statistics related queries
- `writing` – Content rewriting and writing improvement
- `career` – Resume, interview, and career advice
- `unclear` – Ambiguous or unrelated queries
llm-prompt-router
│
├── app.py # Main application
├── prompts.py # Intent classification logic
├── logger.py # Logging system
├── requirements.txt # Python dependencies
├── Dockerfile # Docker container setup
├── docker-compose.yml # Container orchestration
├── README.md # Project documentation
├── .env.example # Environment variables template
└── route_log.jsonl # Log file for routing decisions
Examples of supported user prompts:

