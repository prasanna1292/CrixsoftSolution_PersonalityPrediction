import matplotlib.pyplot as plt

def show_chart(result):

    traits = list(result.keys())
    scores = list(result.values())

    plt.figure(figsize=(8,5))

    plt.bar(traits, scores)

    plt.title("Personality Prediction")

    plt.xlabel("Traits")

    plt.ylabel("Score")

    plt.ylim(0,100)

    plt.show()