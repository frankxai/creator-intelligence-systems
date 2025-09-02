# Genius Creator System

The best system to get into creator mode leveraging latest AI advancements. Go from just brainstorming in chatgpt to actually creating your dreams.

This system is an intelligent workflow and automation layer designed to help creators capture, organize, and act on their ideas. It orchestrates powerful, existing AI assistants with a local file system and Git version control.

## How it Works

1.  **Capture:** Drop raw idea files into the `ideas/inbox` directory.
2.  **Orchestrate:** Run Python scripts from the `src/scripts` directory to process the inbox.
3.  **Delegate & Analyze:** The scripts delegate the analysis to a powerful AI assistant (like Gemini, Claude, etc.) using pre-defined prompts.
4.  **Organize:** The AI's structured output is used to create clean, organized Markdown files in the `ideas/processed` directory.
5.  **Version:** All changes are automatically committed to Git, creating a versioned, structured knowledge base.

## Landing Page

A promotional landing page is being developed in the `landing-page` directory.