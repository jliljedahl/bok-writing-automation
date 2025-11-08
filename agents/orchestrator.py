"""
Orchestrator - Coordinates all NOIR agents
"""

from typing import Dict, Any, List, Optional
from pathlib import Path
import json
from datetime import datetime
import sys

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.llm_client import LLMClient
from agents.creative.harper_agent import HarperAgent
from agents.creative.morgan_agent import MorganAgent
from agents.creative.quinn_agent import QuinnAgent
from agents.creative.river_agent import RiverAgent
from agents.writing.sage_agent import SageAgent
from agents.quality.ellis_agent import EllisAgent
from web.update_dashboard import DashboardUpdater


class Orchestrator:
    """
    Orchestrates the entire book writing process.
    Coordinates all agents through different phases.
    """

    def __init__(self, project_name: str, llm_provider: str = "mock", api_key: Optional[str] = None):
        """
        Initialize orchestrator

        Args:
            project_name: Name of the book project
            llm_provider: 'claude', 'openai', or 'mock'
            api_key: API key for LLM provider (optional, reads from env)
        """
        self.project_name = project_name
        self.updater = DashboardUpdater(project_name)

        # Initialize LLM client
        self.llm_client = LLMClient(provider=llm_provider, api_key=api_key)

        # Initialize agents
        self._init_agents()

        print(f"\n🎬 NOIR Orchestrator initialized for: {project_name}")
        print(f"🤖 LLM Provider: {llm_provider}")
        print(f"👥 Agents loaded: {len(self.agents)}")

    def _init_agents(self):
        """Initialize all agents"""
        self.agents = {
            # Creative Team
            'harper': HarperAgent(self.llm_client),
            'morgan': MorganAgent(self.llm_client),
            'quinn': QuinnAgent(self.llm_client),
            'river': RiverAgent(self.llm_client),

            # Writing Team
            'sage': SageAgent(self.llm_client),

            # Quality Team
            'ellis': EllisAgent(self.llm_client),
        }

    def run_full_pipeline(self, plot_brief: Dict[str, Any]) -> Dict[str, Any]:
        """
        Run complete book writing pipeline

        Args:
            plot_brief: User's plot brief with genre, plotIdea, etc.

        Returns:
            Complete project data with all phases
        """
        print("\n" + "="*60)
        print("🚀 STARTING FULL NOIR PIPELINE")
        print("="*60)

        # Phase 0: Narrative Validation (Creative Planning)
        print("\n📋 PHASE 0: Narrative Validation")
        project_data = self.phase0_narrative_validation(plot_brief)

        # Phase 1: Write first chapter (demo - full book would iterate all chapters)
        print("\n✍️ PHASE 1-2: Writing (Chapter 1 as demo)")
        project_data = self.phase1_write_chapter(project_data, chapter_num=1)

        # Phase 3: Quality Review
        print("\n🔍 PHASE 3: Quality Review (Chapter 1)")
        project_data = self.phase3_quality_review(project_data, chapter_num=1)

        print("\n" + "="*60)
        print("✅ PIPELINE COMPLETE!")
        print("="*60)

        return project_data

    def phase0_narrative_validation(self, plot_brief: Dict[str, Any]) -> Dict[str, Any]:
        """
        Phase 0: Creative team develops plot from brief

        Args:
            plot_brief: User's raw plot idea

        Returns:
            Project data with generated outline, characters, setting, voice
        """
        # Load or create project
        try:
            data = self.updater.load_data()
        except:
            self.updater.create_from_template()
            data = self.updater.load_data()

        # Store original brief
        data['plotBrief'] = plot_brief
        data['currentPhase'] = "Phase 0: Narrative Validation - In Progress"

        # Context for agents
        context = {
            'plotBrief': plot_brief.get('plotIdea', ''),
            'genre': plot_brief.get('genre', ''),
            'targetAudience': plot_brief.get('targetAudience'),
            'wordCount': plot_brief.get('wordCount', 80000)
        }

        # Step 1: Harper creates plot structure
        print("\n  🎬 Harper (Plot Architect) working...")
        harper_output = self.agents['harper'].execute(context)
        data['agentWork'] = {'harper': harper_output}

        # Update context with Harper's work
        context['outline'] = harper_output.get('output', {})

        # Step 2: Morgan creates characters
        print("  🧠 Morgan (Character Psychologist) working...")
        morgan_output = self.agents['morgan'].execute(context)
        data['agentWork']['morgan'] = morgan_output

        # Update context with Morgan's work
        context['characters'] = morgan_output.get('output', {})

        # Step 3: River creates setting
        print("  🌍 River (World Builder) working...")
        river_output = self.agents['river'].execute(context)
        data['agentWork']['river'] = river_output

        # Step 4: Quinn defines voice
        print("  🎭 Quinn (Voice Designer) working...")
        quinn_output = self.agents['quinn'].execute(context)
        data['agentWork']['quinn'] = quinn_output

        # Store structured output in main project data
        if 'output' in harper_output:
            data['outline'] = harper_output['output']

        if 'output' in morgan_output:
            data['characters'] = morgan_output['output'].get('all_characters', [])

        # Update phase
        data['currentPhase'] = "Phase 0: Complete - Awaiting Approval"
        data['lastUpdated'] = datetime.now().isoformat()
        data['title'] = plot_brief.get('title', f"Untitled {context['genre']} Novel")
        data['genre'] = context['genre']

        # Save
        self.updater.save_data(data)
        self.updater.generate_dashboard()

        print("  ✅ Phase 0 complete!")

        return data

    def phase1_write_chapter(self, project_data: Dict[str, Any], chapter_num: int) -> Dict[str, Any]:
        """
        Phase 1-2: Write a chapter

        Args:
            project_data: Current project data
            chapter_num: Which chapter to write

        Returns:
            Updated project data with chapter
        """
        # Build context for Sage
        context = {
            'chapterNumber': chapter_num,
            'outline': project_data.get('outline', {}),
            'characters': project_data.get('characters', []),
            'genre': project_data.get('genre', ''),
            'previousChapters': [ch for ch in project_data.get('chapters', []) if ch['number'] < chapter_num]
        }

        # Sage writes the chapter
        print(f"\n  ✍️ Sage writing Chapter {chapter_num}...")
        sage_output = self.agents['sage'].execute(context)

        # Update project data
        chapters = project_data.get('chapters', [])

        # Find or create chapter entry
        chapter_entry = None
        for ch in chapters:
            if ch['number'] == chapter_num:
                chapter_entry = ch
                break

        if not chapter_entry:
            chapter_entry = {
                'number': chapter_num,
                'title': f"Chapter {chapter_num}",
                'status': 'draft',
                'versions': [],
                'words': 0,
                'quality': None
            }
            chapters.append(chapter_entry)
            chapters.sort(key=lambda x: x['number'])

        # Add version
        chapter_text = sage_output.get('output', {}).get('text', '')
        word_count = len(chapter_text.split())

        chapter_entry['versions'].append({
            'name': 'Draft v1',
            'date': datetime.now().isoformat(),
            'author': 'Sage',
            'text': chapter_text,
            'wordCount': word_count
        })

        chapter_entry['words'] = word_count
        chapter_entry['title'] = sage_output.get('output', {}).get('title', f"Chapter {chapter_num}")
        chapter_entry['status'] = 'in-review'
        chapter_entry['lastUpdated'] = datetime.now().isoformat()

        project_data['chapters'] = chapters
        project_data['totalWords'] = sum(ch['words'] for ch in chapters)
        project_data['currentPhase'] = f"Phase 2: Writing - Chapter {chapter_num} complete"

        # Save
        self.updater.save_data(project_data)
        self.updater.generate_dashboard()

        print(f"  ✅ Chapter {chapter_num} written! ({word_count} words)")

        return project_data

    def phase3_quality_review(self, project_data: Dict[str, Any], chapter_num: int) -> Dict[str, Any]:
        """
        Phase 3: Quality review of chapter

        Args:
            project_data: Current project data
            chapter_num: Which chapter to review

        Returns:
            Updated project data with review
        """
        # Find chapter
        chapter = None
        for ch in project_data.get('chapters', []):
            if ch['number'] == chapter_num:
                chapter = ch
                break

        if not chapter or not chapter.get('versions'):
            print(f"  ⚠️ No chapter {chapter_num} to review")
            return project_data

        # Get latest version
        latest_version = chapter['versions'][-1]

        # Build context
        context = {
            'chapterNumber': chapter_num,
            'chapterText': latest_version.get('text', ''),
            'title': chapter.get('title', ''),
            'outline': project_data.get('outline', {}),
            'characters': project_data.get('characters', [])
        }

        # Ellis reviews
        print(f"\n  🔍 Ellis reviewing Chapter {chapter_num}...")
        ellis_output = self.agents['ellis'].execute(context)

        # Store review
        review = ellis_output.get('output', {})
        chapter['qualityReview'] = review
        chapter['quality'] = review.get('overallScore', 0)

        verdict = review.get('verdict', 'NEEDS_REVISION')
        if verdict == 'APPROVE' or verdict == 'APPROVE_WITH_MINOR_REVISIONS':
            chapter['status'] = 'completed'
            print(f"  ✅ Chapter {chapter_num} APPROVED (score: {chapter['quality']}/10)")
        else:
            chapter['status'] = 'needs-revision'
            print(f"  🔄 Chapter {chapter_num} needs revision (score: {chapter['quality']}/10)")

        project_data['currentPhase'] = f"Phase 3: QA - Chapter {chapter_num} reviewed"

        # Save
        self.updater.save_data(project_data)
        self.updater.generate_dashboard()

        return project_data

    def get_project_status(self) -> Dict[str, Any]:
        """Get current project status"""
        data = self.updater.load_data()
        return {
            'title': data.get('title', 'Untitled'),
            'phase': data.get('currentPhase', 'Not started'),
            'totalWords': data.get('totalWords', 0),
            'chaptersComplete': len([ch for ch in data.get('chapters', []) if ch.get('status') == 'completed']),
            'totalChapters': len(data.get('chapters', [])),
            'lastUpdated': data.get('lastUpdated')
        }
