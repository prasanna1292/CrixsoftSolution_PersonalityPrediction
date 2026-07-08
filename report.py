from datetime import datetime

def save_report(result):

    filename = "Personality_Report.txt"

    with open(filename, "w") as file:

        file.write("PERSONALITY PREDICTION REPORT\n")
        file.write("==============================\n\n")

        file.write("Generated On : ")

        file.write(str(datetime.now()))

        file.write("\n\n")

        for trait, score in result.items():

            file.write(f"{trait}: {score}%\n")

    return filename