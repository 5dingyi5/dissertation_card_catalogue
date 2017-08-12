import re
import os

#copy all filename in folder
for filename in os.listdir("OCR_Original"): 
    #create file path 'folder_name/file_name'
    with open(os.path.join('OCR_Original/', filename), "r") as subj: 
        text = subj.read()
        #regex expression
        regex = re.compile(r'(\b[2|3]\. {1,3}[\w| |\(|\)|\']+)')
        output = regex.findall(text)
        print(output) #display output for troubleshooting purposes
        out_str = ",".join(output)
        with open("original_subj.csv", "a") as output:
            output.write(filename + "," + out_str + "\n")
            #write file with 'file_name, results1, results2, \n' for csv format