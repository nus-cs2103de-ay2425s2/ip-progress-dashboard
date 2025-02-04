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
    
    # For testing: only show week 3 and 4 tasks
    return task_info['week_number'] in [3, 4]
    
    # Actual logic (commented out for now):
    # return due_date <= now + timedelta(days=7)

def get_badge_html(task_name, is_completed, task_info):
    now = datetime.now(pytz.timezone('Asia/Singapore'))
    due_date = task_info['due_date'].replace(tzinfo=pytz.timezone('Asia/Singapore'))
    is_overdue = now > due_date
    is_optional = task_info['is_optional']
    
    # For testing: override completion status based on week number
    if task_info['week_number'] == 3:
        is_completed = '1'  # Mark all week 3 tasks as completed
    elif task_info['week_number'] == 4:
        is_completed = '0'  # Mark all week 4 tasks as not completed
    else:
        is_completed = is_completed.strip() if isinstance(is_completed, str) else is_completed
    
    # Debug print for JAR released task
    if task_name == 'JAR released':
        print(f"Processing JAR released task:")
        print(f"  is_completed (raw): {is_completed}")
        print(f"  is_optional: {is_optional}")
        print(f"  is_overdue: {is_overdue}")
    
    if is_completed == '1':
        # Completed tasks
        badge_class = 'bg-info' if is_optional else 'bg-success'
    else:
        # Not completed tasks
        if is_overdue:
            badge_class = 'bg-danger'  # Red for overdue
        else:
            badge_class = 'bg-secondary' if is_optional else 'bg-dark'  # Gray for optional, black for required
    
    # For not completed tasks, strike through the text
    text = task_name if is_completed == '1' else f'!{task_name}'
    return f'<span class="badge {badge_class} me-1">{text}</span>'

def sort_tasks(tasks):
    # Create a dictionary to store tasks by type and week
    sorted_tasks = defaultdict(lambda: defaultdict(list))
    for task_name, info in tasks.items():
        if should_show_task(info):  # Only include tasks that should be shown
            sorted_tasks[info['type']][info['week_number']].append((task_name, info))
    
    # For each type, sort by week and then by task name
    for task_type in sorted_tasks:
        for week in sorted_tasks[task_type]:
            sorted_tasks[task_type][week].sort(key=lambda x: x[0])
    
    return sorted_tasks

def generate_progress_table(students, tasks):
    # Header template
    header = '''%%[This page was ==last updated on **{{ timestamp }}**==]%%    

<tooltip content="NUSNET (partial)">Student</tooltip>|<tooltip content="i.e., weeks in which some code was committed to the repo">Weekly progress</tooltip>|<tooltip content="i.e., iP increments as indicated by the git tags in your fork">Increments</tooltip>|<tooltip content="i.e., other iP-related admin tasks">Admin tasks</tooltip>
-----------------------------------------------------|-----------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------'''
    
    output = [header]
    sorted_tasks = sort_tasks(tasks)
    
    for student in students:
        # Initialize the three sections
        weekly_progress = []
        increments = []
        admin_tasks = []
        
        # Process Weekly tasks
        for week in sorted(sorted_tasks['Weekly'].keys()):
            for task_name, task_info in sorted_tasks['Weekly'][week]:
                badge = get_badge_html(task_name, student[task_name], task_info)
                weekly_progress.append(badge)
        
        # Process Increment tasks
        for week in sorted(sorted_tasks['Increment'].keys()):
            for task_name, task_info in sorted_tasks['Increment'][week]:
                badge = get_badge_html(task_name, student[task_name], task_info)
                increments.append(badge)
        
        # Process Admin tasks
        for week in sorted(sorted_tasks['Admin'].keys()):
            for task_name, task_info in sorted_tasks['Admin'][week]:
                # Debug print for JAR released task
                if task_name == 'JAR released':
                    print(f"\nProcessing JAR released for student {student['Student ID']}:")
                    print(f"  Value in CSV: {student[task_name]}")
                
                badge = get_badge_html(task_name, student[task_name], task_info)
                admin_tasks.append(badge)
        
        # Combine all sections into one row
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