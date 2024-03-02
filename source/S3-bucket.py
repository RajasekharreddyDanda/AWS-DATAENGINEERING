import boto3    
import os, sys
import csv
import pandas as pd

#read s3 bucket  and get the list of files in it
#read each file one by one and process them
#write  back to S3 with a new filename (e.g., add _processed suffix)
# s3 connection
                                                                                          
aws_access_key_id = 'AKIA5FTZC5JYVZYTHLRF'
aws_secret_access_key = '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'
region_name = 'ap-south-1'

#source and destination s3 bucket name
source_bucket_name = 'raj-aws-de'
destination_bucket_name =  'raj-aws-de-dest'
source_file_key = 'creditcard.csv'

# Create S3 client
try:
    s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=region_name)
# Read file from source S3 bucket
    response = s3.get_object(Bucket=source_bucket_name, Key=source_file_key)
    file_content = response['Body'].read().decode('utf-8')
# read file_content into pandas
except Exception as e:
    print(f"An error occurred: {str(e)}")    
sys.exit()
# read file_content into pandas and print 30 records

#df = pd.read_csv(StringIO(file_content)) # convert string content to dataframe object
#print("Dataframe created successfully.")
#print(df)






