"""
Base Agent Class
All NOIR agents inherit from this
"""

from typing import Dict, Any, Optional
from pathlib import Path
import json
from datetime import datetime


class BaseAgent:
    """
    Base class for all NOIR agents.
    Each agent has:
    - A prompt template (loaded from .md file)
    - An LLM client for API calls
    - Context management
    - Output formatting
    """

    def __init__(self, agent_name: str, agent_type: str, llm_client=None):
        """
        Initialize agent

        Args:
            agent_name: Name of agent (e.g., 'harper', 'morgan')
            agent_type: Type of agent ('creative', 'writing', 'quality')
            llm_client: LLMClient instance for API calls
        """
        self.name = agent_name
        self.type = agent_type
        self.llm_client = llm_client

        # Load agent prompt template
        self.prompt_template = self._load_prompt_template()

    def _load_prompt_template(self) -> str:
        """Load agent's prompt from .md file"""
        base_dir = Path(__file__).parent
        prompt_file = base_dir / self.type / f"{self.name}.md"

        if not prompt_file.exists():
            raise FileNotFoundError(f"Agent prompt not found: {prompt_file}")

        with open(prompt_file, 'r', encoding='utf-8') as f:
            return f.read()

    def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute agent's task

        Args:
            context: Dictionary with all relevant context (plot, characters, etc.)

        Returns:
            Dictionary with agent's output
        """
        raise NotImplementedError("Subclasses must implement execute()")

    def build_prompt(self, context: Dict[str, Any]) -> str:
        """
        Build complete prompt from template + context

        Args:
            context: Context data to inject into prompt

        Returns:
            Complete prompt ready for LLM
        """
        # Start with agent's base prompt
        prompt = self.prompt_template

        # Add context section
        prompt += "\n\n---\n\n# KONTEXT\n\n"

        # Add relevant context
        if 'plotBrief' in context:
            prompt += f"\n## Plot Brief från Författaren\n\n{context['plotBrief']}\n"

        if 'genre' in context:
            prompt += f"\n## Genre\n{context['genre']}\n"

        if 'outline' in context and context['outline']:
            prompt += f"\n## Nuvarande Outline\n{json.dumps(context['outline'], indent=2, ensure_ascii=False)}\n"

        if 'characters' in context and context['characters']:
            prompt += f"\n## Karaktärer\n{json.dumps(context['characters'], indent=2, ensure_ascii=False)}\n"

        if 'previousChapters' in context and context['previousChapters']:
            prompt += f"\n## Tidigare Kapitel\n{self._format_previous_chapters(context['previousChapters'])}\n"

        return prompt

    def _format_previous_chapters(self, chapters: list) -> str:
        """Format previous chapters for context"""
        formatted = ""
        for ch in chapters[-3:]:  # Only last 3 chapters for context
            formatted += f"\n### Kapitel {ch['number']}: {ch['title']}\n"
            formatted += f"{ch.get('synopsis', '')}\n"
        return formatted

    def call_llm(self, prompt: str, max_tokens: int = 4000) -> str:
        """
        Call LLM with prompt

        Args:
            prompt: Complete prompt
            max_tokens: Maximum tokens in response

        Returns:
            LLM response text
        """
        if not self.llm_client:
            raise ValueError("No LLM client configured")

        return self.llm_client.complete(prompt, max_tokens=max_tokens)

    def format_output(self, raw_output: str, output_type: str = "json") -> Dict[str, Any]:
        """
        Format LLM output into structured data

        Args:
            raw_output: Raw text from LLM
            output_type: Expected output type ('json', 'text', 'markdown')

        Returns:
            Structured output dictionary
        """
        return {
            "agent": self.name,
            "type": self.type,
            "timestamp": datetime.now().isoformat(),
            "output": raw_output,
            "status": "completed"
        }

    def extract_json(self, text: str) -> Dict[str, Any]:
        """
        Extract JSON from LLM response
        LLMs often wrap JSON in markdown code blocks
        """
        # Try to find JSON in markdown code block
        import re

        # Look for ```json ... ```
        json_match = re.search(r'```json\s*\n(.*?)\n```', text, re.DOTALL)
        if json_match:
            text = json_match.group(1)

        # Look for ```  ... ``` (without json specifier)
        elif '```' in text:
            code_match = re.search(r'```\s*\n(.*?)\n```', text, re.DOTALL)
            if code_match:
                text = code_match.group(1)

        # Try to parse as JSON
        try:
            return json.loads(text)
        except json.JSONDecodeError as e:
            print(f"⚠️ Warning: Could not parse JSON from {self.name}: {e}")
            print(f"Raw text: {text[:200]}...")
            return {"raw": text, "parseError": str(e)}
