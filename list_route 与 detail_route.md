## detail_route 与 list_route 的区别(好像还有点问题)

> Django rest framework 提供的两种自定义ViewSet() 的两种方法

### detail_route

参数中包含PK，类似于retrieve()

```python
@detail_route(methods=['get'])
def custom_handler(self,request):
    pass
```

### list_route

参数中不带PK， 类似于list()


```python    
@list_route(methods=['get'])
def custom_handler(self,request,pk=None):
    pass
```
