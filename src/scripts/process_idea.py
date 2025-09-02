import os
import shutil
import pathlib

def process_idea():
    project_root = pathlib.Path(__file__).parent.parent.parent
    inbox_path = project_root / "ideas" / "inbox"
    processed_path = project_root / "ideas" / "processed"
    processed_inbox_path = project_root / "ideas" / "processed_inbox"
    strategy_path = project_root / "strategy"

    # Ensure processed directories exist
    processed_path.mkdir(parents=True, exist_ok=True)
    processed_inbox_path.mkdir(parents=True, exist_ok=True)

    # Read strategy files
    goals_content = (strategy_path / "01_goals.md").read_text()
    audience_content = (strategy_path / "02_audience.md").read_text()

    # Find the idea file (assuming only one for this example)
    idea_file = None
    for f in inbox_path.iterdir():
        if f.is_file() and f.name.endswith(".txt"):
            idea_file = f
            break

    if not idea_file:
        print("No idea file found in inbox.")
        return

    idea_content = idea_file.read_text()
    idea_name = idea_file.stem # Get name without extension

    # --- Simulate AI Processing ---
    # This is where the "genius" happens. In a real system, an AI would do this.
    # Here, we'll generate a structured output based on the input and strategy.

    processed_content = f"""# Processed Idea: {idea_name.replace('_', ' ').title()}

## Summary
This idea is about: "{idea_content.strip()}"

## Alignment with Goals
Based on our goals:
- {goals_content.strip().replace('# Goals', '').strip()}

## Target Audience
This idea is relevant to our audience:
- {audience_content.strip().replace('# Audience', '').strip()}

## Suggested Actions
- Research existing content on this topic.
- Outline key points for a video essay.
- Identify potential visual examples.
"""

    # Write processed content to a new file
    output_filename = processed_path / f"{idea_name}.md"
    output_filename.write_text(processed_content)
    print(f"Processed idea saved to: {output_filename}")

    # Move original idea to processed_inbox
    shutil.move(str(idea_file), str(processed_inbox_path / idea_file.name))
    print(f"Original idea moved to: {processed_inbox_path / idea_file.name}")

if __name__ == "__main__":
    process_idea()
