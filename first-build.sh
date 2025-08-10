uv venv .venv 
uv sync
uv pip install dist/eloApp-0.1.0-py3-none-any.whl
eloapp run_dashboard 