import os
import shutil
import pathlib
import sys

def process_idea_orchestrator():
    project_root = pathlib.Path(__file__).parent.parent.parent
    inbox_path = project_root / "ideas" / "inbox"
    processed_path = project_root / "ideas" / "processed"
    processed_inbox_path = project_root / "ideas" / "processed_inbox"
    strategy_path = project_root / "strategy"
    agent_md_path = project_root / "agent.md"

    # Ensure processed directories exist
    processed_path.mkdir(parents=True, exist_ok=True)
    processed_inbox_path.mkdir(parents=True, exist_ok=True)

    # Find the idea file (assuming only one for this example)
    idea_file = None
    for f in inbox_path.iterdir():
        if f.is_file() and f.name.endswith(".txt"):
            idea_file = f
            break

    if not idea_file:
        print("No idea file found in inbox. Please place a .txt file in ideas/inbox/.")
        return

    idea_name = idea_file.stem # Get name without extension
    idea_full_path = idea_file.relative_to(project_root) # Relative path for CLI

    # --- Generate CLI Commands ---
    print("="*80)
    print("CHOOSE YOUR AI TOOL AND RUN THE CORRESPONDING COMMAND:")
    print("="*80)

    # Common context for all commands
    common_context_flags = f"--project-dir \"{project_root}\" --agent-file \"{agent_md_path.relative_to(project_root)}\""
    idea_input_flag = f"--input-file \"{idea_full_path}\""
    strategy_context_flag = f"--strategy-dir \"{strategy_path.relative_to(project_root)}\""

    # 1. Gemini Code Assistant CLI (Hypothetical)
    gemini_command = f"gemini {common_context_flags} {idea_input_flag} {strategy_context_flag}"
    print("\n--- For Gemini Code Assistant CLI ---")
    print(gemini_command)

    # 2. Claude Code CLI (Hypothetical)
    claude_command = f"claude --context-dir . --instructions \"{agent_md_path.relative_to(project_root)}\" --input \"{idea_full_path}\" --strategy \"{strategy_path.relative_to(project_root)}\""
    print("\n--- For Claude Code CLI ---")
    print(claude_command)

    # 3. Codex CLI (OpenAI - Hypothetical)
    # Note: OpenAI CLI often uses 'api completions create' or similar, and might not directly take agent files.
    # This is a more speculative command, assuming a direct 'codex' command for agent-like behavior.
    codex_command = f"openai codex run --agent-file \"{agent_md_path.relative_to(project_root)}\" --input-file \"{idea_full_path}\" --context-dir ."
    print("\n--- For Codex CLI (OpenAI) ---")
    print(codex_command)

    print("="*80)
    print("\nAfter running one of the above commands, paste the AI's output below:")
    print("Press Ctrl+Z (Windows) or Ctrl+D (Unix) and then Enter to finish input.")
    print("="*80)

    ai_output = sys.stdin.read()

    # --- Save Processed Content ---
    output_filename = processed_path / f"{idea_name}.md"
    output_filename.write_text(ai_output.strip())
    print(f"\nProcessed idea saved to: {output_filename}")

    # Move original idea to processed_inbox
    shutil.move(str(idea_file), str(processed_inbox_path / idea_file.name))
    print(f"Original idea moved to: {processed_inbox_path / idea_file.name}")

if __name__ == "__main__":
    process_idea_orchestrator()