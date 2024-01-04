```python
import openai
import random

# Set up OpenAI API
openai.api_key = 'your_openai_api_key'

def generate_prompt(data):
    """
    Generate a creative prompt based on user input.
    """
    prompt = data.get('prompt', '')
    tokens = data.get('tokens', 100)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=tokens
    )

    return {'prompt': response.choices[0].text.strip()}

def expand_idea(data):
    """
    Expand on a given idea.
    """
    idea = data.get('idea', '')
    tokens = data.get('tokens', 100)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=idea,
        max_tokens=tokens
    )

    return {'expanded_idea': response.choices[0].text.strip()}

def daily_challenge():
    """
    Generate a daily creative challenge.
    """
    challenges = [
        "Draw a scene from your favorite book",
        "Write a poem about the changing seasons",
        "Create a character based on someone you know",
        "Design a futuristic cityscape",
        "Compose a song about a long journey"
    ]

    challenge = random.choice(challenges)

    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=challenge,
        max_tokens=100
    )

    return {'challenge': response.choices[0].text.strip()}
```

