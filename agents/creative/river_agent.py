"""
River - World Builder Agent
Creates setting, atmosphere, and sense of place
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class RiverAgent(BaseAgent):
    """
    River - World Builder
    Specializes in:
    - Creating vivid, atmospheric settings
    - Researching locations and making them authentic
    - Building sense of place
    - Integrating setting into plot
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="river", agent_type="creative", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute River's world-building task

        Args:
            context: Contains plot and characters

        Returns:
            Dictionary with setting details
        """
        prompt = self.build_prompt(context)

        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += "Skapa detaljerad setting och atmosfär.\n\n"
        prompt += "Returnera JSON:\n\n"
        prompt += """
```json
{
  "primarySetting": {
    "location": "Specifik plats (stad, bygd, etc)",
    "atmosphere": "Känslan av platsen",
    "significance": "Varför är denna plats viktig för storyn?",
    "season": "Vinter/Sommar/Höst/Vår",
    "timespan": "Hur lång tid täcker berättelsen?",
    "weather": "Typiskt väder som förstärker ton"
  },
  "keyLocations": [
    {
      "name": "Platsens namn",
      "description": "Sensorisk beskrivning",
      "storyRole": "Varför viktigt för plot?",
      "atmosphere": "Mood"
    }
  ],
  "culturalContext": {
    "socialNorms": "Hur folk beter sig här",
    "localColor": "Dialekt, traditioner, detaljer",
    "timePerio": "Modern/Historisk/Tidlös"
  },
  "sensoryPalette": {
    "visual": ["Dominerande färger och ljus"],
    "sounds": ["Typiska ljud"],
    "smells": ["Dofter som definierar platsen"],
    "textures": ["Känsel och material"]
  }
}
```

Viktigt:
- Gör platsen till en KARAKTÄR, inte bara bakgrund
- Använd sensoriska detaljer
- Koppla setting till tema och ton
"""

        raw_response = self.call_llm(prompt, max_tokens=3000)
        setting = self.extract_json(raw_response)

        return self.format_output(setting, output_type="json")
