
import argparse
import pathlib
import sys

def main():
    """
    Constructs a command to run a playbook with a context-aware AI tool.
    """
    parser = argparse.ArgumentParser(description="Launcher for AI playbooks.")
    parser.add_argument("playbook_name", help="The name of the playbook to run (without .txt extension).")
    args = parser.parse_args()

    project_root = pathlib.Path(__file__).parent.parent.parent
    playbook_file = project_root / "playbooks" / f"{args.playbook_name}.txt"

    if not playbook_file.exists():
        print(f"Error: Playbook '{args.playbook_name}.txt' not found in '{project_root / 'playbooks'}'", file=sys.stderr)
        sys.exit(1)

    playbook_content = playbook_file.read_text()

    # This is a hypothetical command structure.
    # The user should replace 'ai_agent' with their actual command-line tool.
    # --project_dir tells the agent the root context.
    # --prompt passes the playbook instructions.
    command = f"ai_agent --project_dir \"{project_root}\" --prompt \"{playbook_content}\""

    print("="*80)
    print("COPY AND RUN THE FOLLOWING COMMAND IN YOUR TERMINAL:")
    print("="*80)
    print(command)
    print("="*80)
    print("\nNOTE: Replace 'ai_agent' with your actual AI tool's command.")


if __name__ == "__main__":
    main()
