# Overview
This script is a wrapper around the sf_bulk package that will query and delete data from salesforce.  The use case here is if you are over on your storage and have some old legacy data youve either already backed up or just dont care about any more.  Additionally, if you are over your storage in production and have a full sandbox, you wont be able to create any data in the sandbox until you get back under the data and file storage limits.  The example code has two common methods: deteling an object and deleting files (ContentVersions).

# Setup

1. create a `.env` file with your salesforce username, password, and token
2. install [salesforce_bulk](https://github.com/heroku/salesforce-bulk): `pip install salesforce_bulk`
3. Adjust the calls to the `query_and_delete` function per your requirements.
4. run the script

# Known Issues
1. We're blinding setting a limit of 5000 records per batch due to salesforce limits. If you run into errors, you can try dropping the limit
2. There are definitely better ways of batch handling and multithreading but this is a quick and dirty hack.  You can mock multi threading but opening multiple terminals and running the script to speed things up a bit
