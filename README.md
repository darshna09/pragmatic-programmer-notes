# pragmatic-programmer-notes
Chapter-wise notes, code snippets, and practical insights from "The Pragmatic Programmer", maintained as a long-term reference for better engineering habits.

## Development Setup

1. Ensure correct Python version: `pyenv local 3.14.2`
2. Enter virtual environment: `source .venv/bin/activate`
    Note: If virtual environment is not there: `python -m venv .venv`
3. Install dependencies: `pip install -r requirements.txt`

**Running the code snippets**

```bash
python src/pragmatic/<topic>/<file_name>.py
```

**Add New Dependencies**

```bash
pip install <library>
pip freeze > requirements.txt
```
