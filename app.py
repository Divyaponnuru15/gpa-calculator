from flask import Flask, render_template, request
from gpa_calculation import calculate_gpa

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    gpa_list = []
    cgpa = None
    total_sem = 0

    if request.method == "POST":
        total_sem = int(request.form["total_sem"])
        semesters_data = []

        for sem in range(1, total_sem + 1):
            theory_input = request.form.get(f"theory_sem{sem}", "")
            practical_input = request.form.get(f"practical_sem{sem}", "")

            theory_grades = [g.strip().upper() for g in theory_input.split(",") if g.strip()]
            practical_grades = [g.strip().upper() for g in practical_input.split(",") if g.strip()]

            semesters_data.append({
                "theory": theory_grades,
                "practical": practical_grades
            })

        gpa_list, cgpa = calculate_gpa(total_sem, semesters_data)

    return render_template(
        "index.html",
        total_sem=total_sem,
        gpa_list=gpa_list,
        cgpa=cgpa
    )

if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=5000)

    # app.run(debug=True)
