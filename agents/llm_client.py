"""
LLM Client for API calls to Claude, GPT, etc.
"""

import os
from typing import Optional, Dict, Any
import json


class LLMClient:
    """
    Client for making LLM API calls.
    Supports multiple providers (Claude, OpenAI, etc.)
    """

    def __init__(self, provider: str = "claude", api_key: Optional[str] = None, model: Optional[str] = None):
        """
        Initialize LLM client

        Args:
            provider: 'claude', 'openai', or 'mock' for testing
            api_key: API key (or reads from environment)
            model: Specific model to use
        """
        self.provider = provider.lower()
        self.api_key = api_key or self._get_api_key()
        self.model = model or self._get_default_model()

        # Initialize provider client
        if self.provider == "claude":
            self._init_claude()
        elif self.provider == "openai":
            self._init_openai()
        elif self.provider == "mock":
            print("⚠️ Using MOCK LLM - no real API calls")
        else:
            raise ValueError(f"Unknown provider: {provider}")

    def _get_api_key(self) -> Optional[str]:
        """Get API key from environment"""
        if self.provider == "claude":
            return os.getenv("ANTHROPIC_API_KEY")
        elif self.provider == "openai":
            return os.getenv("OPENAI_API_KEY")
        return None

    def _get_default_model(self) -> str:
        """Get default model for provider"""
        defaults = {
            "claude": "claude-3-5-sonnet-20241022",
            "openai": "gpt-4-turbo-preview",
            "mock": "mock-model"
        }
        return defaults.get(self.provider, "")

    def _init_claude(self):
        """Initialize Anthropic Claude client"""
        try:
            import anthropic
            if not self.api_key:
                print("⚠️ No ANTHROPIC_API_KEY found. Set it with:")
                print("   export ANTHROPIC_API_KEY='your-key-here'")
                print("   Using MOCK mode instead.")
                self.provider = "mock"
                return

            self.client = anthropic.Anthropic(api_key=self.api_key)
            print(f"✅ Claude client initialized with model: {self.model}")

        except ImportError:
            print("⚠️ Anthropic package not installed. Install with:")
            print("   pip install anthropic")
            print("   Using MOCK mode instead.")
            self.provider = "mock"

    def _init_openai(self):
        """Initialize OpenAI client"""
        try:
            import openai
            if not self.api_key:
                print("⚠️ No OPENAI_API_KEY found. Using MOCK mode.")
                self.provider = "mock"
                return

            self.client = openai.OpenAI(api_key=self.api_key)
            print(f"✅ OpenAI client initialized with model: {self.model}")

        except ImportError:
            print("⚠️ OpenAI package not installed. Using MOCK mode.")
            self.provider = "mock"

    def complete(self, prompt: str, max_tokens: int = 4000, temperature: float = 0.7) -> str:
        """
        Get completion from LLM

        Args:
            prompt: The prompt to send
            max_tokens: Maximum tokens in response
            temperature: Sampling temperature (0-1)

        Returns:
            LLM response text
        """
        if self.provider == "mock":
            return self._mock_complete(prompt, max_tokens)
        elif self.provider == "claude":
            return self._claude_complete(prompt, max_tokens, temperature)
        elif self.provider == "openai":
            return self._openai_complete(prompt, max_tokens, temperature)
        else:
            raise ValueError(f"Unknown provider: {self.provider}")

    def _claude_complete(self, prompt: str, max_tokens: int, temperature: float) -> str:
        """Call Claude API"""
        try:
            message = self.client.messages.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return message.content[0].text

        except Exception as e:
            print(f"❌ Claude API error: {e}")
            print("Falling back to MOCK mode for this call...")
            return self._mock_complete(prompt, max_tokens)

    def _openai_complete(self, prompt: str, max_tokens: int, temperature: float) -> str:
        """Call OpenAI API"""
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                max_tokens=max_tokens,
                temperature=temperature,
                messages=[
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content

        except Exception as e:
            print(f"❌ OpenAI API error: {e}")
            print("Falling back to MOCK mode for this call...")
            return self._mock_complete(prompt, max_tokens)

    def _mock_complete(self, prompt: str, max_tokens: int) -> str:
        """
        Mock completion for testing without API calls
        Returns structured placeholder based on what's being asked
        """
        prompt_lower = prompt.lower()

        # Detect what kind of output is expected based on prompt
        # Order matters - check most specific first!
        if "morgan" in prompt_lower or ("karaktär" in prompt_lower and "psykolog" in prompt_lower):
            return self._mock_character_output()
        elif "harper" in prompt_lower or ("plot" in prompt_lower and "architect" in prompt_lower):
            return self._mock_plot_output()
        elif "chapter" in prompt_lower and "write" in prompt_lower:
            return self._mock_chapter_output()
        elif "review" in prompt_lower or "feedback" in prompt_lower or "ellis" in prompt_lower:
            return self._mock_review_output()
        elif "character" in prompt_lower or "protagonist" in prompt_lower:
            return self._mock_character_output()
        elif "logline" in prompt_lower or "plot" in prompt_lower:
            return self._mock_plot_output()
        else:
            return f"[MOCK RESPONSE - {max_tokens} tokens]\n\nThis is a placeholder response for testing.\n\nPrompt was: {prompt[:100]}..."

    def _mock_plot_output(self) -> str:
        """Mock plot/outline generation"""
        return """
{
  "logline": "En utbränd detektiv måste konfrontera sitt mörka förflutna när en serie mord tvingar honom tillbaka till den stad han svurit att aldrig återvända till.",
  "hook": "Första kroppen hittas på exakt samma plats där hans partner dog för tio år sedan.",
  "twist": "Mördaren är inte vem vi tror - utan någon som protagonist själv indirekt skapat genom sina tidigare handlingar.",
  "resolution": "Protagonist offrar sin frihet för att rädda andra och hittar slutligen försoning genom att acceptera sitt ansvar.",
  "threeActStructure": {
    "act1": {
      "description": "Setup - introducera världen, protagonistens ghost, och inciting incident",
      "keyBeats": [
        {"name": "Opening Image", "description": "Protagonist i sin nya tillvaro, försöker fly sitt förflutna"},
        {"name": "Inciting Incident", "description": "Kallad tillbaka till gamla staden för att hjälpa med mord"},
        {"name": "First Plot Point", "description": "Upptäcker koppling till sitt eget förflutna, kan inte vända om"}
      ]
    },
    "act2": {
      "description": "Confrontation - jakten intensifieras, twists avslöjas",
      "keyBeats": [
        {"name": "Midpoint", "description": "Stor upptäckt som vänder allt upp och ner"},
        {"name": "All Is Lost", "description": "Protagonist förlorar allt och står ensam"}
      ]
    },
    "act3": {
      "description": "Resolution - klimax och upplösning",
      "keyBeats": [
        {"name": "Climax", "description": "Final konfrontation med antagonist och sig själv"},
        {"name": "Resolution", "description": "Ny jämvikt, protagonist har förändrats"}
      ]
    }
  }
}
"""

    def _mock_character_output(self) -> str:
        """Mock character creation"""
        return """
{
  "protagonist": {
    "name": "Erik Lindström",
    "age": 45,
    "occupation": "Före detta kriminalinspektör, nu säkerhetsrådgivare",
    "psychology": {
      "ghost": "Hans partner dog under en operation han ledde för 10 år sedan. Skulden har förlamat honom.",
      "want": "Vill bevisa att han inte är ansvarig för partnerns död",
      "need": "Behöver acceptera sitt ansvar och förlåta sig själv",
      "fear": "Rädd för att förlora fler människor han bryr sig om",
      "flaw": "Isolerar sig och undviker djupa relationer för att skydda sig själv"
    },
    "arc": {
      "beginning": "Cynisk, isolerad, lever i skuggan av sitt förflutna",
      "middle": "Tvingas konfrontera gamla demoner och börjar känna igen",
      "end": "Accepterar sitt ansvar, förlåter sig själv, öppnar sig för andra"
    }
  },
  "antagonist": {
    "name": "Martin Söderberg",
    "motivation": "Hämnas på de som förstörde hans liv genom systemets försummelser",
    "connection": "Bror till en person som dog i same incident som partnern",
    "sympathy": "Förlorade allt på grund av andras misstag. Hans smärta är verklig och förståelig."
  }
}
"""

    def _mock_chapter_output(self) -> str:
        """Mock chapter writing"""
        return """
Regnet smattrade mot bilrutan när Erik Lindström körde in mot staden han svurit att aldrig återvända till. Tio år. Tio långa år sedan han lämnat Ystad och allt det innebar.

Hans telefon surrade på passagerarsätet. Samma nummer som ringt tre gånger redan. Han visste vem det var. Visste vad de ville.

"Lindström," sa han när han äntligen svarade.

"Vi behöver dig här. Du vet varför."

Erik slöt ögonen en kort sekund. Ja, han visste. Den första kroppen hade hittats exakt där Anna föll. Exakt samma plats. Det kunde inte vara en tillfällighet.

"Jag är på väg," sa han och la på.

[... resten av kapitlet fortsätter ...]

KAPITEL SLUT
"""

    def _mock_review_output(self) -> str:
        """Mock quality review"""
        return """
{
  "overallScore": 8,
  "categories": {
    "pacing": {
      "score": 8,
      "feedback": "Bra tempo, bygger tension effektivt. Öppningsscenen drar in läsaren direkt."
    },
    "characterization": {
      "score": 7,
      "feedback": "Erik är välskriven men kunde visa mer inre konflikt i öppningen."
    },
    "dialogue": {
      "score": 9,
      "feedback": "Naturlig och koncis. Telefonsamtalet är särskilt bra."
    },
    "atmosphere": {
      "score": 8,
      "feedback": "Regnet och setting skapar mörk ton perfekt för noir."
    }
  },
  "strengths": [
    "Stark hook - koppling till förflutna väcker direkt frågor",
    "Koncis prosa som matchar genren",
    "Bra use of weather för atmosfär"
  ],
  "improvements": [
    "Lägg till mer sensoriska detaljer i öppningen",
    "Utforska Eriks inre monolog lite djupare",
    "Fler konkreta detaljer om staden när han närmar sig"
  ],
  "mustFix": [],
  "verdict": "APPROVE_WITH_MINOR_REVISIONS"
}
"""
