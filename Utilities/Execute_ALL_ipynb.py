import papermill as pm
import os

def execute_notebook(notebook_path, output_path):
    try:
        pm.execute_notebook(
            notebook_path,
            output_path,
            log_output=True
        )
        print(f"Notebook '{notebook_path}' executed successfully.")
    except Exception as e:
        print(f"Error executing notebook '{notebook_path}': {str(e)}")

def execute_all_notebooks(folder_path):
    # Get all files in the folder
    notebook_files = [file for file in os.listdir(folder_path) if file.endswith(".ipynb")]
    print(notebook_files)

    # Execute each notebook
    for notebook_file in notebook_files:
        notebook_path = os.path.join(folder_path, notebook_file)
        output_path = os.path.join(folder_path, f"output_{notebook_file}")
        execute_notebook(notebook_path, output_path)

# Specify the folder containing your Jupyter Notebooks
notebooks_folder = <path of the folder containing .ipynb files>

# Execute all notebooks in the specified folder
execute_all_notebooks(notebooks_folder)
