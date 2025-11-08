"""
Quinn - Voice Designer Agent
Defines narrative voice, tone, and style
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class QuinnAgent(BaseAgent):
    """
    Quinn - Voice Designer
    Specializes in:
    - Defining narrative POV and voice
    - Setting tone and atmosphere
    - Creating distinct character voices
    - Prose style recommendations
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="quinn", agent_type="creative", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Quinn's voice design task

        Args:
            context: Contains plot, characters, genre

        Returns:
            Dictionary with voice and tone guidelines
        """
        prompt = self.build_prompt(context)

        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += "Designa narrativ röst och ton för denna bok.\n\n"
        prompt += "Returnera JSON:\n\n"
        prompt += """
```json
{
  "narrativeVoice": {
    "pov": "First person / Third person limited / Third person omniscient",
    "tense": "Present / Past",
    "tone": "Mörk, melankolisk / Spännande, snabb / etc",
    "style": "Koncis noir / Detaljerad literary / etc",
    "proseGuidelines": [
      "Använd korta meningar för tempo",
      "Undvik adverb",
      "Visa, berätta inte"
    ]
  },
  "characterVoices": {
    "protagonist": "Hur protagonist tänker/pratar",
    "antagonist": "Distinkt från protagonist",
    "supporting": "Andra viktiga röster"
  },
  "atmosphereKeywords": ["mörk", "regn", "isolering", "etc"],
  "sampleOpening": "Första stycket skrivet i rätt röst som exempel"
}
```
"""

        raw_response = self.call_llm(prompt, max_tokens=3000)
        voice_design = self.extract_json(raw_response)

        return self.format_output(voice_design, output_type="json")
