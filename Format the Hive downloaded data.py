#  FullhighriskFinaloutput0407v2

#python utility to format such that deal high risk data is formatted ..dataframe loadable format
import csv 
import pandas

#loan data formatting    

def ReadWriteconfig_file(file,outfile):
   # try:
        file_object = open(file, 'r')
        lines = csv.reader(file_object, delimiter='|', quotechar='"')
        flag = 0
        data=[]
        count = 0
        for line in lines:
            count = count +1
            str1 = "" 
            #print(line)
            #print(count)
            for i in line:
                   
                 
                #print(i)
                str1 += i
                #print("string"+str1)
            if  str1.startswith('+'):
                    flag =1
                    print('inside skip line')
                    continue
            else:
                #convert column with comma as string column for proper formatting
                
                #line[8] ='"'+line[8]+'"'
                #line[4] ='"'+line[4]+'"' 
                    #remove unwanted spaces from column heading row
                if count==2:       
                        line = [x.strip(' ') for x in line]
                        #print(line)
                        data.append(line)
                else:    
                        line= ['"' + item + '"' for item in line]
			data.append(line)  
        file_object.close()
        if flag ==1: #if + line is present in file
            file_object = open(outfile, 'w')
            for line in data:
                     
                    str1 = ''.join(Line)
                    str1 = str1+','
                    print("after"+str1)
                    file_object.write(str1+"\n")
            file_object.close() 
    #except Exception,e:
    #       print e
    
#call procedure to remove format , comma lines    
ReadWriteconfig_file('FullhighriskFinaloutput0407v2.csv','FullhighriskFinaloutput0407v2-formattedv4.csv')  

