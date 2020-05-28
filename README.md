# S3Hunter
Download All Files From misconfigured s3 

     ```bash

         usage: python3 s3hunter.py [-h] -u URL [-csv] [-o]
         
         Mandotary arguments:
         
          -u URL, --url URL  url of S3 e.g. https://s3.ap-
                             south-1.amazonaws.com/S3name/
         
         optional arguments:
          -h, --help         show this help message and exit
         
          -c, --csv          Save in csv format FileName,LastModified,Size 
          -o, --output       Download All files in local System
          ```


## Installation

 ![installation](https://user-images.githubusercontent.com/29729380/83110425-adf73800-a0e0-11ea-83df-ea3b1f009424.png)



              git clone https://github.com/rizwansoaib/S3Hunter.git
              cd S3Hunter
              pip3 install -r requirements.txt
              python3 s3hunter.py -u s3url 
             
              
  ## Example
  
               python3 s3hunter.py -u https://pys3hunter.s3.ap-south-1.amazonaws.com/ -c -o

                
   **-o:    Download All files**
   
   **-c:    Build Dataset with File Name,LastModified,Size**

          
