# S3Hunter
Download All Files From misconfigured s3 



         usage: python3 s3hunter.py [-h] -u URL [-csv] [-o]
         
         Mandotary arguments:
         
          -u URL, --url URL  url of S3 e.g. https://s3.ap-
                             south-1.amazonaws.com/S3name/
         
         optional arguments:
          -h, --help         show this help message and exit
         
          -c, --csv          Save in csv format FileName,LastModified,Size 
          -o, --output       Download All files in local System


## Installation



              git clone https://github.com/rizwansoaib/S3Hunter.git
              cd S3Hunter
              pip3 install -r requirements.txt
              python3 s3hunter.py -u s3url 
             
              
  ## Example
  
               python3 s3hunter.py -u https://pys3hunter.s3.ap-south-1.amazonaws.com/ -c -o

                
   **-o:    Download All files**
   **-c:    Build Dataset with File Name,LastModified,Size**

          
