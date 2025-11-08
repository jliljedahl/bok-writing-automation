"""
Harper - Plot Architect Agent
Creates plot structure, outline, and story beats
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class HarperAgent(BaseAgent):
    """
    Harper - Plot Architect
    Specializes in:
    - Creating compelling loglines
    - Designing plot structure (three-act, Save the Cat, etc.)
    - Crafting twists and hooks
    - Planning story beats and pacing
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="harper", agent_type="creative", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Harper's plot architecture task

        Args:
            context: Must contain 'plotBrief' with user's raw idea

        Returns:
            Dictionary with structured plot outline
        """
        # Build prompt from template + context
        prompt = self.build_prompt(context)

        # Add specific instructions for Harper
        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += "Baserat på författarens plot brief, skapa en komplett plot-struktur.\n\n"
        prompt += "Returnera ditt svar som JSON med följande struktur:\n\n"
        prompt += """
```json
{
  "logline": "En mening som fångar hela berättelsen",
  "hook": "Öppningsscenen som drar in läsaren direkt",
  "twist": "Den stora vändningen som förändrar allt",
  "resolution": "Hur berättelsen löses upp",
  "threeActStructure": {
    "act1": {
      "description": "Setup - introducera värld och konflikt",
      "keyBeats": [
        {"name": "Opening Image", "description": "...", "chapter": 1},
        {"name": "Inciting Incident", "description": "...", "chapter": 2},
        {"name": "First Plot Point", "description": "...", "chapter": 3}
      ]
    },
    "act2": {
      "description": "Confrontation - eskalera konflikt",
      "keyBeats": [
        {"name": "Midpoint", "description": "...", "chapter": 6},
        {"name": "All Is Lost", "description": "...", "chapter": 9}
      ]
    },
    "act3": {
      "description": "Resolution - klimax och upplösning",
      "keyBeats": [
        {"name": "Climax", "description": "...", "chapter": 11},
        {"name": "Resolution", "description": "...", "chapter": 12}
      ]
    }
  }
}
```

Viktigt:
- Logline ska vara koncis men fånga hela berättelsen
- Hook måste vara OMEDELBART engagerande
- Twist måste vara både överraskande OCH logisk i efterhand
- Alla beats ska ha konkreta beskrivningar, inte bara titlar
"""

        # Call LLM
        raw_response = self.call_llm(prompt, max_tokens=4000)

        # Parse JSON response
        plot_structure = self.extract_json(raw_response)

        # Format output
        return self.format_output(plot_structure, output_type="json")
