rebuild-venv:
	@echo ">>> Suppression de l'ancien venv..."
	rm -rf .venv
	@echo ">>> Création d'un nouveau venv..."
	python -m venv .venv
	@echo ">>> Upgrade de pip..."
	.venv/bin/pip install --upgrade pip
	@echo ">>> Installation des dépendances communes..."
	.venv/bin/pip install -r requirements.txt



# ----------------------------------
#         HEROKU COMMANDS
# ----------------------------------

streamlit:
	-@streamlit run app.py


# ----------------------------------
#    LOCAL INSTALL COMMANDS
# ----------------------------------
install:
	@pip install . -U

clean:
	@rm -fr */__pycache__
	@rm -fr __init__.py
	@rm -fr build
	@rm -fr dist
	@rm -fr *.dist-info
	@rm -fr *.egg-info
	-@rm model.joblib
