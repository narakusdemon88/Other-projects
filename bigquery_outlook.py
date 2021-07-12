# Run this first
# export GOOGLE_APPLICATION_CREDENTIALS=/mnt/c/Users/YOUR_USER_NAME/creds.json

import datetime as dt
import logging

import win32com.client
from google.cloud import bigquery
from google.cloud import bigquery_storage_v1beta1

const=win32com.client.constants

outlook = win32com.client.Dispatch("Outlook.Application").GetNameSpace("MAPI")

# Set up for logging
logging.basicConfig(
  filename='output.log',
  level = logging.INFO,
  format='%(asctime)s:%(levelname)s:%(message)s')

# example: July 4, 1776 = 07-04-1776
today = dt.datetime.today().strftime('%m-%d-%Y')

def extract_data():
  try:
    # Connect to BigQuery API
    bqclient = bigquery.Client()

    bqstorageclient = bigquery_storage_v1beta1.BigQueryStorageClient()
    logging.info('BigQuery successfully authenticated')

  except:
    logging.info('BigQuery authentication unsuccessful')

  # Actual query is here.
  query_string = """
  SELECT
    *
  FROM
    DATABASE.TABLE_NAME
  """
  try:
    # Create a pandas dataframe
    dataframe = (
        bqclient.query(query_string)
        .result()
        .to_dataframe(bqstorage_client=bqstorageclient)
    )

  except:
    logging.log('Could not successfully extract data')

  dataframe.to_csv(today + '_report.csv', index=False)

  logging.log('Query extracted successfully')


def send_mail():

  olMailItem = 0x0
  obj = win32com.client.Dispatch("Outlook.Application")
  newMail = obj.CreateItem(olMailItem)
  newMail.Subject = "Identification Daily report"

  newMail.To = 'RECEIVERS_EMAIL@EMAIL.COM'
  attachment = 'PATH' + today + '_report.csv'

  newMail.Body =  'Dear receiver,'+\
                  '\n'+'This email reports things.'+\
                  '\n'+'This email was sent automatically using Python.'
  newMail.Attachments.Add(Source=attachment)
  newMail.display()
  newMail.Send()

if __name__ == "__main__":
  extract_data()
  send_mail()
