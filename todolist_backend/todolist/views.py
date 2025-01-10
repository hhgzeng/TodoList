import json
import logging
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import TodoItem

# 配置日志记录器
logger = logging.getLogger(__name__)

@require_http_methods(["GET"])
def get_todo_list(request):
    """获取所有待办事项
    
    Returns:
        JsonResponse: 包含所有待办事项的JSON响应
    """
    try:
        # 查询所有待办事项
        todos = TodoItem.objects.all()
        # 将查询结果转换为列表
        todo_list = list(todos.values())
        logger.info("成功获取待办事项列表")
        return JsonResponse({'status': 'success', 'data': todo_list})
    except Exception as e:
        logger.error(f"获取待办事项列表失败: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def add_todo(request):
    """添加新的待办事项
    
    Args:
        request: 包含待办事项信息的请求
        
    Returns:
        JsonResponse: 新创建的待办事项信息
    """
    try:
        data = json.loads(request.body)
        value = data.get('value')
        is_completed = data.get('isCompleted', False)
        
        if not value:
            return JsonResponse({'status': 'error', 'message': '待办事项内容不能为空'}, status=400)
            
        # 创建新的待办事项
        todo = TodoItem.objects.create(
            value=value,
            isCompleted=is_completed
        )
        logger.info(f"成功创建待办事项: {value}")
        return JsonResponse({
            'status': 'success',
            'data': {
                'id': todo.id,
                'value': todo.value,
                'isCompleted': todo.isCompleted,
                'created_at': todo.created_at,
                'updated_at': todo.updated_at
            }
        })
    except Exception as e:
        logger.error(f"创建待办事项失败: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def update_todo(request):
    """更新待办事项状态
    
    Args:
        request: 包含待办事项ID的请求
        
    Returns:
        JsonResponse: 更新后的待办事项信息
    """
    try:
        data = json.loads(request.body)
        todo_id = data.get('id')
        
        if not todo_id:
            return JsonResponse({'status': 'error', 'message': '未提供待办事项ID'}, status=400)
            
        # 查找并更新待办事项
        todo = TodoItem.objects.get(id=todo_id)
        todo.isCompleted = not todo.isCompleted
        todo.save()
        
        logger.info(f"成功更新待办事项状态: ID {todo_id}")
        return JsonResponse({
            'status': 'success',
            'data': {
                'id': todo.id,
                'value': todo.value,
                'isCompleted': todo.isCompleted,
                'updated_at': todo.updated_at
            }
        })
    except TodoItem.DoesNotExist:
        logger.error(f"待办事项不存在: ID {todo_id}")
        return JsonResponse({'status': 'error', 'message': '待办事项不存在'}, status=404)
    except Exception as e:
        logger.error(f"更新待办事项失败: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)

@csrf_exempt
@require_http_methods(["POST"])
def delete_todo(request):
    """删除待办事项
    
    Args:
        request: 包含待办事项ID的请求
        
    Returns:
        JsonResponse: 删除操作的结果状态
    """
    try:
        data = json.loads(request.body)
        todo_id = data.get('id')
        
        if not todo_id:
            return JsonResponse({'status': 'error', 'message': '未提供待办事项ID'}, status=400)
            
        # 查找并删除待办事项
        todo = TodoItem.objects.get(id=todo_id)
        todo.delete()
        
        logger.info(f"成功删除待办事项: ID {todo_id}")
        return JsonResponse({'status': 'success', 'message': '待办事项已删除'})
    except TodoItem.DoesNotExist:
        logger.error(f"待办事项不存在: ID {todo_id}")
        return JsonResponse({'status': 'error', 'message': '待办事项不存在'}, status=404)
    except Exception as e:
        logger.error(f"删除待办事项失败: {str(e)}")
        return JsonResponse({'status': 'error', 'message': str(e)}, status=500)
