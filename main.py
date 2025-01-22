import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
import json

# Load the configuration from a file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Access paths from the configuration
web_scrapping_path = config["notebooks"]["web_scrapping"]
analise_noticias_pt_path = config["notebooks"]["analise_noticias_pt_pt"]

# Function to run jupyter notebooks
def run_notebook(notebook_path):
    # Load the notebook
    with open(notebook_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Setup the ExecutePreprocessor
    ep = ExecutePreprocessor(timeout=600, kernel_name="python3")

    # Execute the notebook
    try:
        ep.preprocess(nb, {"metadata": {"path": "./"}})  # Adjust this path as needed
    except Exception as e:
        msg = "Error executing the notebook '%s'.\n\n" % notebook_path
        msg += "See notebook '%s' for the traceback." % notebook_path
        print(msg)
        raise
    finally:
        # Save the executed notebook
        with open(notebook_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)

# Paths to your notebooks
notebook1 = web_scrapping_path
notebook2 = analise_noticias_pt_path

# Run the notebooks
run_notebook(notebook1)
run_notebook(notebook2)
