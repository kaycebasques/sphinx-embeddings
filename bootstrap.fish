python3 -m venv venv
. venv/bin/activate.fish
python3 -m pip install -r requirements.txt
cd docs
python3 -m pip install -r requirements.txt
cd ..
deactivate
