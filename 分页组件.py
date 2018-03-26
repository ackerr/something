# 页面分页操作

class Page(object):
    def __init__(self,page,pages,base_url,num=10):
        self.page = page
        self.pages = pages
        self.base_url = base_url
        self.num = num

    def change_num(self):
        pass

    @property
    def start_page(self):
        first = (self.page - 1) * self.num
        return first

    @property
    def end_page(self):
        last = self.page * self.num
        return last

    def total_pages(self):
        m, n = divmod(self.pages, self.num)
        if n != 0:
            m = m + 1
        return m

    def current_page(self):
        m = self.total_pages()
        # 分页设计
        if m <= 5:  # 页码小于11
            start = 1
            end = m
        elif m > 5:  # 页码大于11
            if self.page < 3:  # 当前页码小于6
                start = 1
                end = 5
            else:  # 当前页码大于6
                if m - self.page <= 2:  # 当前页码跟总页码差小于5
                    start = m - 4
                    end = m
                else:  # 当前页码跟总页码差大于5
                    start = self.page - 2
                    end = self.page + 2
        #  动态生成页码标签
        pageer = []

        for i in range(start, end + 1):
            if i == self.page:
                pageer.append('<a href="%s?p=%s" class="page_color">%s</a>' % (self.base_url,i, i))
            else:
                pageer.append('<a href="%s?p=%s">%s</a>' % (self.base_url,i, i))
        pageer.append('<a href="%s?p=%s">%s</a>' % (self.base_url, 1, '首页'))
        if self.page != 1:  # 第一页是不要有上一页
            pageer.append('<a href="%s?p=%s">%s</a>' % (self.base_url,self.page - 1, '上一页'))
        if self.page != m:  # 最后一页时不要有下一页
            pageer.append('<a href="%s?p=%s">%s</a>' % (self.base_url,self.page + 1, '下一页'))
        pageer.append('<a href="%s?p=%s">%s</a>' % (self.base_url, self.total_pages(), '末页'))
        current_page = ''.join(pageer)
        return current_page
