import csv 
import argparse
import requests 
from bs4 import BeautifulSoup as bs



def savefile(s3name,urls):
  for url in urls:
    curl=s3name+'/'+url
    resp = requests.get(curl)
    f=open(url.split('/')[-1],'wb')
    f.write(resp.content)
    f.close()














def load(s3name): 

    url = s3name
    resp = requests.get(url)
    soup=bs(resp.content,'xml')
    x=soup.find_all('Contents')
    metadata=[]
    urls=[]
    i=0
    for e in x:
      datarow={}
      k=e.find('Key').get_text()
      lm=e.find('LastModified').get_text()
      s=e.find('Size').get_text()
      urls.append(k)
      datarow['Key']=k
      datarow['LastModified']=lm
      datarow['Size']=s
      print(i,s3name+'/'+k)
      i+=1 
      metadata.append(datarow)
    return metadata,urls


def savetoCSV(metadata, filename): 

  
  fields = ['Key', 'LastModified', 'Size'] 

   
  with open(filename+'.csv', 'w') as csvfile: 

    
    writer = csv.DictWriter(csvfile, fieldnames = fields) 

     
    writer.writeheader() 

     
    writer.writerows(metadata) 

  
def main(): 
  my_parser = argparse.ArgumentParser()
  my_parser.add_argument('-u','--url', action='store',  required=True,help='url of S3 e.g. https://s3.ap-south-1.amazonaws.com/S3name/')
  my_parser.add_argument('-c','--csv', action='store_true',help='Save in csv format')
  my_parser.add_argument('-o','--output', action='store_true',help='Download All files in local Systems')
  args = my_parser.parse_args()
  s3name=args.url
  if(s3name[-1]=='/'):s3name=s3name[:-1]
  metadata,urls=load(s3name) 

  if args.csv:
    filename=s3name.split('/')[-1]
    savetoCSV(metadata, filename)
  if args.output:
    savefile(s3name,urls)
  
  
if __name__ == "__main__": 

  # calling main function 
  main() 
