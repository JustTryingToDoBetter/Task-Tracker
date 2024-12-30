##Add, Update, and Delete tasks
##Mark a task as in progress or done
#List all tasks
#List all tasks that are done
#List all tasks that are not done
#List all tasks that are in progress
## lets get this breada

import argparse
import json
from datetime import datetime

task_file = "tasks.json"

def load_tasks():
    try:
        with open(task_file, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(task_file, "w") as file:
        json.dump(tasks, file, indent=4)

def addTask (title):
    tasks = load_tasks()
    tasks.append({
        "id" : len(tasks) + 1,
         "title" : title, 
         "finished" :  False,
         "in Progress": True,
         "createdAt" : datetime.now().isoformat()
         })
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def deleteTask(title):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == title:
            del task["title"]

    save_tasks(tasks)
    print(f"Task {title} has been removed")

def updateTask(title):
    tasks = load_tasks()
    for task in tasks:
        if task["title"] == title:
            tasks.append({
                "id" : tasks[title], 
                "title" : title, 
                "finished" : True,
                "in Progress" : False, 
                "updatedAt" : datetime.now().isoformat()
            })

    save_tasks(tasks)
    print(f"task{title} has been updated")

def listTasks():
    tasks = load_tasks()
    if tasks == None:
        print("no tasks")
    for task in tasks:
        print(task)

def completedTasks():
    tasks = load_tasks()

    for task in tasks:
        if task["finished"]:
            print(task["title"])

def IncompleteTasks():
    tasks = load_tasks()

    for task in tasks:
        if not task["finished"]:
            print(task["title"])


def inProgress():
    tasks = load_tasks()

    for task in tasks:
        if task["in Progress"]:
            print(task["title"])

    

def main():
    parser = argparse.ArgumentParser(description="Task Tracker CLI")
    parser.add_argument("command", choices=["add", "listAll", "checkCompleted", "delete", "update", "checkInProgress", "checkIncomplete"], help="Command to execute")
    parser.add_argument("--title", type=str, help="Title of the task to add/update/delete")
    
    args = parser.parse_args()

    if args.command == "add":
        if not args.title:
            print("Error: --title is required for adding a task.")
        else:
            addTask(args.title)
    elif args.command == "listAll":
        listTasks()
    elif args.command == "checkCompleted":
        completedTasks()
    elif args.command == "delete":
        if not args.title:
            print("Error: --title is required for deleting a task.")
        else:
            deleteTask(args.title)
    elif args.command == "checkIncomplete":
        IncompleteTasks()
    elif args.command == "update":
        if not args.title:
            print("Error: --title is required for updating a task.")
        else:
            updateTask(args.title)
    elif args.command == "checkInProgress":
        inProgress()

if __name__ == "__main__":
    main()


    

