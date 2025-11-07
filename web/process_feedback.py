#!/usr/bin/env python3
"""
NOIR Feedback Processor
Processar feedback från författare och uppdaterar dashboard
"""

import json
import sys
from pathlib import Path
from datetime import datetime
from update_dashboard import DashboardUpdater

def process_outline_feedback(project_name, feedback_file):
    """Process feedback on outline"""
    print(f"📝 Processar outline feedback för: {project_name}")
    
    with open(feedback_file, 'r', encoding='utf-8') as f:
        feedback = json.load(f)
    
    updater = DashboardUpdater(project_name)
    data = updater.load_data()
    
    # Update outline with feedback
    if 'outline' not in data:
        data['outline'] = {}
    
    data['outline']['feedback'] = feedback
    data['outline']['status'] = feedback['decision'].lower()
    data['outline']['lastReviewed'] = feedback['date']
    data['outline']['score'] = feedback['overallScore']
    
    # Update phase based on decision
    if feedback['decision'] == 'GO':
        data['currentPhase'] = "Fas 1: Creative Planning - Godkänd att fortsätta"
        print("\n✅ OUTLINE GODKÄND! Moving to Fas 1...")
    elif feedback['decision'] == 'REVISE':
        data['currentPhase'] = "Fas 0: Narrative Validation - Revision begärd"
        print("\n🟡 REVISION BEGÄRD. Harper kommer revidera outline...")
    elif feedback['decision'] == 'NO-GO':
        data['currentPhase'] = "Fas 0: Narrative Validation - NO-GO, behöver ny approach"
        print("\n🔴 NO-GO. Outline fungerar inte. Fundera på ny story approach...")
    
    updater.save_data(data)
    updater.generate_dashboard()
    
    print(f"\n📊 FEEDBACK SAMMANFATTNING:")
    print(f"   Decision: {feedback['decision']}")
    print(f"   Overall Score: {feedback['overallScore']}/10")
    print(f"   Changes Requested: {sum(1 for c in feedback['comments'].values() if c.get('changeRequested', False))}")
    print(f"\n💡 Nästa steg: {feedback.get('nextSteps', 'Se dashboard för status')}")

def process_chapter_feedback(project_name, chapter_num, feedback_file):
    """Process feedback on chapter"""
    print(f"📝 Processar kapitel {chapter_num} feedback för: {project_name}")
    
    with open(feedback_file, 'r', encoding='utf-8') as f:
        feedback = json.load(f)
    
    updater = DashboardUpdater(project_name)
    data = updater.load_data()
    
    # Find chapter
    chapter = None
    for ch in data['chapters']:
        if ch['number'] == chapter_num:
            chapter = ch
            break
    
    if not chapter:
        print(f"❌ Kapitel {chapter_num} finns inte!")
        return
    
    # Add feedback to chapter
    if 'feedback' not in chapter:
        chapter['feedback'] = []
    
    chapter['feedback'].append(feedback)
    chapter['feedbackStatus'] = feedback['decision'].lower()
    chapter['lastReviewedDate'] = feedback['date']
    
    # Update chapter status based on decision
    if feedback['decision'] == 'APPROVE':
        if feedback['version'] == 'FINAL':
            chapter['status'] = 'completed'
            print(f"\n✅ KAPITEL {chapter_num} GODKÄNT OCH KLART!")
        else:
            chapter['status'] = 'in-progress'
            print(f"\n✅ {feedback['version']} GODKÄND! Moving to QA...")
    elif feedback['decision'] in ['REVISE', 'APPROVE_FOR_QA']:
        chapter['status'] = 'in-progress'
        print(f"\n🟡 REVISION/QA BEGÄRD för Kapitel {chapter_num}")
    
    updater.save_data(data)
    updater.generate_dashboard()
    
    print(f"\n📊 FEEDBACK SAMMANFATTNING:")
    print(f"   Version: {feedback['version']}")
    print(f"   Decision: {feedback['decision']}")
    print(f"   Overall Score: {feedback['overallScore']}/10")
    print(f"   Must Fix: {len(feedback.get('mustFix', []))}")
    print(f"   Nice to Have: {len(feedback.get('niceToHave', []))}")
    print(f"\n💡 Nästa steg: {feedback.get('nextSteps', 'Se dashboard för status')}")

def main():
    if len(sys.argv) < 3:
        print("📚 NOIR Feedback Processor")
        print("\nAnvändning:")
        print("  python3 process_feedback.py <projekt> outline")
        print("  python3 process_feedback.py <projekt> chapter <nummer>")
        print("\nExempel:")
        print("  python3 process_feedback.py min-thriller outline")
        print("  python3 process_feedback.py min-thriller chapter 1")
        print("\nFeedback filer:")
        print("  books/<projekt>/feedback-outline.json")
        print("  books/<projekt>/feedback-chapter-1.json")
        sys.exit(1)
    
    project_name = sys.argv[1]
    feedback_type = sys.argv[2]
    base_dir = Path(__file__).parent.parent
    
    if feedback_type == 'outline':
        feedback_file = base_dir / "books" / project_name / "feedback-outline.json"
        if not feedback_file.exists():
            print(f"❌ Ingen outline feedback hittades: {feedback_file}")
            print(f"\nSkapa den först:")
            print(f"  cp templates/feedback/feedback-outline-template.json books/{project_name}/feedback-outline.json")
            print(f"  # Fyll i feedback")
            print(f"  python3 web/process_feedback.py {project_name} outline")
            sys.exit(1)
        
        process_outline_feedback(project_name, feedback_file)
    
    elif feedback_type == 'chapter':
        if len(sys.argv) < 4:
            print("❌ Kapitelnummer saknas!")
            print("  python3 process_feedback.py <projekt> chapter <nummer>")
            sys.exit(1)
        
        chapter_num = int(sys.argv[3])
        feedback_file = base_dir / "books" / project_name / f"feedback-chapter-{chapter_num}.json"
        
        if not feedback_file.exists():
            print(f"❌ Ingen chapter feedback hittades: {feedback_file}")
            print(f"\nSkapa den först:")
            print(f"  cp templates/feedback/feedback-chapter-template.json books/{project_name}/feedback-chapter-{chapter_num}.json")
            print(f"  # Fyll i feedback")
            print(f"  python3 web/process_feedback.py {project_name} chapter {chapter_num}")
            sys.exit(1)
        
        process_chapter_feedback(project_name, chapter_num, feedback_file)
    
    else:
        print(f"❌ Okänd feedback-typ: {feedback_type}")
        print("  Använd: outline eller chapter")
        sys.exit(1)

if __name__ == "__main__":
    main()
