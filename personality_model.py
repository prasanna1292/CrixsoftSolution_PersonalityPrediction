def predict_personality(text):
    text = text.lower()

    traits = {
        "Leadership": 0,
        "Teamwork": 0,
        "Communication": 0,
        "Creativity": 0,
        "Problem Solving": 0
    }

    keywords = {
        "Leadership": [
            "leader", "leadership", "managed",
            "captain", "mentor"
        ],

        "Teamwork": [
            "team", "collaboration",
            "group", "cooperate"
        ],

        "Communication": [
            "communication", "presentation",
            "public speaking", "speaker"
        ],

        "Creativity": [
            "creative", "innovation",
            "design", "developed"
        ],

        "Problem Solving": [
            "problem", "analysis",
            "solution", "debug",
            "algorithm"
        ]
    }

    for trait in keywords:

        for word in keywords[trait]:

            if word in text:
                traits[trait] += 20

        if traits[trait] > 100:
            traits[trait] = 100

    return traits