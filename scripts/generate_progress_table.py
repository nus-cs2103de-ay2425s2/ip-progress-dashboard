import csv
from datetime import datetime, timedelta
import pytz
from collections import defaultdict

def read_task_definitions(file_path):
    tasks = {}
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Strip whitespace from task name and all other fields
            task_name = row['Task Name'].strip()
            tasks[task_name] = {
                'type': row['Task Type'].strip(),
                'is_optional': row['Is Optional'].strip().lower() == 'true',
                'due_date': datetime.strptime(row['Due Date'].strip(), '%Y-%m-%d %H:%M'),
                'week_number': int(row['Week Number'].strip())
            }
    return tasks

def read_student_progress(file_path):
    with open(file_path, 'r') as f:
        reader = csv.DictReader(f)
        # Convert to list and strip whitespace from all field names
        headers = [h.strip() for h in reader.fieldnames]
        # Create a new reader with cleaned headers
        f.seek(0)
        next(f)  # Skip the header row
        return list(csv.DictReader(f, fieldnames=headers))

def should_show_task(task_info):
    now = datetime.now(pytz.timezone('Asia/Singapore'))
    due_date = task_info['due_date'].replace(tzinfo=pytz.timezone('Asia/Singapore'))
    
    # Show tasks that are:
    # 1. Due before today (past tasks)
    # 2. Due within the next 5 days (upcoming tasks)
    return due_date <= now + timedelta(days=5)

def get_badge_html(task_name, is_completed, task_info):
    now = datetime.now(pytz.timezone('Asia/Singapore'))
    due_date = task_info['due_date'].replace(tzinfo=pytz.timezone('Asia/Singapore'))
    is_overdue = now > due_date
    is_optional = task_info['is_optional']
    
    # Clean up completion status and ensure it's treated as a string
    is_completed = str(is_completed).strip() if is_completed is not None else '0'
    
    if is_completed == '1':
        # Optional tasks use bg-info, required tasks use bg-success
        badge_class = 'bg-info' if is_optional else 'bg-success'
    else:
        # Not completed tasks
        if is_overdue:
            badge_class = 'bg-danger'  # Overdue tasks are red
        else:
            # Optional tasks use bg-secondary, required tasks use bg-dark
            badge_class = 'bg-secondary' if is_optional else 'bg-dark'
    
    text = task_name if is_completed == '1' else f'!{task_name}'
    return f'<span class="badge {badge_class} me-1">{text}</span>'

def sort_tasks(tasks):
    # Create a dictionary to store tasks by type without sorting
    sorted_tasks = defaultdict(lambda: defaultdict(list))
    for task_name, info in tasks.items():
        if should_show_task(info):  # Only include tasks that should be shown
            sorted_tasks[info['type']][info['week_number']].append((task_name, info))
    
    # Remove the sorting step to maintain original sequence
    return sorted_tasks

def generate_progress_table(students, tasks):
    header = '''%%[This page was ==last updated on **{{ timestamp }}**==]%%    

<tooltip content="NUSNET (partial)">Student</tooltip>|<tooltip content="i.e., weeks in which some code was committed to the repo">Weekly progress</tooltip>|<tooltip content="i.e., iP increments as indicated by the git tags in your fork">Increments</tooltip>|<tooltip content="i.e., other iP-related admin tasks">Admin tasks</tooltip>
-----------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------'''
    
    output = [header]
    
    # Create ordered lists for each type
    weekly_tasks = []
    increment_tasks = []
    admin_tasks = []
    
    # First pass: collect tasks in original order from task_definitions.csv
    with open('data/task_definitions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            task_name = row['Task Name'].strip()
            if task_name in tasks and should_show_task(tasks[task_name]):
                task_info = tasks[task_name]
                if task_info['type'] == 'Weekly':
                    weekly_tasks.append((task_name, task_info))
                elif task_info['type'] == 'Increment':
                    increment_tasks.append((task_name, task_info))
                elif task_info['type'] == 'Admin':
                    admin_tasks.append((task_name, task_info))
    
    for student in students:
        weekly_badges = []
        increment_badges = []
        admin_badges = []
        
        # Process Weekly tasks
        for task_name, task_info in weekly_tasks:
            if task_name in student:
                badge = get_badge_html(task_name, student[task_name], task_info)
                weekly_badges.append(badge)
        
        # Process Increment tasks
        for task_name, task_info in increment_tasks:
            if task_name in student:
                badge = get_badge_html(task_name, student[task_name], task_info)
                increment_badges.append(badge)
        
        # Process Admin tasks
        for task_name, task_info in admin_tasks:
            if task_name in student:
                badge = get_badge_html(task_name, student[task_name], task_info)
                admin_badges.append(badge)
        
        student_row = f"{student['Student ID']}|{''.join(weekly_badges)}|{''.join(increment_badges)}|{''.join(admin_badges)}"
        output.append(student_row)
    
    return '\n'.join(output)

def main():
    # Read the CSV files
    tasks = read_task_definitions('data/task_definitions.csv')
    students = read_student_progress('data/student_progress.csv')
    
    # Debug print task definitions and student progress
    print("\nTask Definitions loaded:")
    with open('data/task_definitions.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            task_name = row['Task Name'].strip()
            if task_name in tasks:
                info = tasks[task_name]
                print(f"{task_name}: Week {info['week_number']}, Type: {info['type']}, Optional: {info['is_optional']}")
    
    print("\nChecking for undefined tasks in student progress:")
    if students:
        student = students[0]
        for task_name in sorted(student.keys()):
            if task_name not in tasks and task_name not in ['Full Name', 'Student ID']:
                print(f"Warning: Task '{task_name}' in student progress but not in task definitions")
    
    # Generate the markdown content
    markdown_content = generate_progress_table(students, tasks)
    
    # Write to the output file
    output_path = 'contents/cs2103/ip-progress-table-fragment.md'
    with open(output_path, 'w') as f:
        f.write(markdown_content)

if __name__ == '__main__':
    main() 