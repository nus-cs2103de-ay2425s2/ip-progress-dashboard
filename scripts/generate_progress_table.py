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
    # 2. Due within the next 7 days (upcoming tasks)
    return due_date <= now + timedelta(days=7)

def get_badge_html(task_name, is_completed, task_info):
    now = datetime.now(pytz.timezone('Asia/Singapore'))
    due_date = task_info['due_date'].replace(tzinfo=pytz.timezone('Asia/Singapore'))
    is_overdue = now > due_date
    is_optional = task_info['is_optional']
    
    # Use actual completion status from CSV
    is_completed = is_completed.strip() if isinstance(is_completed, str) else is_completed
    
    if is_completed == '1':
        badge_class = 'bg-info' if is_optional else 'bg-success'
    else:
        if is_overdue:
            badge_class = 'bg-danger'
        else:
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
    task_groups = defaultdict(list)
    
    # Group tasks by type while maintaining original order
    for task_name, info in tasks.items():
        if should_show_task(info):
            task_groups[info['type']].append((task_name, info))
    
    for student in students:
        weekly_progress = []
        increments = []
        admin_tasks = []
        
        # Process tasks in original order within each type
        for task_name, task_info in task_groups['Weekly']:
            badge = get_badge_html(task_name, student[task_name], task_info)
            weekly_progress.append(badge)
        
        for task_name, task_info in task_groups['Increment']:
            badge = get_badge_html(task_name, student[task_name], task_info)
            increments.append(badge)
        
        for task_name, task_info in task_groups['Admin']:
            badge = get_badge_html(task_name, student[task_name], task_info)
            admin_tasks.append(badge)
        
        student_row = f"{student['Student ID']}|{''.join(weekly_progress)}|{''.join(increments)}|{''.join(admin_tasks)}"
        output.append(student_row)
    
    return '\n'.join(output)

def main():
    # Read the CSV files
    tasks = read_task_definitions('data/task_definitions.csv')
    students = read_student_progress('data/student_progress.csv')
    
    # Debug print task definitions
    print("\nTask Definitions loaded:")
    for task_name, info in tasks.items():
        if task_name == 'JAR released':
            print(f"Found JAR released task:")
            print(f"  Type: {info['type']}")
            print(f"  Optional: {info['is_optional']}")
            print(f"  Due Date: {info['due_date']}")
            print(f"  Week: {info['week_number']}")
    
    # Generate the markdown content
    markdown_content = generate_progress_table(students, tasks)
    
    # Write to the output file
    output_path = 'contents/cs2103/ip-progress-table-fragment.md'
    with open(output_path, 'w') as f:
        f.write(markdown_content)

if __name__ == '__main__':
    main() 