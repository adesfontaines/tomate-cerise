# Tomate Cerise

Plateforme de réservation de paniers de légumes en circuit court.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Lancer l'API

```bash
uvicorn app.main:app --reload
```

## Tests

```bash
pytest -q
```
