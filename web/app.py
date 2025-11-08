#!/usr/bin/env python3
"""
NOIR Flask Backend
Interaktiv backend för plot intake och feedback
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from pathlib import Path
import json
from datetime import datetime
import sys

# Add web directory to path for imports
sys.path.insert(0, str(Path(__file__).parent))
from update_dashboard import DashboardUpdater

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

BASE_DIR = Path(__file__).parent.parent

# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================

def get_updater(project_name):
    """Get DashboardUpdater instance"""
    return DashboardUpdater(project_name)

def get_project_data(project_name):
    """Load project data"""
    updater = get_updater(project_name)
    return updater.load_data()

def save_project_data(project_name, data):
    """Save project data"""
    updater = get_updater(project_name)
    updater.save_data(data)
    updater.generate_dashboard()

# ============================================================================
# PROJECT ENDPOINTS
# ============================================================================

@app.route('/api/projects', methods=['GET'])
def list_projects():
    """List all projects"""
    books_dir = BASE_DIR / "books"
    if not books_dir.exists():
        return jsonify({"projects": []})

    projects = [
        {
            "name": d.name,
            "path": str(d),
            "hasData": (d / "data.json").exists()
        }
        for d in books_dir.iterdir()
        if d.is_dir() and not d.name.startswith('.')
    ]

    return jsonify({"projects": projects})

@app.route('/api/projects/<project_name>', methods=['GET'])
def get_project(project_name):
    """Get project data"""
    try:
        data = get_project_data(project_name)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/projects/<project_name>', methods=['POST'])
def create_project(project_name):
    """Create new project"""
    try:
        updater = get_updater(project_name)

        # Create initial data
        data = {
            "title": request.json.get('title', project_name),
            "author": request.json.get('author', 'Author'),
            "currentPhase": "Fas 0: Plot Intake",
            "structure": "Ej vald",
            "targetWords": 80000,
            "totalWords": 0,
            "lastUpdated": datetime.now().isoformat(),
            "outline": None,
            "characters": [],
            "chapters": []
        }

        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": f"Project {project_name} created",
            "data": data
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================================
# PLOT INTAKE ENDPOINTS
# ============================================================================

@app.route('/api/projects/<project_name>/plot-brief', methods=['POST'])
def submit_plot_brief(project_name):
    """
    Submit simple plot brief and let AI agents generate detailed plot.
    This is the NEW simplified workflow!
    """
    try:
        brief_data = request.json

        # Create or load project
        updater = get_updater(project_name)
        try:
            data = get_project_data(project_name)
        except:
            # Project doesn't exist, create from template
            updater.create_from_template()
            data = get_project_data(project_name)

        # Store the original brief
        data['plotBrief'] = {
            **brief_data,
            "submittedDate": datetime.now().isoformat(),
            "status": "processing"
        }

        # Simulate AI Agent Processing
        # In production, this would call actual AI agents
        # For now, we generate structured mock data based on the brief

        plot_idea = brief_data.get('plotIdea', '')
        genre = brief_data.get('genre', '')

        # HARPER - Plot Architect generates structure
        data['agentWork'] = {
            "harper": {
                "status": "completed",
                "timestamp": datetime.now().isoformat(),
                "output": {
                    "logline": f"[HARPER GENERATED] Based on your {genre} idea - A compelling logline that captures the essence of your story...",
                    "hook": f"[HARPER GENERATED] An opening that immediately pulls readers in...",
                    "twist": f"[HARPER GENERATED] A shocking revelation that changes everything...",
                    "resolution": f"[HARPER GENERATED] How the story concludes and what it means...",
                    "threeActStructure": {
                        "act1": {
                            "description": "Setup - introduce world, characters, conflict",
                            "keyBeats": [
                                {"name": "Opening Image", "description": "..."},
                                {"name": "Inciting Incident", "description": "..."},
                                {"name": "First Plot Point", "description": "..."}
                            ]
                        },
                        "act2": {
                            "description": "Confrontation - escalating conflict",
                            "keyBeats": [
                                {"name": "Midpoint", "description": "..."},
                                {"name": "All Is Lost", "description": "..."}
                            ]
                        },
                        "act3": {
                            "description": "Resolution - climax and wrap-up",
                            "keyBeats": [
                                {"name": "Climax", "description": "..."},
                                {"name": "Resolution", "description": "..."}
                            ]
                        }
                    }
                }
            },
            "morgan": {
                "status": "completed",
                "timestamp": datetime.now().isoformat(),
                "output": {
                    "protagonist": {
                        "name": "[MORGAN GENERATED] Name based on genre/setting",
                        "age": 35,
                        "occupation": "[MORGAN GENERATED] Occupation",
                        "psychology": {
                            "ghost": "[MORGAN GENERATED] Past trauma that shapes them...",
                            "want": "[MORGAN GENERATED] What they consciously pursue...",
                            "need": "[MORGAN GENERATED] What they actually need to grow...",
                            "fear": "[MORGAN GENERATED] Deepest fear holding them back...",
                            "flaw": "[MORGAN GENERATED] Fatal flaw to overcome..."
                        },
                        "arc": {
                            "beginning": "[MORGAN GENERATED] Who they are at start...",
                            "middle": "[MORGAN GENERATED] How they change...",
                            "end": "[MORGAN GENERATED] Who they become..."
                        }
                    },
                    "antagonist": {
                        "name": "[MORGAN GENERATED] Antagonist name",
                        "motivation": "[MORGAN GENERATED] Why they do what they do (must be logical from their POV)...",
                        "connection": "[MORGAN GENERATED] How they relate to protagonist...",
                        "sympathy": "[MORGAN GENERATED] What makes them human/relatable..."
                    },
                    "supporting": [
                        {
                            "name": "[MORGAN GENERATED] Supporting character 1",
                            "role": "Ally/Mentor/etc",
                            "purpose": "Their role in protagonist's journey"
                        }
                    ]
                }
            },
            "river": {
                "status": "completed",
                "timestamp": datetime.now().isoformat(),
                "output": {
                    "primarySetting": {
                        "location": "[RIVER GENERATED] Specific location",
                        "atmosphere": "[RIVER GENERATED] Mood and feeling of place...",
                        "significance": "[RIVER GENERATED] Why this place matters to the story...",
                        "season": "Winter/Summer/etc",
                        "timespan": "How long the story takes"
                    },
                    "keyLocations": [
                        {
                            "name": "[RIVER GENERATED] Important location 1",
                            "description": "Details...",
                            "storyRole": "Why this place is important..."
                        }
                    ]
                }
            },
            "quinn": {
                "status": "completed",
                "timestamp": datetime.now().isoformat(),
                "output": {
                    "narrativeVoice": {
                        "pov": "First person / Third person limited / etc",
                        "tense": "Present / Past",
                        "tone": f"[QUINN GENERATED] Based on {genre} - dark/light/etc",
                        "style": "[QUINN GENERATED] Prose style recommendations..."
                    },
                    "characterVoices": {
                        "protagonist": "[QUINN GENERATED] How they speak/think...",
                        "antagonist": "[QUINN GENERATED] Distinct voice..."
                    }
                }
            }
        }

        # Update status
        data['currentPhase'] = "Agent Processing Complete - Awaiting Your Review"
        data['lastUpdated'] = datetime.now().isoformat()
        data['title'] = brief_data.get('title', f"Untitled {genre.capitalize()} Novel")
        data['genre'] = genre
        data['targetWords'] = brief_data.get('wordCount', 80000)

        # Save
        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": "Plot brief processed by AI agents",
            "project": project_name,
            "agentStatus": {
                "harper": "completed",
                "morgan": "completed",
                "river": "completed",
                "quinn": "completed"
            },
            "nextStep": f"/plot-review.html?project={project_name}"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/projects/<project_name>/plot-intake', methods=['POST'])
def submit_plot_intake(project_name):
    """Submit plot intake and generate outline"""
    try:
        plot_data = request.json

        # Load project data
        data = get_project_data(project_name)

        # Store plot intake
        data['plotIntake'] = {
            **plot_data,
            "submittedDate": datetime.now().isoformat(),
            "status": "submitted"
        }

        # Generate initial outline from plot
        data['outline'] = {
            "logline": plot_data.get('logline', ''),
            "hook": plot_data.get('hook', ''),
            "twist": plot_data.get('twist', ''),
            "resolution": plot_data.get('resolution', ''),
            "status": "draft",
            "generatedFrom": "plot-intake",
            "generatedDate": datetime.now().isoformat(),
            "acts": [
                {
                    "number": 1,
                    "title": "Akt I: Setup",
                    "description": plot_data.get('act1_description', ''),
                    "beats": [
                        {
                            "name": "Inciting Incident",
                            "description": plot_data.get('inciting_incident', ''),
                            "chapter": 1
                        },
                        {
                            "name": "First Plot Point",
                            "description": plot_data.get('first_plot_point', ''),
                            "chapter": 3
                        }
                    ]
                },
                {
                    "number": 2,
                    "title": "Akt II: Confrontation",
                    "description": plot_data.get('act2_description', ''),
                    "beats": [
                        {
                            "name": "Midpoint",
                            "description": plot_data.get('midpoint', ''),
                            "chapter": 6
                        },
                        {
                            "name": "All Is Lost",
                            "description": plot_data.get('all_is_lost', ''),
                            "chapter": 9
                        }
                    ]
                },
                {
                    "number": 3,
                    "title": "Akt III: Resolution",
                    "description": plot_data.get('act3_description', ''),
                    "beats": [
                        {
                            "name": "Climax",
                            "description": plot_data.get('climax', ''),
                            "chapter": 11
                        },
                        {
                            "name": "Resolution",
                            "description": plot_data.get('resolution', ''),
                            "chapter": 12
                        }
                    ]
                }
            ]
        }

        # Update phase
        data['currentPhase'] = "Fas 0: Narrative Validation - Awaiting Review"
        data['lastUpdated'] = datetime.now().isoformat()

        # Initialize characters from plot
        if plot_data.get('protagonist'):
            data['characters'].append({
                "name": plot_data['protagonist'].get('name', 'Protagonist'),
                "role": "Protagonist",
                "age": plot_data['protagonist'].get('age'),
                "occupation": plot_data['protagonist'].get('occupation'),
                "description": plot_data['protagonist'].get('description'),
                "arc": {
                    "start": plot_data['protagonist'].get('arc_start'),
                    "middle": plot_data['protagonist'].get('arc_middle'),
                    "end": plot_data['protagonist'].get('arc_end')
                },
                "ghost": plot_data['protagonist'].get('ghost'),
                "want": plot_data['protagonist'].get('want'),
                "need": plot_data['protagonist'].get('need')
            })

        if plot_data.get('antagonist'):
            data['characters'].append({
                "name": plot_data['antagonist'].get('name', 'Antagonist'),
                "role": "Antagonist",
                "age": plot_data['antagonist'].get('age'),
                "occupation": plot_data['antagonist'].get('occupation'),
                "description": plot_data['antagonist'].get('description'),
                "motivation": plot_data['antagonist'].get('motivation')
            })

        # Initialize chapters based on structure
        chapter_count = plot_data.get('chapter_count', 12)
        data['chapters'] = []
        for i in range(1, chapter_count + 1):
            data['chapters'].append({
                "number": i,
                "title": f"Kapitel {i}",
                "status": "pending",
                "words": 0,
                "quality": None,
                "versions": [],
                "metadata": {}
            })

        # Save
        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": "Plot intake submitted and outline generated",
            "outline": data['outline']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================================
# OUTLINE ENDPOINTS
# ============================================================================

@app.route('/api/projects/<project_name>/outline', methods=['GET'])
def get_outline(project_name):
    """Get outline"""
    try:
        data = get_project_data(project_name)
        return jsonify(data.get('outline', {}))
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/projects/<project_name>/outline/feedback', methods=['POST'])
def submit_outline_feedback(project_name):
    """Submit feedback on outline"""
    try:
        feedback = request.json
        data = get_project_data(project_name)

        if 'outline' not in data:
            return jsonify({"error": "No outline found"}), 404

        # Add feedback to outline
        data['outline']['feedback'] = feedback
        data['outline']['feedbackDate'] = datetime.now().isoformat()
        data['outline']['status'] = feedback['decision'].lower()

        # Update phase based on decision
        if feedback['decision'] == 'APPROVE':
            data['currentPhase'] = "Fas 1: Creative Planning"
            data['outline']['approved'] = True
            data['outline']['approvedDate'] = datetime.now().isoformat()
        elif feedback['decision'] == 'REVISE':
            data['currentPhase'] = "Fas 0: Narrative Validation - Revision Requested"
        elif feedback['decision'] == 'REJECT':
            data['currentPhase'] = "Fas 0: Narrative Validation - Rejected"

        data['lastUpdated'] = datetime.now().isoformat()

        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": f"Outline feedback submitted: {feedback['decision']}",
            "currentPhase": data['currentPhase']
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================================
# CHARACTER ENDPOINTS
# ============================================================================

@app.route('/api/projects/<project_name>/characters', methods=['GET'])
def get_characters(project_name):
    """Get all characters"""
    try:
        data = get_project_data(project_name)
        return jsonify(data.get('characters', []))
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/projects/<project_name>/characters/feedback', methods=['POST'])
def submit_characters_feedback(project_name):
    """Submit feedback on characters"""
    try:
        feedback = request.json
        data = get_project_data(project_name)

        # Store feedback
        data['charactersFeedback'] = feedback
        data['charactersFeedbackDate'] = datetime.now().isoformat()

        if feedback['decision'] == 'APPROVE':
            data['currentPhase'] = "Fas 2: Writing"

        data['lastUpdated'] = datetime.now().isoformat()
        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": "Characters feedback submitted"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================================
# CHAPTER ENDPOINTS
# ============================================================================

@app.route('/api/projects/<project_name>/chapters', methods=['GET'])
def get_chapters(project_name):
    """Get all chapters"""
    try:
        data = get_project_data(project_name)
        return jsonify(data.get('chapters', []))
    except Exception as e:
        return jsonify({"error": str(e)}), 404

@app.route('/api/projects/<project_name>/chapters/<int:chapter_num>', methods=['GET'])
def get_chapter(project_name, chapter_num):
    """Get specific chapter"""
    try:
        data = get_project_data(project_name)
        chapter = next((ch for ch in data.get('chapters', []) if ch['number'] == chapter_num), None)

        if not chapter:
            return jsonify({"error": f"Chapter {chapter_num} not found"}), 404

        return jsonify(chapter)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/projects/<project_name>/chapters/<int:chapter_num>/feedback', methods=['POST'])
def submit_chapter_feedback(project_name, chapter_num):
    """Submit feedback on chapter"""
    try:
        feedback = request.json
        data = get_project_data(project_name)

        # Find chapter
        chapter = next((ch for ch in data.get('chapters', []) if ch['number'] == chapter_num), None)

        if not chapter:
            return jsonify({"error": f"Chapter {chapter_num} not found"}), 404

        # Add feedback
        if 'feedback' not in chapter:
            chapter['feedback'] = []

        chapter['feedback'].append({
            **feedback,
            "submittedDate": datetime.now().isoformat()
        })

        chapter['feedbackStatus'] = feedback['decision'].lower()

        # Update status based on decision
        if feedback['decision'] == 'APPROVE':
            if feedback.get('version') == 'FINAL':
                chapter['status'] = 'completed'
            else:
                chapter['status'] = 'in-progress'

        data['lastUpdated'] = datetime.now().isoformat()
        save_project_data(project_name, data)

        return jsonify({
            "success": True,
            "message": f"Chapter {chapter_num} feedback submitted"
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# ============================================================================
# HEALTH CHECK
# ============================================================================

@app.route('/api/health', methods=['GET'])
def health():
    """Health check"""
    return jsonify({
        "status": "ok",
        "service": "NOIR Backend",
        "version": "1.0.0"
    })

# ============================================================================
# MAIN
# ============================================================================

if __name__ == '__main__':
    print("🚀 NOIR Backend Starting...")
    print("📡 API: http://localhost:5000")
    print("📚 Endpoints:")
    print("   GET  /api/projects")
    print("   POST /api/projects/<name>")
    print("   POST /api/projects/<name>/plot-intake")
    print("   POST /api/projects/<name>/outline/feedback")
    print("   POST /api/projects/<name>/chapters/<num>/feedback")
    print("")
    print("✅ Backend ready! Press Ctrl+C to stop.")

    app.run(debug=True, port=5000, host='0.0.0.0')
