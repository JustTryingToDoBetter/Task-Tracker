# Task-Tracker


A simple command-line interface (CLI) application for managing your tasks. Built with Python, this tool helps you organize, track, and manage your to-do list directly from the terminal.

## Features

- ✅ Add new tasks
- 🗑️ Delete tasks
- ✏️ Update task status
- 📋 List all tasks
- ✔️ View completed tasks
- ❌ View incomplete tasks
- 🔄 Track tasks in progress

## Requirements

- Python 3.x
- No external dependencies required (uses only Python standard library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/JustTryingToDoBetter/Task-Tracker.git
cd Task-Tracker
```

2. Ensure Python 3 is installed:
```bash
python3 --version
```

That's it! The application is ready to use.

## Usage

The Task Tracker CLI accepts various commands to manage your tasks. All tasks are stored in a `tasks.json` file in the same directory.

### Basic Syntax

```bash
python3 taskTracker.py <command> [--title "Task title"]
```

### Available Commands

#### Add a Task
Add a new task to your list. New tasks are automatically marked as "in progress".

```bash
python3 taskTracker.py add --title "Complete project documentation"
```

#### List All Tasks
Display all tasks with their details (ID, title, status, creation date).

```bash
python3 taskTracker.py listAll
```

#### Delete a Task
Remove a task from your list by title.

```bash
python3 taskTracker.py delete --title "Complete project documentation"
```

#### Update a Task
Mark a task as completed (sets finished to true and in progress to false).

```bash
python3 taskTracker.py update --title "Complete project documentation"
```

#### Check Completed Tasks
View only the tasks that have been marked as completed.

```bash
python3 taskTracker.py checkCompleted
```

#### Check Incomplete Tasks
View all tasks that are not yet completed.

```bash
python3 taskTracker.py checkIncomplete
```

#### Check Tasks In Progress
View all tasks that are currently in progress.

```bash
python3 taskTracker.py checkInProgress
```

### Get Help

To see all available commands and options:

```bash
python3 taskTracker.py --help
```

## Task Data Structure

Tasks are stored in `tasks.json` with the following structure:

```json
[
    {
        "id": 1,
        "title": "Task title",
        "finished": false,
        "in Progress": true,
        "createdAt": "2024-12-30T14:39:38.278313"
    }
]
```

### Task Properties

- **id**: Unique identifier for the task (auto-generated)
- **title**: Description of the task
- **finished**: Boolean indicating if the task is completed
- **in Progress**: Boolean indicating if the task is currently being worked on
- **createdAt**: ISO format timestamp of when the task was created
- **updatedAt**: ISO format timestamp of when the task was last updated (added on update)

## Examples

Here's a typical workflow:

```bash
# Add some tasks
python3 taskTracker.py add --title "Write README"
python3 taskTracker.py add --title "Fix bugs"
python3 taskTracker.py add --title "Deploy application"

# List all tasks
python3 taskTracker.py listAll

# Mark a task as completed
python3 taskTracker.py update --title "Write README"

# Check what's completed
python3 taskTracker.py checkCompleted

# Check what's still in progress
python3 taskTracker.py checkInProgress

# Delete a task
python3 taskTracker.py delete --title "Fix bugs"
```

## File Structure

```
Task-Tracker/
├── taskTracker.py    # Main application file
├── tasks.json        # Task storage (auto-generated)
└── README.md         # This file
```

## Contributing

Feel free to fork this repository and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available for anyone to use and modify.

## Project Origin

This project was inspired by the roadmap.sh Task Tracker project idea.

---

Made with ❤️ for better task management
