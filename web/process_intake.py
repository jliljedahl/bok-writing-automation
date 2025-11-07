#!/usr/bin/env python3
"""
NOIR Plot Intake Processor
Tar emot plot-intake och genererar initial outline
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from update_dashboard import DashboardUpdater

def process_plot_intake(project_name, intake_file):
    """
    Process plot intake file and generate initial structure
    """
    print(f"📝 Processar plot intake för: {project_name}")
    print(f"📂 Läser från: {intake_file}")

    # Read intake file
    with open(intake_file, 'r', encoding='utf-8') as f:
        intake_content = f.read()

    # Initialize project
    updater = DashboardUpdater(project_name)
    data = updater.load_data()

    # Parse intake (simplified - in real use, AI agents would do this)
    print("\n🎯 Genererar initial struktur...")

    # Update basic info
    data['currentPhase'] = "Fas 0: Narrative Validation - Väntar på godkännande"
    data['lastUpdated'] = datetime.now().isoformat()

    # Create initial outline placeholder
    data['outline'] = {
        "logline": "[GENERERAS: Harper analyserar din plot]",
        "hook": "[GENERERAS: Harper skapar hook från din inciting incident]",
        "twist": "[GENERERAS: Harper utvecklar din twist]",
        "resolution": "[GENERERAS: Harper designar resolution]",
        "status": "draft",
        "approvedBy": None,
        "acts": [
            {
                "number": 1,
                "title": "Akt I: Setup",
                "description": "[GENERERAS från din plot intake]",
                "beats": []
            },
            {
                "number": 2,
                "title": "Akt II: Confrontation",
                "description": "[GENERERAS från din plot intake]",
                "beats": []
            },
            {
                "number": 3,
                "title": "Akt III: Resolution",
                "description": "[GENERERAS från din plot intake]",
                "beats": []
            }
        ]
    }

    # Save plot intake reference
    data['plotIntake'] = {
        "file": str(intake_file),
        "processedDate": datetime.now().isoformat(),
        "status": "processed"
    }

    updater.save_data(data)
    updater.generate_dashboard()

    print("\n✅ Plot intake processad!")
    print(f"\n📋 NÄSTA STEG:")
    print(f"1. Öppna dashboard: books/{project_name}/dashboard.html")
    print(f"2. Granska den genererade outlin (när Harper är klar)")
    print(f"3. Ge feedback via feedback.json")
    print(f"4. Godkänn eller begär revision")
    print(f"\n💡 För att simulera agent-arbete, kör:")
    print(f"   python3 web/simulate_agents.py {project_name}")

def main():
    if len(sys.argv) < 2:
        print("📚 NOIR Plot Intake Processor")
        print("\nAnvändning:")
        print("  python3 process_intake.py <projekt-namn>")
        print("\nProjektet måste ha:")
        print("  books/<projekt-namn>/plot-intake.md")
        print("\nExempel:")
        print("  python3 process_intake.py min-thriller")
        sys.exit(1)

    project_name = sys.argv[1]
    base_dir = Path(__file__).parent.parent
    intake_file = base_dir / "books" / project_name / "plot-intake.md"

    if not intake_file.exists():
        print(f"❌ Fel: Ingen plot intake hittades:")
        print(f"   {intake_file}")
        print(f"\nSkapa den först:")
        print(f"  cp templates/plot-intake.md books/{project_name}/")
        print(f"  # Fyll i plot-intake.md")
        print(f"  python3 web/process_intake.py {project_name}")
        sys.exit(1)

    process_plot_intake(project_name, intake_file)

if __name__ == "__main__":
    main()
