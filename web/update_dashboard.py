#!/usr/bin/env python3
"""
NOIR Dashboard Updater
Uppdaterar web dashboard med bokprojektets data.
"""

import json
import os
import shutil
from datetime import datetime
from pathlib import Path

class DashboardUpdater:
    def __init__(self, project_name):
        self.project_name = project_name
        self.base_dir = Path(__file__).parent.parent
        self.project_dir = self.base_dir / "books" / project_name
        self.data_file = self.project_dir / "data.json"
        self.web_dir = self.base_dir / "web"

    def load_data(self):
        """Ladda projektdata från JSON-fil."""
        if not self.data_file.exists():
            print(f"⚠️ Ingen datafil hittades: {self.data_file}")
            print(f"Skapar ny från template...")
            self.create_from_template()

        with open(self.data_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def save_data(self, data):
        """Spara projektdata till JSON-fil."""
        self.project_dir.mkdir(parents=True, exist_ok=True)

        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

        print(f"✅ Data sparad: {self.data_file}")

    def create_from_template(self):
        """Skapa nytt projekt från template."""
        template_file = self.web_dir / "data-template.json"

        if not template_file.exists():
            raise FileNotFoundError(f"Template saknas: {template_file}")

        self.project_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(template_file, self.data_file)
        print(f"✅ Nytt projekt skapat: {self.project_name}")

    def generate_dashboard(self):
        """Generera dashboard HTML med projektdata."""
        # Data sparas redan i data.json via save_data()
        # Dashboard.html laddar den via fetch('data.json')

        # Kopiera dashboard template till projektmappen
        template_file = self.web_dir / "dashboard.html"
        output_file = self.project_dir / "dashboard.html"

        shutil.copy(template_file, output_file)

        print(f"✅ Dashboard genererad: {output_file}")
        print(f"📂 Öppna i webbläsare: file://{output_file.absolute()}")
        print(f"⚠️  OBS: Använd lokal webbserver för bästa resultat:")
        print(f"   cd {self.project_dir}")
        print(f"   python3 -m http.server 8000")
        print(f"   Öppna: http://localhost:8000/dashboard.html")

        return output_file

    def update_chapter(self, chapter_number, version_name, text, metadata=None):
        """Uppdatera ett kapitel med ny version."""
        data = self.load_data()

        # Hitta kapitel
        chapter = None
        for ch in data['chapters']:
            if ch['number'] == chapter_number:
                chapter = ch
                break

        if not chapter:
            print(f"⚠️ Kapitel {chapter_number} finns inte. Skapar nytt...")
            chapter = {
                "number": chapter_number,
                "title": f"Kapitel {chapter_number}",
                "status": "pending",
                "words": 0,
                "quality": None,
                "tension": None,
                "lastUpdated": None,
                "synopsis": "",
                "versions": [],
                "metadata": {}
            }
            data['chapters'].append(chapter)
            data['chapters'].sort(key=lambda x: x['number'])

        # Räkna ord
        word_count = len(text.split())

        # Lägg till ny version
        new_version = {
            "name": version_name,
            "date": datetime.now().isoformat(),
            "author": metadata.get('author', 'Unknown') if metadata else 'Unknown',
            "quality": metadata.get('quality') if metadata else None,
            "text": text
        }

        chapter['versions'].append(new_version)
        chapter['words'] = word_count
        chapter['lastUpdated'] = datetime.now().isoformat()

        # Uppdatera status
        if version_name == "FINAL":
            chapter['status'] = "completed"
            if metadata and 'quality' in metadata:
                chapter['quality'] = metadata['quality']
        elif version_name.startswith("Draft"):
            chapter['status'] = "in-progress"

        # Uppdatera metadata
        if metadata:
            chapter['metadata'].update(metadata)

        # Uppdatera totalt ordantal
        data['totalWords'] = sum(ch['words'] for ch in data['chapters'])
        data['lastUpdated'] = datetime.now().isoformat()

        # Spara
        self.save_data(data)

        # Regenerera dashboard
        self.generate_dashboard()

        print(f"✅ Kapitel {chapter_number} uppdaterat: {version_name} ({word_count} ord)")

    def update_outline(self, outline_data):
        """Uppdatera bokens outline."""
        data = self.load_data()
        data['outline'] = outline_data
        data['lastUpdated'] = datetime.now().isoformat()

        self.save_data(data)
        self.generate_dashboard()

        print("✅ Outline uppdaterad")

    def update_characters(self, characters):
        """Uppdatera karaktärslista."""
        data = self.load_data()
        data['characters'] = characters
        data['lastUpdated'] = datetime.now().isoformat()

        self.save_data(data)
        self.generate_dashboard()

        print(f"✅ {len(characters)} karaktärer uppdaterade")

    def set_phase(self, phase_name):
        """Sätt aktuell fas."""
        data = self.load_data()
        data['currentPhase'] = phase_name
        data['lastUpdated'] = datetime.now().isoformat()

        self.save_data(data)
        self.generate_dashboard()

        print(f"✅ Fas uppdaterad: {phase_name}")

    def list_projects(self):
        """Lista alla bokprojekt."""
        books_dir = self.base_dir / "books"
        if not books_dir.exists():
            print("Inga projekt ännu.")
            return []

        projects = [d.name for d in books_dir.iterdir() if d.is_dir()]
        return projects


def main():
    import sys

    if len(sys.argv) < 2:
        print("📚 NOIR Dashboard Updater")
        print("\nAnvändning:")
        print("  python update_dashboard.py <projekt-namn> [command] [args]")
        print("\nKommandon:")
        print("  generate              - Generera dashboard från data")
        print("  list                  - Lista alla projekt")
        print("  init                  - Skapa nytt projekt från template")
        print("\nExempel:")
        print("  python update_dashboard.py mitt-projekt generate")
        print("  python update_dashboard.py mitt-projekt init")
        sys.exit(1)

    if sys.argv[1] == "list":
        updater = DashboardUpdater("temp")
        projects = updater.list_projects()
        print(f"\n📚 Bokprojekt ({len(projects)}):")
        for p in projects:
            print(f"  - {p}")
        sys.exit(0)

    project_name = sys.argv[1]
    updater = DashboardUpdater(project_name)

    command = sys.argv[2] if len(sys.argv) > 2 else "generate"

    if command == "generate":
        output = updater.generate_dashboard()
        print(f"\n🎉 Klart! Öppna dashboard:")
        print(f"   file://{output.absolute()}")

    elif command == "init":
        updater.create_from_template()
        updater.generate_dashboard()
        print(f"\n🎉 Nytt projekt skapat: {project_name}")

    else:
        print(f"❌ Okänt kommando: {command}")
        sys.exit(1)


if __name__ == "__main__":
    main()
