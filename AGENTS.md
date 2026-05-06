Quick facts (what an automated agent would otherwise miss)

- Entrypoint: app.py — the Flask app is started with `python app.py` and binds to 0.0.0.0:8000 (app.run(..., port=8000, debug=True)).
- Do not assume PORT env var is respected: app.py contains commented code referencing `os.environ.get("PORT")`, but it is not used. The included Procfile (`web: python app.py`) will therefore not work on platforms (e.g. Heroku) that require binding to the $PORT env var until app.py is changed.
- Data is in-memory only: models/todo.py implements a linked-list in memory. Restarting the process clears all tasks. There is no database or persistence layer.
- Routes (useful when adding tests or making requests):
  - GET / -> index (renders templates/index.html)
  - POST /agregar -> agregar (expects form fields `titulo` and `descripcion`)
  - POST /completar -> completar (expects form field `descripcion`)
  - POST /eliminar -> eliminar (expects form field `descripcion`)
- Templates and static files: templates/ contains the Jinja2 templates; static/ contains assets. Controllers render templates via render_template.

Developer commands (exact)

- Create & activate a venv (the README uses `.venv`):
  - python3 -m venv .venv
  - source .venv/bin/activate
- Install dependencies:
  - pip install -r requirements.txt
  - or `pip install flask` (requirements.txt only contains `flask`).
- Run dev server (as the repo expects):
  - python3 app.py
  - The app will be available at http://localhost:8000

Repo hygiene / gotchas

- .venv is gitignored (.gitignore) — do not add the virtualenv to the repo.
- There are no tests, CI configs, or linters in the repo. Don’t try to run pytest or assume a test runner exists.
- If you plan to deploy to a platform that requires binding to $PORT (Heroku, some PaaS), update app.py to read PORT from the environment or use gunicorn. The file already contains a commented snippet showing how to use `os.environ.get("PORT")`.

When inspecting code to make edits

- Start at app.py to understand routing and server configuration, then check controllers/home_controller.py (wiring) and models/todo.py (business logic / in-memory store).
- Prefer editing controllers for request/response behaviour and models for data logic. Templates are in templates/.

If something is missing

- The repo contains no tests or CI; if you need test targets or CI config, add them explicitly — nothing here will run automatically.
