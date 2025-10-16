# 📝 Tasks CLI — JSON-based Task Manager

A lightweight command-line task manager written in Python.  
It stores tasks in a simple **JSON file** (`tasks.json`) — no database required.

[https://github.com/chico127/TaskTracker](https://roadmap.sh/projects/task-tracker)

---

## 🚀 Features

- ✅ Add new tasks with a description and optional status  
- 🔄 Update task status (`todo`, `in-progress`, `done`)  
- 🗑️ Delete tasks by ID  
- 📋 List all tasks, or filter by status (including “not-done”)  
- ⏰ Tracks creation and update timestamps  
- 💾 All data stored locally in `tasks.json`

---

## 🧰 Requirements

- Python **3.8+**
- No external dependencies — uses only the Python standard library (`argparse`, `json`, `datetime`, `pathlib`)

---

## ⚙️ Installation

1. Clone or download this repository.
2. Navigate into the project folder.
3. Verify Python is installed:
   ```bash
   python --version
   ```
4. You’re ready to go!

---

## 🧩 Usage

Run the CLI directly with:

```bash
python tasks.py <command> [options]
```

### Commands

#### ➕ Add a task
```bash
python tasks.py add "Write documentation"
```
or specify a status:
```bash
python tasks.py add "Review pull request" --status in-progress
```

#### ✏️ Update a task’s status
```bash
python tasks.py update 1 --status done
```

#### 📋 List tasks
List all tasks:
```bash
python tasks.py list
```

List only `in-progress` tasks:
```bash
python tasks.py list --status in-progress
```

List all tasks that are **not done**:
```bash
python tasks.py list --status not-done
```

#### 🗑️ Delete a task
```bash
python tasks.py delete 3
```

---

## 🧠 Example CLI Session

Here’s an example of what using this app looks like in your terminal:

```bash
$ python tasks.py add "Write documentation"
✅ Added task #1: 'Write documentation' [todo]

$ python tasks.py add "Review PR" --status in-progress
✅ Added task #2: 'Review PR' [in-progress]

$ python tasks.py list
ID    DESCRIPTION                   STATUS       CREATED              UPDATED
-----------------------------------------------------------------------------------------------
1     Write documentation            todo         2025-10-16 20:00:00  2025-10-16 20:00:00
2     Review PR                      in-progress  2025-10-16 20:05:00  2025-10-16 20:05:00

$ python tasks.py update 1 --status done
✅ Updated task 1 to [done]

$ python tasks.py list --status not-done
ID    DESCRIPTION                   STATUS       CREATED              UPDATED
-----------------------------------------------------------------------------------------------
2     Review PR                      in-progress  2025-10-16 20:05:00  2025-10-16 20:05:00

$ python tasks.py delete 2
🗑️  Task 2 deleted.

$ python tasks.py list
ID    DESCRIPTION                   STATUS       CREATED              UPDATED
-----------------------------------------------------------------------------------------------
1     Write documentation            done         2025-10-16 20:00:00  2025-10-16 20:10:45
```

---

## 🗂️ Data format (`tasks.json`)

Tasks are stored in a human-readable JSON file:

```json
[
  {
    "id": 1,
    "description": "Write documentation",
    "status": "done",
    "createdAt": "2025-10-16 20:00:00",
    "updatedAt": "2025-10-16 20:10:45"
  }
]
```

---

## ⚠️ Notes

- The JSON file is rewritten each time you modify tasks — this is expected.  
- All operations are local; no network or server required.  
- IDs are automatically assigned in ascending order.

---

## 🧩 License

This project is open-source.

