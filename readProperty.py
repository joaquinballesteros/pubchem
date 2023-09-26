
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

def getCID(compound_name):
    search_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/name/{compound_name}/cids/JSON'
    response = requests.get(search_url)
    #connection error
    if response.status_code == 200:
        data = response.json()
        if 'IdentifierList' in data:
            try:
                cid = data['IdentifierList']['CID'][0]
                return cid
            except(KeyError):
                    print('CID not found ' + CID)
            except(ConnectionError):
                print('Server refuse conection')
                exit()
        else:
            print('Compound not found ' + compound_name)
    else:
        print(f'Error: {response.status_code}')
        print('Compound not found ' + compound_name)
    return -1

def getXLogP(CID):
    search_url = f'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{CID}/property/XLogP/JSON'
    response = requests.get(search_url)
    if response.status_code == 200:
        data = response.json()
        if 'PropertyTable' in data:
            try:
                prop = data["PropertyTable"]["Properties"][0]["XLogP"]
                return prop
            except(KeyError):
                print('XlogP not found for CID' + str(CID))
            except(ConnectionError):
                print('Server refuse conection')
                exit()
        else:
            print('XlogP not found ' + compound_name)
    else:
        print(f'Error: {response.status_code}')
        print('XlogP not found ' + compound_name)
    return -1

# read by default 1st sheet of an excel file
dataframe = pd.read_excel('input.xlsx')
print(dataframe)

for index, row in dataframe.iterrows():
    name = row['CAS']
    if str(name)!='nan':
        if "(" in name:
            name = name.lstrip('(')
        if ")" in name:
            name = name.rstrip(')')

        xlogp = row['XLogP3-AA']

        #It is not complete
        if (numpy.isnan(row['XLogP3-AA']) and name!="na"):
            cid = getCID(name)
            if (cid>=0):
                time.sleep(1)
                prop=getXLogP(cid)
                if (prop>0):
                    time.sleep(1)
                    dataframe.at[index, 'XLogP3-AA'] = prop
                    print("New " + name + " index " + str(index))
                else:
                    dataframe.at[index, 'XLogP3-AA'] = -1
                    print("Not found and assing -1 to " + name)
            else:
                dataframe.at[index, 'XLogP3-AA'] = -1
                print("Not found and assing -1 to " + name)
            
        else:
            print("Already founded: " + name + " index " + str(index))
        # Save the modified DataFrame to an Excel file
        dataframe.to_excel('input.xlsx', index=False)
    else:
        print('Compound empty field CAS ')







 
print(dataframe)




