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
dev

## git@github.com usage
first an ssh-key has to be generated
```ssh-keygen -t rsa -b 4096 -C "<EMAIL>"
eval $(ssh-agent -s)
ssh-add ~/.ssh/id_rsa
```

after that the ~/.ssh/id_rsa.pub content has to be pasted to github SSH settings