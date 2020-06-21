# matask_maker
The App should randomly create new mathmatic tasks for 1-4 class kids

## Dependencies
git
python3
python3-devel


## good to have
jq

## branches
master
int
dev

## git@github.com usage
first an ssh-key has to be generated
```ssh-keygen -t rsa -b 4096 -C "<EMAIL>"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

after that the ~/.ssh/id_rsa.pub content has to be pasted to github SSH settings


### CURL command
`curl -X PUT "http://3.125.113.0:8000/items/78" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"name\":\"toaster\",\"is_offer\":true}"`

### Background task
should be used with asyncio
example:
```asyncio def create_item(...background_tasks: BackgroundTasks...):
    pass
```

***asyncio has to be installed with pip if you use python 3.6
Try to install python 3.7 as you install python3
***


## Tutorial
https://www.youtube.com/watch?v=5GorMC2lPpk
