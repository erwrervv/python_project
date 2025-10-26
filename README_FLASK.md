# Flask starter

This is a minimal Flask starter added to the repository.

Quick start (Windows PowerShell):

1. Create a virtual environment (optional but recommended):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Run the app (two options):

Option A — run the package-style entry (uses `run.py`):

```powershell
python run.py
```

Option B — run the new top-level entrypoint (recommended for this example):

```powershell
python app.py
```

4. Run tests:

```powershell
pytest -q
```
