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

<!-- STARLIGHT:OPERATING:BEGIN v2 sha=9f8fecc91edc source=794db1e51a55a128816f7aa266eb0ac1dbd452c3 -->

## Agent operating guidance

Repository agents use the shared Starlight operating contract in `AGENTS.md` alongside local instructions.
The contract asks agents to establish a useful outcome, select relevant skills, complete authorized work,
verify current sources, refine the actual artifact, and report evidence and remaining gates.
It covers human agency, privacy, rights, resource stewardship and bounded proactivity.
Repository identity, brand, canon, build commands and release gates remain local.

[Pinned contract](https://github.com/frankxai/Starlight-Intelligence-System/blob/794db1e51a55a128816f7aa266eb0ac1dbd452c3/docs/architecture/agents-md/band-a.md)
· [Projection and verification](https://github.com/frankxai/Starlight-Intelligence-System/blob/794db1e51a55a128816f7aa266eb0ac1dbd452c3/docs/architecture/AGENTS-MD-CONTRACT.md)

These files supply operating guidance. They do not activate an agent, grant tool permissions,
schedule recurring work, certify compliance or prove a live capability.

<!-- STARLIGHT:OPERATING:END -->
