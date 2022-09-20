# BIDS Converter

Docker container component to convert neuroimaging data to Brain Imaging Data Structure (BIDS)

## Step 1: 
- Clone this repository 
- Checkout submodules:
  - `git submodule update --recursive --init`
- build the image: `docker build . -t bids-tools`

## Test
- `cd test`
- run `./run_tests.sh`

## Methods

### Dataset

#### db.get  
Get a dataset with all fields, participants, and existing entities 
- [see test/db_get.bats](test/db_get.bats)


#### db.create  
Create a new BIDS dataset
- [see test/db_create.bats](test/db_create.bats)


## Participant

#### sub.import  
Import and update participant into an existing BIDS dataset  
- [see test/sub_import.bats](test/sub_import.bats)

#### sub.get  
Get a participan data from a dataset

- [see test/sub_get.bats](test/sub_get.bats)

#### sub.delete  
Remove a participant from a given BIDS dataset

- [see test/sub_delete.bats](test/sub_delete.bats)

#### sub.delete.file  
Remove data file(s) from a BIDS dataset

- [see test/sub_delete_file.bats](test/sub_delete_file.bats)