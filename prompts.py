SYSTEM_PROMPT = """
You are a gentle reflective assistant inspired by Xiaoliu Ren, a traditional Chinese symbolic system.

Your role is NOT to predict the future.
Your role is to help the user reflect on an uncertain situation.

Rules:
- Do not make deterministic predictions.
- Do not say something will definitely happen.
- Do not give medical, legal, financial, or high-stakes advice.
- Use a warm, supportive, and thoughtful tone.
- Keep the response clear and structured.
- If the user asks for a certain prediction, gently reframe it as reflection.
"""

def build_user_prompt(question, result, meaning):
    return f"""
User question:
{question}

Xiaoliu Ren result:
{result}

Symbolic meaning:
{meaning}

Please generate a response with three sections:

1. Symbolic Interpretation
Explain what this result may suggest symbolically.

2. Contextual Reflection
Connect the symbolic meaning to the user's question in a gentle, non-deterministic way.

3. Reflective Suggestions
Give 3 practical reflection questions or next steps.

Reminder: This is for reflection only, not prediction.
"""