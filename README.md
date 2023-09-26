# pubchem
This repository is created to group scripts needed for retrieval information from (PubChem)[https://pubchem.ncbi.nlm.nih.gov].

* ## Download and installation
1. Install [Python 3.9+](https://www.python.org/)
2. Download/Clone this repository and enter it into the main directory.
3. Create a virtual environment: `python -m venv env`
4. Activate the environment: 
   
   In Linux or Mac: `source env/bin/activate`

   In Windows: `.\env\Scripts\Activate`

   ** In case you are running Ubuntu, please install the package python3-dev with the command `sudo apt update && sudo apt install python3-dev` and update wheel and setuptools with the command `pip  install --upgrade pip wheel setuptools` right after step 4.
   
5. Install the dependencies: `pip install -r requirements.txt`

* ## How to use it!
1. Please include in the same folder a file called **input.xlsx** from the TimsTOF machine; it should consist of a column called CAS with its value encoded with parentheses.
2. Open a terminal and activate the enviroment.
   
   In Linux or Mac: `source env/bin/activate`

   In Windows: `.\env\Scripts\Activate`

3. Run the script. I will show you the components that were found and the ones that were not. During this process, it will save in the **output.xlsl** file.
4. If the PubChem cut or you lost the connection, you will have the information found at **output.xlsl**. You can rename it to **input.xlsx** and start the process again, keeping all the compounds you already found.
  
