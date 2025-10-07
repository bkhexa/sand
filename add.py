import os
import zipfile

# Get the current notebook name (assumes you're running this inside a cell)
try:
    from IPython import get_ipython
    ipython = get_ipython()
    notebook_name = ipython.config['IPKernelApp']['connection_file'].split('/')[-1].replace('json', 'ipynb')
except:
    notebook_name = None  # If not running inside a notebook

# Name of the output ZIP file
zip_filename = "archive_output.zip"

with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for foldername, subfolders, filenames in os.walk('.'):
        for filename in filenames:
            filepath = os.path.join(foldername, filename)
            # Normalize path (remove ./ at the beginning)
            arcname = os.path.relpath(filepath, '.')

            # Skip the notebook itself
            if notebook_name and notebook_name in filepath:
                continue

            # Add to zip
            zipf.write(filepath, arcname)

print(f"Zipped everything (except this notebook) into: {zip_filename}")
