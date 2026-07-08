import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from personality_model import predict_personality
from pdf_reader import extract_text
from chart import show_chart
from report import save_report

resume_text = ""

# ---------------- Upload Resume ---------------- #

def upload_resume():
    global resume_text

    file_path = filedialog.askopenfilename(
        filetypes=[("PDF Files", "*.pdf")]
    )

    if file_path:
        try:
            resume_text = extract_text(file_path)

            text_box.delete("1.0", tk.END)
            text_box.insert(tk.END, resume_text)

            messagebox.showinfo(
                "Success",
                "Resume uploaded successfully!"
            )

        except Exception as e:
            messagebox.showerror(
                "Error",
                f"Unable to read PDF\n\n{e}"
            )


# ---------------- Analyze Resume ---------------- #

def analyze_resume():

    if resume_text.strip() == "":
        messagebox.showwarning(
            "Warning",
            "Please upload a resume first."
        )
        return

    result = predict_personality(resume_text)

    # Show Graph
    show_chart(result)

    # Save Report
    filename = save_report(result)

    output_box.delete("1.0", tk.END)

    output_box.insert(
        tk.END,
        "=========== Personality Prediction Report ===========\n\n"
    )

    highest_trait = max(result, key=result.get)

    for trait, score in result.items():

        bars[trait]["value"] = score

        output_box.insert(
            tk.END,
            f"{trait:20}: {score}%\n"
        )

    output_box.insert(
        tk.END,
        "\n-----------------------------------------\n"
    )

    output_box.insert(
        tk.END,
        f"\nDominant Personality : {highest_trait}\n"
    )

    # Recommended Role

    if highest_trait == "Leadership":
        role = "Project Manager"

    elif highest_trait == "Problem Solving":
        role = "Software Engineer"

    elif highest_trait == "Communication":
        role = "HR Executive"

    elif highest_trait == "Creativity":
        role = "UI/UX Designer"

    else:
        role = "Team Coordinator"

    output_box.insert(
        tk.END,
        f"\nRecommended Role : {role}\n"
    )

    output_box.insert(
        tk.END,
        "\n=========================================\n"
    )

    output_box.insert(
        tk.END,
        "\nAnalysis Completed Successfully!"
    )

    messagebox.showinfo(
        "Success",
        f"Report saved as\n\n{filename}"
    )


# ---------------- GUI ---------------- #

root = tk.Tk()

root.title("Personality Prediction Through CV Analysis")

root.geometry("850x750")

root.configure(bg="#f0f4f8")


heading = tk.Label(
    root,
    text="Personality Prediction Through CV Analysis",
    font=("Arial", 18, "bold"),
    bg="#f0f4f8",
    fg="#003366"
)

heading.pack(pady=15)


upload_btn = tk.Button(
    root,
    text="Upload Resume (PDF)",
    command=upload_resume,
    bg="#28a745",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

upload_btn.pack(pady=10)


text_box = tk.Text(
    root,
    height=15,
    width=95
)

text_box.pack(pady=10)


analyze_btn = tk.Button(
    root,
    text="Predict Personality",
    command=analyze_resume,
    bg="#007bff",
    fg="white",
    font=("Arial", 12, "bold"),
    width=20
)

analyze_btn.pack(pady=10)


# ---------------- Progress Bars ---------------- #

progress_frame = tk.Frame(root, bg="#f0f4f8")
progress_frame.pack(pady=10)

traits = [
    "Leadership",
    "Teamwork",
    "Communication",
    "Creativity",
    "Problem Solving"
]

bars = {}

for trait in traits:

    label = tk.Label(
        progress_frame,
        text=trait,
        width=20,
        anchor="w",
        bg="#f0f4f8",
        font=("Arial", 10, "bold")
    )

    label.pack()

    bar = ttk.Progressbar(
        progress_frame,
        orient="horizontal",
        length=350,
        mode="determinate",
        maximum=100
    )

    bar.pack(pady=4)

    bars[trait] = bar


# ---------------- Output Box ---------------- #

output_label = tk.Label(
    root,
    text="Prediction Result",
    font=("Arial", 12, "bold"),
    bg="#f0f4f8"
)

output_label.pack(pady=5)


output_box = tk.Text(
    root,
    height=12,
    width=95,
    bg="white"
)

output_box.pack(pady=10)


root.mainloop()