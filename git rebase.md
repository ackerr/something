> 随便放一下

多人开发时，在功能开完完毕准备提pr时，一般远端库也会有所更新，这个时候正常流程就是去拉取最新的代码。

1.git pull 

pull 操作简单粗暴，不讲道理，直接将远端代码拉取合并到本地，实际上pull 是fetch + merge 二合一的操作

2.git fetch + git merge



3.git fetch + git rebase





```shell
$ git fetch origin master
$ git log -p master..origin/master
$ git merge origin/master
```



这个时候如果有人一样修改某段代码，可能就需要手动的解决冲突了(这步貌似是避免不了的了，除非事先沟通好)。

##### 记一个正常流程

#### git fetch

#### git merge

#### git rebase 

- git  rebase --continue
- git rebase --abort
- git rebase --skip

`git rebase --help`



##### rebase 的骚操作

- git rebase -i   commit_hash

- 
