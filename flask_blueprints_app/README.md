# Flask Blueprints Demo App

A small Flask project demonstrating an application factory and multiple Blueprints.

## Features
- `main` Blueprint for the home page (`/`)
- `blog` Blueprint under `/blog`
- `api` Blueprint under `/api`
- Shared base template with navigation
- Simple pytest test suite

## Project structure
```
flask_blueprints_app/
├── app/
│   ├── __init__.py
│   ├── data.py
│   ├── api/
│   ├── blog/
│   ├── main/
│   └── templates/
├── tests/
│   └── test_app.py
└── run.py
```

## Setup and run
1. Create and activate a virtual environment (optional but recommended).
2. Install dependencies:
   ```bash
   pip install flask pytest
   ```
3. Run the app:
   ```bash
   python run.py
   ```
4. Open `http://127.0.0.1:5000` in your browser.

## Run tests
```bash
pytest
```
