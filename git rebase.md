多人开发时，在写好功能准备提pr时，一般远端库也会有更新，这个时候正常流程就是去拉取最新的代码，有冲突也可以早点发现。

先介绍一下两者拉取代码的姿势

#### 1.git pull 

```bash
git pull <远程主机名> <远程分支名>:<本地分支名>
```

pull 操作简单粗暴，直接将远端代码拉取并合并到本地，对，就是这么不讲道理，实际上pull 是 fetch + merge 。

#### 2.git fetch

```bash
git fetch <远程主机名> <远程分支名>:<本地分支名>
```

fetch 是将远端代码全部保存到本地，但此时并没有合并到代码中，而是存放在了.git/FETCH_HEAD文件中

这里肯定就需要提一波FETCH_HEAD了

> FETCH_HEAD指的是: 某个branch在服务器上的最新状态， 每一个执行过fetch操作的项目都会存在一个，FETCH_HEAD列表, 这个列表保存在 `.git/FETCH_HEAD` 文件中，其中每一行对应于远程服务器的一个分支commit_id， 当前分支指向的FETCH_HEAD, 就是这个文件第一行对应的那个分支。

此时如果想要更新本地代码就需要进一步 rebase 或 merge 操作。

fetch操作的优点，可以在合并时，查看一波代码的变化，而不是不讲道德的合并然后解冲突

```shell
git fetch origin master
git diff master..origin/master 
git merge origin/master
```

#### 3.git rebase



#### 4.git merge



















如果有报`CONFLICT (content): Merge conflict in xxxx.py` ，就需要手动解冲突了。

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



# 总结一句：git真好用
