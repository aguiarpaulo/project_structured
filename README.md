#My ETL Project
1. Clone the repository:
```bash
git clone https://github.com/aguiarpaulo/project_structured.git

cd project_structured
```
2. Configure the correct Python version with pyenv:
```bash
pyenv install 3.11.3
pyenv local 3.11.3
```
3. Install project dependencies:
poetry install
3. Activate the virtual environment:
poetry shell
3. Run tests to ensure everything is working as expected:
poetry run pytest -v
3. Run the command to view project documentation:
mkdocs serve
3. Run the pipeline run command to perform ETL:
python3 app/main.py
3. Check in the data/output folder if the file was generated correctly.
Contact:
Paulo Aguiar - aguiarlapaulo@gmail.com
