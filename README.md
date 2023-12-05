#My ETL Project
Clone the repository:
git clone https://github.com/aguiarpaulo/project_structured.git

cd project_structured
Configure the correct Python version with pyenv:
pyenv install 3.11.3
pyenv local 3.11.3
Install project dependencies:
poetry install
Activate the virtual environment:
poetry shell
Run tests to ensure everything is working as expected:
poetry run pytest -v
Run the command to view project documentation:
mkdocs serve
Run the pipeline run command to perform ETL:
python3 app/main.py
Check in the data/output folder if the file was generated correctly.
Contact:
Paulo Aguiar - aguiarlapaulo@gmail.com
