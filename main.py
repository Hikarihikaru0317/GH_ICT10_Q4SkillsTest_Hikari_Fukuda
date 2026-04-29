from pyscript import display, document
import numpy as np
import matplotlib.pyplot as plt

attendance = {
    'Monday': 0,
    'Tuesday': 0,
    'Wednesday': 0,
    'Thursday': 0,
    'Friday': 0
}

submitted_days = []

def submit_attendance(e):
    day = document.getElementById('day-select').value
    absences = int(document.getElementById('absences-input').value)

    attendance[day] = absences

    if day not in submitted_days:
        submitted_days.append(day)
        
    progress = len(submitted_days) * 20
    document.getElementById('progress-bar').style.width = str(progress) + '%'


    plt.close('all')
    document.getElementById('output').innerHTML = " "


    ordered_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    days_to_plot = np.array([d for d in ordered_days if d in submitted_days])
    absences_to_plot = np.array([attendance[d] for d in ordered_days if d in submitted_days])


    fig, ax = plt.subplots(figsize=(5.5, 3.8))
    ax.plot(days_to_plot, absences_to_plot, marker='o', color='steelblue', linewidth=2)

    ax.set_title("Weekly Attendance (Absences)") 
    ax.set_xlabel("Day")                          
    ax.set_ylabel("Number of Absences")          
    ax.grid(True, linestyle='--', alpha=0.5)
    fig.tight_layout()

    display(fig, target='output')