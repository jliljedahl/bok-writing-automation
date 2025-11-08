"""
Ellis - Quality Reviewer Agent
Reviews and provides feedback on chapters
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from agents.base_agent import BaseAgent
from typing import Dict, Any


class EllisAgent(BaseAgent):
    """
    Ellis - Quality Reviewer
    Specializes in:
    - Reviewing chapter quality
    - Providing actionable feedback
    - Scoring on multiple dimensions
    - Identifying strengths and weaknesses
    """

    def __init__(self, llm_client=None):
        super().__init__(agent_name="ellis", agent_type="quality", llm_client=llm_client)

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute Ellis's review task

        Args:
            context: Must contain:
                - chapterText: The chapter to review
                - chapterNumber: Which chapter
                - outline: For checking if beats were hit
                - characters: For consistency check

        Returns:
            Dictionary with detailed review
        """
        chapter_num = context.get('chapterNumber', 1)
        chapter_text = context.get('chapterText', '')

        prompt = self.build_prompt(context)

        prompt += "\n\n---\n\n# DIN UPPGIFT\n\n"
        prompt += f"Granska KAPITEL {chapter_num} och ge detaljerad feedback.\n\n"
        prompt += f"## Kapiteltext att granska:\n\n{chapter_text}\n\n"
        prompt += "---\n\n"
        prompt += """
## Granskningskriterier:

Betygsätt varje kategori 1-10 och ge konkret feedback:

1. **Pacing** (1-10)
   - Är tempot rätt?
   - Drar scener ut för länge eller rushas de igenom?
   - Varierar rytmen?

2. **Tension/Suspense** (1-10)
   - Bygger kapitlet spänning?
   - Finns conflict i varje scen?
   - Vill man läsa vidare?

3. **Dialogue** (1-10)
   - Låter dialogerna naturliga?
   - Har varje karaktär distinkt röst?
   - Driver dialog plot framåt?

4. **Character Consistency** (1-10)
   - Agerar karaktärer enligt sina etablerade profiler?
   - Känns deras beslut trovärdiga?
   - Visas character development?

5. **Prose Quality** (1-10)
   - Språket vackert men inte blomsterikt?
   - Bra variation i meningslängd?
   - Undviks klyschor?

6. **Plot Advancement** (1-10)
   - Driver kapitlet handlingen framåt?
   - Träffas plot beats?
   - Finns consequences för actions?

7. **Atmosphere** (1-10)
   - Skapas rätt mood?
   - Används sensoriska detaljer effektivt?
   - Känns setting levande?

## Returnera JSON:

```json
{
  "overallScore": 8,
  "categories": {
    "pacing": {
      "score": 8,
      "feedback": "Konkret kommentar om pacing..."
    },
    "tension": {
      "score": 7,
      "feedback": "..."
    },
    "dialogue": {
      "score": 9,
      "feedback": "..."
    },
    "characterConsistency": {
      "score": 8,
      "feedback": "..."
    },
    "proseQuality": {
      "score": 7,
      "feedback": "..."
    },
    "plotAdvancement": {
      "score": 8,
      "feedback": "..."
    },
    "atmosphere": {
      "score": 9,
      "feedback": "..."
    }
  },
  "strengths": [
    "Specifik styrka 1",
    "Specifik styrka 2",
    "Specifik styrka 3"
  ],
  "improvements": [
    "Specifik förbättring med exempel från texten",
    "Annan förbättring"
  ],
  "mustFix": [
    "Kritiska problem som MÅSTE åtgärdas"
  ],
  "verdict": "APPROVE / APPROVE_WITH_MINOR_REVISIONS / NEEDS_REVISION / REJECT"
}
```

## Bedömningskriterier för verdict:

- **APPROVE**: Score 9-10, inga större problem
- **APPROVE_WITH_MINOR_REVISIONS**: Score 7-8, små justeringar
- **NEEDS_REVISION**: Score 5-6, betydande problem
- **REJECT**: Score 1-4, måste skrivas om

Var konstruktiv men ärlig. Ge konkreta exempel från texten.
"""

        # Call LLM
        raw_response = self.call_llm(prompt, max_tokens=4000)

        # Parse review
        review = self.extract_json(raw_response)

        return self.format_output(review, output_type="json")
