. venv/bin/activate.fish
cd docs
set SRC_DIR .
set OUT_DIR ./_build
sphinx-build -M html $SRC_DIR $OUT_DIR --fail-on-warning
cd ..
deactivate
