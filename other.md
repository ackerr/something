
## 深浅拷贝



    import copy

    l = [[3,4],3,5]
    a = l  # 完全一样
    b = l.copy()
    c = copy.deepcopy(l)
    d = copy.copy(l) # 等于l.copy()
    
    
### 深拷贝 两个列表互相独立，不受影响 可用id（）查看两个列表是不是一个地址
### 浅拷贝 第一层修改，不受影响，内层修改，同样被修改，例如内嵌列表等，第一层id()不同，内层id（）相同
   
## reduce



## filter




## map


## redis scan 迭代


## 位运算符
~6 = -7

'>> 右移 将值转化为二进制进行移动'

' << 左移'

