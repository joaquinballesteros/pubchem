# pubchem
This repository is created to group scripts needed for retrieval information from (PubChem)[https://pubchem.ncbi.nlm.nih.gov].

* ## Download and installation
1. Install [Python 3.9+](https://www.python.org/)
2. Download/Clone this repository and enter it into the main directory. If you are not familiar with Git, just go to the green button code, click on it, and download the zip.
3. Open a terminal, and navigate to a folder where you will install this protect. Then Create a virtual environment: `python -m venv env`
4. Then, activate the environment: 
   
   In Linux or Mac: `source env/bin/activate`

   In Windows: `.\env\Scripts\Activate`

   ** In case you are running Ubuntu, please install the package python3-dev with the command `sudo apt update && sudo apt install python3-dev` and update wheel and setuptools with the command `pip  install --upgrade pip wheel setuptools` right after step 4.
   
5. Install the dependencies in the terminal: `pip install -r requirements.txt`

* ## How to use it!
1. Please include in the same folder a file called **input.xlsx**; see the attached template.
2. Open a terminal and activate the enviroment.
   
   In Linux or Mac: `source env/bin/activate`

   In Windows: `.\env\Scripts\Activate`

3. Run the script in the terminal. 
   `python readProperty.py`
4. It will show you the components that were found and the ones that were not. During this process, it will overwrite in the **input.xlsl** file. If the PubChem cut or you lost the connection, you will have the information found at **input.xlsl**. You just need to rerun again, it will save the current progress.

* ## Troubleshooting
* Python not found: If you are windows system, please add the program to the path. [How to do that](https://medium.com/@viknesh2798/how-to-fix-the-issues-while-using-python-command-in-the-command-prompt-ba56d9018c5f)
* Enviroment can not be activated: Please check that you are in the folder that you created the enviroment. 
  
