""" 
Author: Joaquín Ballesteros, jballesteros@uma.es
License: GNU General Public License v.3.0.


Description: An easy API rest usage from PubChem. Introduce the list of compound by name in a CSV file and return a CSV file with those names and the property that you select.endswith
1. **Molecular Weight (MW)**: The molecular weight of the compound.
2. **Canonical SMILES**: The Simplified Molecular Input Line Entry System notation for the compound.
3. **InChI**: The International Chemical Identifier for the compound.
4. **XLogP**: Calculated partition coefficient (logP) of the compound.
5. **Exact Mass**: The exact mass of the compound.
6. **Topological Polar Surface Area (TPSA)**: The polar surface area of the compound.
7. **Number of Hydrogen Bond Donors**: The count of hydrogen bond donor atoms in the compound.
8. **Number of Hydrogen Bond Acceptors**: The count of hydrogen bond acceptor atoms in the compound.
9. **Rotatable Bond Count**: The count of rotatable bonds in the compound.
10. **Complexity (Molecular Complexity)**: A measure of the structural complexity of the compound.
11. **Isomeric SMILES**: SMILES notation that accounts for isomerism.
12. **InChIKey**: A hashed version of the InChI, often used as a unique identifier for compounds.
13. **Covalent Unit Count**: The count of covalently bound units in a polymer or oligomer.
14. **Monoisotopic Mass**: The monoisotopic mass of the compound.
15. **Volume3D**: The calculated 3D volume of the compound.
16. **Polarizability**: The polarizability of the compound.
17. **Density**: The density of the compound """

import requests
import pandas as pd
import json
import numpy
import time
import math
import datetime
import signal
import time
import readchar

fLog = None
dataframe=None
saving=False
 
def handler(signum, frame):
    if (not saving):
        msg = "Ctrl-c was pressed. Do you really want to exit? Y/n "
        print(msg, end="", flush=True)
        res = readchar.readchar()
        if res == 'Y':
            fLog.close()
            dataframe.to_excel("input.xlsx", index=False)
            exit(1)
        else:
            print("", end="\r", flush=True)
            print(" " * len(msg), end="", flush=True) # clear the printed line
            print("    ", end="\r", flush=True)
 
 
signal.signal(signal.SIGINT, handler)


def getCID(compound_name):
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/cids/JSON"
    try:
        response = requests.get(search_url)
    except ConnectionError:
        print("Server refuse conection")
        return -2
    except KeyError:
        print("CID not found " + CID)
        return -1

    # connection error
    if response.status_code == 200:
        data = response.json()
        if "IdentifierList" in data:
            cid = data["IdentifierList"]["CID"][0]
            return cid
        else:
            print("Compound not found " + compound_name)
    else:
        print(f"Error: {response.status_code}")
        print("Compound not found " + compound_name)
    return -1


def getByName(compound_name):
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/cids/JSON"
    try:
        time.sleep(0.1)
        response = requests.get(search_url)
    except ConnectionError:
        print("Server refuse conection")
        return -2
    except KeyError:
        print("CID not found " + CID)
        return -1

    # connection error
    if response.status_code == 200:
        data = response.json()
        if "IdentifierList" in data:
            cid = data["IdentifierList"]["CID"][0]
            return cid
        else:
            print("Compound not found " + compound_name)
    else:
        print(f"Error: {response.status_code}")
        print("Compound not found " + compound_name)
    return math.inf


def getXLogP(CID):
    search_url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{CID}/property/XLogP/JSON"
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        if "PropertyTable" in data:
            try:
                prop = data["PropertyTable"]["Properties"][0]["XLogP"]
                return prop
            except KeyError:
                print("XlogP not found for CID" + str(CID))
            except ConnectionError:
                print("Server refuse conection")
                exit()
        else:
            print("XlogP not found " + compound_name)
    else:
        print(f"Error: {response.status_code}")
        print("XlogP not found " + compound_name)
    return math.inf


def getXLogP3_CID(cid):
    time.sleep(0.1)
    prop = getXLogP(cid)
    if prop is not math.inf:
        print("New " + name + " index " + str(index))
        return prop
    else:
        print("Not found and assing inf to " + str(index))
        return math.inf


# read by default 1st sheet of an excel file
dataframe = pd.read_excel("input.xlsx")
fLog = open("log.txt", "a")

now = datetime.datetime.now()
fLog.write("-*************************************-\n")
fLog.write("   New entry "+str(now.strftime("%d-%m-%Y %H:%M:%S")+" \n"))
fLog.write("-*************************************-\n")
# show date in different format

counterFound=0
for index, row in dataframe.iterrows():
    name = str(row["CAS"])
    xlogp = row["XLogP3-AA"]
    if str(name) != "(na)" and str(name) != "na":
        if "(" in name:
            name = name.lstrip("(")
        if ")" in name:
            name = name.rstrip(")")
        # It is not complete
    else:
        name = row["Name"]
    
    if numpy.isnan(row["XLogP3-AA"]):
        if (numpy.isnan(row["CID"])):
            cid = getCID(name)
        else:
            cid = row["CID"]
        if cid >= 0:
            dataframe.at[index, "CID"]=cid
            dataframe.at[index, "XLogP3-AA"] = getXLogP3_CID(cid)
            fLog.write("Assigned " + str(dataframe.at[index, "XLogP3-AA"]) + " to row " + str(index) + " with CAS " + name + " CID found " + str(cid)+ "\n")
            counterFound+=1
        elif cid == -2:
            print("Server refuse connection " + str(index))
            fLog.write("--Server refuse connection " + str(index) + " with CAS " + name + " CID found " + str(cid)+ "\n")
            fLog.close()
            exit()
        else:
            row["CID"]=math.inf
            print("Not found and assing inf to " + str(index))
            fLog.write("**Assigned inf to row " + str(index) + " with CAS " + name + " CID found " + str(cid)+ "\n")
            dataframe.at[index, "XLogP3-AA"] = math.inf

    else:
        print("Already found: " + name + " index " + str(index))
        fLog.write("****Already found. Row " + str(index) + " with CAS " + name+ "\n")
    # Save the modified DataFrame to an Excel file
    saving = True
    dataframe.to_excel("input.xlsx", index=False)
    fLog.flush()
    saving = False
        


fLog.close()
print("Complete! " + str(counterFound) + " compound found in this iteration. Review log.txt to find the errors")
