### 如何合并commit

> git rebase -i (某个commit hash)

```python
p, pick = use commit
r, reword = use commit, but edit the commit message
e, edit = use commit, but stop for amending
s, squash = use commit, but meld into previous commit  (保留修改，向前合并commit)
f, fixup = like "squash", but discard this commit's log message
x, exec = run command (the rest of the line) using shell
d, drop = remove commit (直接将修改弹出，撤销commit)
```

> 注意事项

- 合并是向前合并，所以最早的commit不能为squash
- 找一个合适的commit hash,这个commit hash 不会为包含在修改内容中


### 将commit 撤回，并保留修改

- git reset (commit hash) --soft
- git reset --hard (commit hash) 直接回退到此版本，修改不保留
- git reset HEAD .       撤销暂存区 中的内容
- git reset HEAD - file  撤销暂存区中某个文件的修改

### 暂存修改 stash

- git stash  (保存修改)
- git stash list (查看stash list)
- git stash pop XXX (清除某个stash,恢复修改)
- git stash drop XXX (删除某个stash)
- git stash show -p  xxx/stash@{0} (查看某个stash的内容)

### 删除分支

- git br -a 查看远程与本地的所有分支
- git br -D [分支] 删除本地分支
- git push origin --delete [远程分支]  删除远程分支 
