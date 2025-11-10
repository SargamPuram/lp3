General Setup & Environment Commands
Check Python version
python3 --version

Check installed packages
pip3 list

Upgrade pip locally (if allowed)
python3 -m pip install --upgrade --user pip

Install packages locally without root (avoids global conflicts)
pip3 install --user package_name

Virtual environments (isolated Python env)
Create: python3 -m venv myenv
Activate: source myenv/bin/activate (then deactivate to exit)
Use virtual envs to prevent dependency clash on shared systems.

Installing Packages (sometimes require user flag)
pip3 install --user pandas numpy matplotlib seaborn scikit-learn

If pip or Python3 missing, try:
sudo apt-get install python3-pip (may not be allowed)

List packages in Jupyter notebook cell if you can’t install externally:
!pip install pandas numpy scikit-learn

File and Directory Management
ls -ltr : list files with details and sort by time (most recent last)

pwd : current directory

cd path : change directory

mkdir foldername : create folder

cp file1 file2 : copy files

rm filename : remove file

rm -r foldername : remove directory recursively

Running Jupyter Notebooks
Start Jupyter if installed:
jupyter notebook --no-browser --port=8888
Then open browser with displayed URL (e.g., http://localhost:8888)

Run notebook cells step-wise and see outputs

Restart kernel if environment seems off via notebook UI

Useful Python commands inside Notebook
Check versions inside notebook:

python
import sys
print(sys.version)
import pandas as pd
print(pd.__version__)
Check installed packages:

python
!pip list
Debugging & Logs
If errors on module loading (like sklearn), check installed versions & reinstall if possible

If old Python version, use compatible package versions or ask instructor for help

Summary:
Use virtual environments to isolate dependencies. Use pip install --user to avoid permission issues. Keep track of where your notebook is running and files are stored. Debug any import or version issues early.

This command list will help you smoothly run your ML practicals despite college system limitations.

If you want, I can also give you a tailored bash script snippet to automate environment setup tomorrow!