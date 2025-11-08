#!/usr/bin/env python3
"""
NOIR - AI-Powered Book Writing System
Main orchestration script

Usage:
    python3 run_noir.py --project my-book --brief plot-brief.json
    python3 run_noir.py --project my-book --chapter 1
    python3 run_noir.py --project my-book --status
"""

import sys
import argparse
import json
from pathlib import Path
from datetime import datetime

# Add agents to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.orchestrator import Orchestrator


def load_plot_brief(brief_file: Path) -> dict:
    """Load plot brief from JSON file"""
    if not brief_file.exists():
        print(f"❌ Brief file not found: {brief_file}")
        sys.exit(1)

    with open(brief_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def main():
    parser = argparse.ArgumentParser(
        description='NOIR - AI-Powered Book Writing System',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Start new book from plot brief
  python3 run_noir.py --project my-thriller --brief plot-brief.json

  # Run full pipeline (Phase 0-3)
  python3 run_noir.py --project my-thriller --brief plot-brief.json --full

  # Write specific chapter
  python3 run_noir.py --project my-thriller --chapter 1

  # Check project status
  python3 run_noir.py --project my-thriller --status

  # Use Claude API instead of mock
  python3 run_noir.py --project my-thriller --brief plot-brief.json --provider claude

  # Use OpenAI
  python3 run_noir.py --project my-thriller --brief plot-brief.json --provider openai
        """
    )

    parser.add_argument('--project', required=True,
                        help='Project name (will create books/<project-name>/)')

    parser.add_argument('--brief', type=str,
                        help='Path to plot brief JSON file')

    parser.add_argument('--chapter', type=int,
                        help='Write specific chapter number')

    parser.add_argument('--status', action='store_true',
                        help='Show project status')

    parser.add_argument('--full', action='store_true',
                        help='Run full pipeline (Phase 0-3 with demo chapter)')

    parser.add_argument('--provider', default='mock',
                        choices=['claude', 'openai', 'mock'],
                        help='LLM provider (default: mock for testing)')

    parser.add_argument('--api-key', type=str,
                        help='API key (or set ANTHROPIC_API_KEY / OPENAI_API_KEY env var)')

    args = parser.parse_args()

    # Initialize orchestrator
    print("\n" + "="*70)
    print("🎬 NOIR - AI-Powered Book Writing System")
    print("="*70)

    orchestrator = Orchestrator(
        project_name=args.project,
        llm_provider=args.provider,
        api_key=args.api_key
    )

    # Handle different commands
    if args.status:
        # Show status
        status = orchestrator.get_project_status()
        print("\n📊 PROJECT STATUS\n")
        print(f"Title: {status['title']}")
        print(f"Phase: {status['phase']}")
        print(f"Words: {status['totalWords']:,}")
        print(f"Chapters: {status['chaptersComplete']}/{status['totalChapters']}")
        if status['lastUpdated']:
            print(f"Last Updated: {status['lastUpdated']}")
        print()

    elif args.brief:
        # Load plot brief
        brief_file = Path(args.brief)
        plot_brief = load_plot_brief(brief_file)

        if args.full:
            # Run full pipeline
            print("\n🚀 Running FULL PIPELINE (Phase 0-3 with demo chapter)")
            print("This will:")
            print("  1. Generate plot structure (Harper)")
            print("  2. Create characters (Morgan)")
            print("  3. Design setting (River)")
            print("  4. Define voice (Quinn)")
            print("  5. Write Chapter 1 (Sage)")
            print("  6. Review Chapter 1 (Ellis)")
            print("\nStarting...\n")

            project_data = orchestrator.run_full_pipeline(plot_brief)

            print("\n✨ FULL PIPELINE COMPLETE!")
            print(f"\n📂 Open dashboard: books/{args.project}/dashboard.html")

        else:
            # Just run Phase 0
            print("\n📋 Running Phase 0: Narrative Validation")
            project_data = orchestrator.phase0_narrative_validation(plot_brief)

            print("\n✅ Phase 0 Complete!")
            print(f"\n📂 Open dashboard: books/{args.project}/dashboard.html")
            print("\n💡 Next steps:")
            print(f"  - Review the generated outline")
            print(f"  - To write chapters, run:")
            print(f"    python3 run_noir.py --project {args.project} --chapter 1")

    elif args.chapter:
        # Write specific chapter
        print(f"\n✍️ Writing Chapter {args.chapter}")

        # Load existing project
        project_data = orchestrator.updater.load_data()

        if not project_data.get('outline'):
            print("❌ Error: No outline found. Run Phase 0 first with --brief")
            sys.exit(1)

        # Write chapter
        project_data = orchestrator.phase1_write_chapter(project_data, args.chapter)

        # Review chapter
        project_data = orchestrator.phase3_quality_review(project_data, args.chapter)

        print(f"\n✅ Chapter {args.chapter} Complete!")
        print(f"\n📂 Open dashboard: books/{args.project}/dashboard.html")

    else:
        parser.print_help()
        print("\n❌ Error: Must specify --brief, --chapter, or --status")
        sys.exit(1)


if __name__ == "__main__":
    main()
