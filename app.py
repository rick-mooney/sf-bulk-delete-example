from salesforce_bulk import SalesforceBulk
from salesforce_bulk import CsvDictsAdapter
import os
import time
import unicodecsv


bulk = SalesforceBulk(username=os.environ.get('USER'), password=os.environ.get('PW'), 
                    security_token=os.environ.get('TOKEN'), domain='test')
print('Authenticated')

def delete_records():
    bulk.create_delete_job('ContentVersion', contentType='CSV')


def query_and_delete(obj, query=None):
    print('running query')
    query_job = bulk.create_query_job(obj, contentType='CSV')
    if not query:
        query = 'select Id from %s order by createddate desc limit 5000' % obj
    query_batch = bulk.query(query_job, query)
    bulk.close_job(query_job)
    while not bulk.is_batch_done(query_batch):
        time.sleep(3)

    delete_job = bulk.create_delete_job(obj, contentType='CSV')
    results = bulk.get_all_results_for_query_batch(query_batch)
    print('recieved results')
    for result in results:
        print('deleting records')
        delete_batch = bulk.post_batch(delete_job, result)
        bulk.wait_for_batch(delete_job, delete_batch)
        print('delete job complete')
    bulk.close_job(delete_job)

if __name__ == '__main__':
    for x in range(10):
        print('running job %s' % x)
        query_and_delete('EmailMessage')
        query_and_delete('select Id from ContentVersion order by contentsize desc limit 5000')
