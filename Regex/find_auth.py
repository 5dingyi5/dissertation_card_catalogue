import re
import os

#copy all filename in folder
for filename in os.listdir("OCR_TES"): 
    #create file path 'folder_name/file_name'
    with open(os.path.join('OCR_TES/', filename), "r") as auth: 
        text = auth.read()
        #regex expression
        regex = re.compile(r'(\b[A-Z]{2,} \([\w| |-]+)')
        output = regex.findall(text)
        print(output) #display output for troubleshooting purposes
        out_str = ",".join(output)
        with open("tes_auth.csv", "a") as output:
            output.write(filename + "," + out_str + "\n")
            #write file with 'file_name, results1, results2, \n' for csv format