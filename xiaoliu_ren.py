from datetime import datetime

RESULTS = [
    "Da'an 大安",
    "Liulian 留连",
    "Suxi 速喜",
    "Chikou 赤口",
    "Xiaoji 小吉",
    "Kongwang 空亡"
]

MEANINGS = {
    "Da'an 大安": "Stability, calmness, and steady progress.",
    "Liulian 留连": "Delay, hesitation, or temporary stagnation.",
    "Suxi 速喜": "Quick movement, positive news, or fast change.",
    "Chikou 赤口": "Conflict, misunderstanding, or communication risk.",
    "Xiaoji 小吉": "Small success, gradual improvement, or modest support.",
    "Kongwang 空亡": "Uncertainty, emptiness, or unclear direction."
}

def generate_result():
    now = datetime.now()
    index = (now.month + now.day + now.hour) % 6
    return RESULTS[index]

def get_meaning(result):
    return MEANINGS[result]