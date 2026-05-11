BASELINE_TEMPLATES = {
    "Da'an 大安": "This result suggests stability and smooth progress. You may continue carefully and avoid unnecessary changes.",
    "Liulian 留连": "This result suggests delay or stagnation. You may need to wait, observe, and avoid rushing.",
    "Suxi 速喜": "This result suggests fast movement or possible good news. You may take action, but still stay realistic.",
    "Chikou 赤口": "This result suggests conflict or misunderstanding. You should be careful with communication and avoid impulsive decisions.",
    "Xiaoji 小吉": "This result suggests small success or gradual improvement. You may move forward step by step.",
    "Kongwang 空亡": "This result suggests uncertainty or lack of clarity. You may need more information before making a decision."
}

def get_baseline(result):
    return BASELINE_TEMPLATES[result]