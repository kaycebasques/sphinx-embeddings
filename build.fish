. venv/bin/activate.fish
cd docs
if test -d _build; rm -rf _build; end
set SRC_DIR .
set OUT_DIR ./_build
sphinx-build -M html $SRC_DIR $OUT_DIR --fail-on-warning
cd ..
deactivate
