

import os # this syntax only works for MacOS. Please ask me for windows or Linux 
from os import path 

def rename (directory):
    conditions = os.listdir(directory)
    for cond in conditions:
        if True :
            os.mkdir('20231106_092346_PB22point7_mTmG_GFP-TJP1_Per1 gRNA Set2 KO_2'+'/'+cond)
            if os.path.isdir(directory+'/'+cond):
                timepoints= os.listdir(directory+'/'+cond)
                for timep in timepoints:
                    if timep[-3:] == 'tif' and timep[0:1]!= '.': #Some weird files appear sometimes 
                        oldname = timep
                        oldnb = timep[1:5]
                        if (timep[3] == 0):
                            nt = 75 + int(timep[4])
                            newnb = '00'+nt 
                        else :
                            
                            nt = 75 + int(timep[3:5])
                            if nt < 100 :
                                newnb = '00'+str(nt) #a better way to do it must exist if you encode numbers differently 
                                                     #allowing the 0 in first position 
                            else :
                                newnb = '0'+str(nt)
                            print (newnb)
                        newname = 't'+str(newnb)+oldname[5:]    

                        #print(oldname, newname)              
                    
                        os.rename (directory+'/'+cond+'/'+oldname , '20231106_092346_PB22point7_mTmG_GFP-TJP1_Per1 gRNA Set2 KO_2'+'/'+cond+'/'+newname)
                        
rename('20231106_092346_PB22point7_mTmG_GFP-TJP1_Per1 gRNA Set2 KO')