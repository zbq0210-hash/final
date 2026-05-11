# 🌙 Xiaoliu Ren Reflective Assistant

A culturally inspired GenAI reflection assistant based on Xiaoliu Ren (小六壬).

This project explores how generative AI can transform a traditional symbolic interpretation system into a more contextualized reflective workflow.

The system is designed as a lightweight reflection tool rather than a prediction system.


---

# 1. Context, User, and Problem

## Context

Many people turn to symbolic systems not because they expect accurate predictions, but because they want a structured way to think about uncertainty.

Traditional symbolic systems like Xiaoliu Ren usually provide fixed and generic interpretations. However, users often want reflections that connect to their own situations and emotions.

This project explores whether GenAI can generate more contextualized and personalized reflective responses while still maintaining the symbolic structure of Xiaoliu Ren.

---

## Target User

The target users are students and young adults facing low-stakes uncertainty, such as:

- career questions
- internships
- relationships
- future planning
- study pressure

The system is intended for reflective support and emotional reassurance rather than factual prediction.

---

## Workflow

1. User enters an uncertain personal question
2. The app uses a simple time-based rule to generate one of six Xiaoliu Ren symbolic states.
3. The system maps the number to a Xiaoliu Ren symbolic state
4. The baseline system generates a static interpretation
5. The GenAI system generates a contextualized reflective response
6. The user compares and reflects on the outputs

---

# 2. Solution and Design

## What I Built

I built a Streamlit-based GenAI reflection assistant using OpenAI API.

The application combines:

- a deterministic symbolic generation layer
- prompt-engineered reflective generation
- baseline comparison
- bilingual interface design

The app does not use retrieval, agents, or fine-tuning. The goal was to keep the workflow simple, focused, and easy to evaluate.

---

## Baseline vs GenAI

The project intentionally compares two approaches.

### Baseline System

The baseline maps each Xiaoliu Ren result to a fixed template explanation.

Example:

| Symbolic Result | Baseline Output |
|---|---|
| Xiaoji 小吉 | “This result suggests gradual improvement and small progress.” |

The baseline does not adapt to user context.

---

### GenAI System

The GenAI version uses:

- user question
- symbolic state
- structured prompting
- tone constraints

to generate contextualized reflective suggestions.

This allows the output to adapt to different user situations while maintaining consistency with the symbolic meaning.

---

## Prompt Design

The system prompt explicitly instructs the model to:

- avoid deterministic predictions
- avoid high-stakes advice
- maintain a supportive and reflective tone
- avoid presenting outputs as truth
- frame outputs as symbolic reflection

The app uses:

- OpenAI API
- GPT-4o-mini
- low temperature (`0.4`) for more stable outputs

---

## Multilingual Interface

The interface supports both English and Chinese to better match the cultural origin of Xiaoliu Ren and improve accessibility for bilingual users.

---

# 3. Why GenAI Is Useful

A fixed-template system can only provide static interpretations.

However, this workflow requires:

- adapting symbolic meanings to different user situations
- generating coherent explanations
- maintaining tone consistency
- producing reflective suggestions

These tasks require flexible natural language generation rather than simple classification.

Generative AI is useful because it can create context-aware reflective responses while preserving the symbolic structure of the workflow.

---

# 4. Evaluation and Results

## Evaluation Setup

The system was evaluated using a small fixed test set of user questions, including:

- “Can I get a job next month?”
- “Should I continue this relationship?”
- “Should I change my major?”
- “Is this a good time to move to another city?”

The same questions were tested on:

1. Fixed-template baseline
2. GenAI reflective system

---

## Evaluation Rubric

Outputs were evaluated on:

- Relevance
- Coherence
- Clarity
- Helpfulness
- Tone appropriateness

Each category was scored on a 1–5 scale.

---

## Results

### Baseline Strengths

- simple
- consistent
- predictable

### Baseline Weaknesses

- repetitive
- generic
- unable to adapt to user context

---

### GenAI Strengths

- more personalized
- more emotionally supportive
- better contextual adaptation
- stronger reflective quality

### GenAI Weaknesses

- occasional vague phrasing
- sometimes repetitive
- cannot respond well to highly complex or high-stakes questions
- may generate overly broad reflective suggestions

The system performs best on short, low-stakes, open-ended questions.

---

# 5. Human Role and Trust Boundary

This project is designed as a reflection tool, not a prediction system.

The outputs should not be treated as factual predictions or authoritative advice.

The system should not be trusted for:

- financial decisions
- legal advice
- medical advice
- high-stakes life decisions

Final decisions always remain with the user.

---

# 6. Artifact Snapshot

## Example Input

```text
Can I get a job next month?


## Example Output
1. Symbolic Interpretation
The result of Xiaoji, which translates to "small success," symbolizes a period of gradual improvement and modest support. It suggests that while the journey may not be marked by grand achievements, there is potential for steady progress and small victories along the way. This symbol encourages patience and resilience, highlighting the importance of recognizing and celebrating incremental advancements in one's path.
2. Contextual Reflection
In the context of your question about finding a job in 2026, the notion of small success invites you to consider the steps you can take now that may lead to positive outcomes in the future. Rather than viewing the search for a job as a singular event, it may be more beneficial to think of it as a journey filled with opportunities for learning and growth. The idea of gradual improvement suggests that each effort you make—whether through skill development, networking, or exploring different avenues—can contribute to your overall progress, even if the results are not immediately visible.
3. Reflective Suggestions
Here are three questions to help you reflect on your journey toward finding a job:
1. What skills or experiences can I cultivate now that will enhance my employability in the future?
• Consider taking courses, volunteering, or engaging in projects that align with your career goals.
2. How can I build and nurture my professional network in a way that feels authentic and supportive?
• Reflect on the relationships you can develop and how they might open doors for you down the line.
3. What small successes have I achieved in my career journey so far, and how can I celebrate these milestones?
• Acknowledge your progress, no matter how minor it may seem, as this can boost your confidence and motivation moving forward.






