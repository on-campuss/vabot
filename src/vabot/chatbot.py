from openai import OpenAI
from typing import Optional

class Vabot(object):
    def __init__(self, api_key: str, organization_id: Optional[str]=None) -> None:
        self.api_key: str = api_key
        self.engine: str = "text-davinci-003"
        self.model = "gpt-3.5-turbo"
        self.oganization_id = organization_id

        self.client: OpenAI = OpenAI(api_key=self.api_key, organization=self.oganization_id)

    def generate_response(self, prompt: str, max_tokens: int = 50, temperature: float = 0.7):
        response = self.client.completions.create(
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
            model= self.model,
            messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who won the world series in 2020?"},
    {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
    {"role": "user", "content": "Where was it played?"}
  ]


        )
        return response.choices[0].text.strip()