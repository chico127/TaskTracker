#!/usr/bin/env python3
import argparse, json
from datetime import datetime
from pathlib import Path

VALID_STATUSES = ('todo', 'in-progress', 'done')
DEFAULT_FILE = Path("tasks.json")

def load_tasks(file_path=DEFAULT_FILE):
    if file_path.exists():
        with open(file_path, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks, file_path=DEFAULT_FILE):
    with open(file_path, "w") as f:
        json.dump(tasks, f, indent=2)

def add_task(description, status="todo", file_path=DEFAULT_FILE):
    tasks = load_tasks(file_path)
    new_id = (max([t["id"] for t in tasks]) + 1) if tasks else 1
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": new_id,
        "description": description,
        "status": status,
        "createdAt": now,
        "updatedAt": now,
    }
    tasks.append(new_task)
    save_tasks(tasks, file_path)
    print(f"Added task #{new_id}: '{description}' [{status}]")

def update_task(task_id, status, file_path=DEFAULT_FILE):
    tasks = load_tasks(file_path)
    for t in tasks:
        if t["id"] == task_id:
            t["status"] = status
            t["updatedAt"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks, file_path)
            print(f"Updated task {task_id} to [{status}]")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id, file_path=DEFAULT_FILE):
    tasks = load_tasks(file_path)
    new_tasks = [t for t in tasks if t["id"] != task_id]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
    else:
        save_tasks(new_tasks, file_path)
        print(f"Task {task_id} deleted.")

def list_tasks(status=None, file_path=DEFAULT_FILE):
    tasks = load_tasks(file_path)
    if status == "not-done":
        tasks = [t for t in tasks if t["status"] != "done"]
    elif status:
        tasks = [t for t in tasks if t["status"] == status]

    if not tasks:
        print("(no tasks found)")
        return

    print(f"\n{'ID':<5} {'DESCRIPTION':<30} {'STATUS':<12} {'CREATED':<20} {'UPDATED':<20}")
    print("-" * 95)
    for t in tasks:
        print(f"{t['id']:<5} {t['description']:<30} {t['status']:<12} {t['createdAt']:<20} {t['updatedAt']:<20}")

def main():
    parser = argparse.ArgumentParser(description="Tasks CLI (JSON version).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    add_p = sub.add_parser("add", help="Add new task")
    add_p.add_argument("description")
    add_p.add_argument("--status", choices=VALID_STATUSES, default="todo")

    update_p = sub.add_parser("update", help="Update task")
    update_p.add_argument("id", type=int)
    update_p.add_argument("--status", choices=VALID_STATUSES, required=True)

    del_p = sub.add_parser("delete", help="Delete task")
    del_p.add_argument("id", type=int)

    list_p = sub.add_parser("list", help="List tasks")
    list_p.add_argument("--status", choices=VALID_STATUSES + ("not-done",))

    args = parser.parse_args()

    if args.cmd == "add":
        add_task(args.description, args.status)
    elif args.cmd == "update":
        update_task(args.id, args.status)
    elif args.cmd == "delete":
        delete_task(args.id)
    elif args.cmd == "list":
        list_tasks(args.status)

if __name__ == "__main__":
    main()
