
## 深浅拷贝



    import copy

    l = [[3,4],3,5]
    a = l
    b = l.copy()
    c = copy.deepcopy(l)
    d = copy.copy(l) # 等于l.copy()
    
    
### 深拷贝 两个列表互相独立，不受影响
### 浅拷贝 第一层不受影响，内层修改，同样被修改，例如内嵌列表等
   
## reduce



## filter




## map
