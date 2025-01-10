from django.db import models

class TodoItem(models.Model):
    """待办事项模型类
    
    属性:
        value (str): 待办事项的具体内容
        isCompleted (bool): 待办事项的完成状态
        created_at (datetime): 创建时间
        updated_at (datetime): 最后更新时间
    """
    value = models.CharField(max_length=200, verbose_name='待办事项内容')
    isCompleted = models.BooleanField(default=False, verbose_name='完成状态')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        db_table = 'todo_items'  # 指定数据库表名
        ordering = ['-created_at']  # 按创建时间倒序排序
        verbose_name = '待办事项'
        verbose_name_plural = '待办事项列表'

    def __str__(self):
        """返回待办事项的字符串表示"""
        return f"{self.value} - {'已完成' if self.isCompleted else '未完成'}"
