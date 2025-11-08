"""
Sage - Lead Writer Agent
Writes actual chapter prose
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class SageAgent(BaseAgent):
    """
    Sage - Lead Writer
    Specializes in:
    - Writing full chapter prose
    - Following voice and style guidelines
    - Maintaining character consistency
    - Executing plot beats
    - Creating engaging scenes
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="sage", agent_type="writing", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Sage's writing task

        Args:
            context: Must contain:
                - chapterNumber
                - outline with this chapter's beats
                - characters
                - previousChapters (for continuity)

        Returns:
            Dictionary with chapter text
        """
        chapter_num = context.get('chapterNumber', 1)

        prompt = self.build_prompt(context)

        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += f"Skriv KAPITEL {chapter_num} som fullständig prosa.\n\n"

        # Find this chapter's beats from outline
        beats_for_this_chapter = self._extract_chapter_beats(context.get('outline', {}), chapter_num)

        if beats_for_this_chapter:
            prompt += "## Plot Beats för Detta Kapitel:\n\n"
            for beat in beats_for_this_chapter:
                prompt += f"- **{beat['name']}**: {beat['description']}\n"
            prompt += "\n"

        prompt += """
## Krav:

1. **Längd**: 2000-3000 ord (ett fullständigt kapitel)
2. **Struktur**:
   - Hook (öppning som drar in)
   - Development (scener som driver plot framåt)
   - Cliffhanger eller resolution (beroende på kapitel)

3. **Visa, berätta inte**:
   - Använd dialog
   - Använd action
   - Använd sensoriska detaljer
   - INTE: "Han var arg" → UTAN: "Hans käkar spände. Naglarna grävde in i handflatorna."

4. **Character voice**:
   - Följ karaktärernas etablerade röster
   - Intern monolog ska matcha deras psykologi
   - Dialog ska kännas naturlig

5. **Pacing**:
   - Korta meningar för action/tension
   - Längre för reflection/atmosfär
   - Variera rytm

6. **Scene-struktur**:
   - Varje scen har: Goal, Conflict, Disaster/Resolution
   - Visa karaktärsutveckling genom action

## Format:

Returnera JSON med:

```json
{
  "title": "Kapitel X: Titel",
  "text": "Hela kapiteltexten här...",
  "wordCount": 2500,
  "scenes": [
    {"summary": "Kort sammanfattning av scen 1"},
    {"summary": "Kort sammanfattning av scen 2"}
  ],
  "keyMoments": [
    "Viktiga händelser i kapitlet"
  ]
}
```

VIKTIGT: Skriv HELA kapitlet, inte bara outline. Detta ska vara publikationsklar prosa.
"""

        # Call LLM with higher token limit for full chapter
        raw_response = self.call_llm(prompt, max_tokens=8000)

        # Parse response
        chapter_data = self.extract_json(raw_response)

        return self.format_output(chapter_data, output_type="json")

    def _extract_chapter_beats(self, outline: Dict[str, Any], chapter_num: int) -> list:
        """Extract plot beats that occur in this chapter"""
        beats = []

        if 'threeActStructure' in outline:
            structure = outline['threeActStructure']
            for act_key in ['act1', 'act2', 'act3']:
                if act_key in structure and 'keyBeats' in structure[act_key]:
                    for beat in structure[act_key]['keyBeats']:
                        if beat.get('chapter') == chapter_num:
                            beats.append(beat)

        # Also check if outline has 'acts' array (alternative format)
        if 'acts' in outline:
            for act in outline['acts']:
                if 'beats' in act:
                    for beat in act['beats']:
                        if beat.get('chapter') == chapter_num:
                            beats.append(beat)

        return beats
