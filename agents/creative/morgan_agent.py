"""
Morgan - Character Psychologist Agent
Creates deep, psychologically realistic characters
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class MorganAgent(BaseAgent):
    """
    Morgan - Character Psychologist
    Specializes in:
    - Creating protagonist with ghost, want, need, fear, flaw
    - Designing character arcs
    - Crafting antagonist with believable motivation
    - Ensuring character consistency
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="morgan", agent_type="creative", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Morgan's character creation task

        Args:
            context: Must contain 'plotBrief' and ideally 'outline'

        Returns:
            Dictionary with character profiles
        """
        # Build prompt
        prompt = self.build_prompt(context)

        # Add specific instructions
        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += "Baserat på plot brief och outline, skapa djupa karaktärsprofiler.\n\n"
        prompt += "Returnera JSON med följande struktur:\n\n"
        prompt += """
```json
{
  "protagonist": {
    "name": "För- och efternamn",
    "age": 35,
    "occupation": "Yrke som är relevant för storyn",
    "psychology": {
      "ghost": "Trauma från förr som formar dem idag",
      "want": "Vad de medvetet strävar efter (ofta fel sak)",
      "need": "Vad de verkligen behöver för att växa (ofta motsats till want)",
      "fear": "Djupaste rädsla som håller dem tillbaka",
      "flaw": "Fatal flaw de måste övervinna"
    },
    "arc": {
      "beginning": "Vem de är i början",
      "middle": "Hur de förändras",
      "end": "Vem de blir"
    },
    "voice": {
      "mannerisms": "Sätt att prata/tänka",
      "vocabulary": "Ordval och uttryck",
      "internalDialogue": "Hur deras tankar låter"
    }
  },
  "antagonist": {
    "name": "Namn",
    "motivation": "Varför gör de detta? MÅSTE vara logiskt från deras perspektiv",
    "connection": "Hur relaterar de till protagonist?",
    "sympathy": "Vad gör dem sympatiska/mänskliga?",
    "methods": "Hur jobbar de för att nå sitt mål?"
  },
  "supporting": [
    {
      "name": "Namn",
      "role": "Ally/Mentor/Love Interest/etc",
      "purpose": "Varför finns de i storyn?",
      "relationship": "Relation till protagonist"
    }
  ],
  "all_characters": [
    {
      "name": "Alla karaktärer i list-format för dashboard",
      "role": "Protagonist/Antagonist/Supporting",
      "description": "Kort sammanfattning"
    }
  ]
}
```

KRITISKT VIKTIGT:
- Ghost måste vara SPECIFIKT, inte generiskt ("förälder dog" - FEL, "Såg sin far bli mördad när hon var 8" - RÄTT)
- Want vs Need måste vara i konflikt (det skapar character arc)
- Antagonist MÅSTE ha logisk motivation från DERAS perspektiv
- Alla karaktärer ska kännas som riktiga människor, inte arketyper
"""

        # Call LLM
        raw_response = self.call_llm(prompt, max_tokens=4000)

        # Parse JSON
        characters = self.extract_json(raw_response)

        # Format output
        return self.format_output(characters, output_type="json")
