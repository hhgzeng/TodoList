<template>
  <div class="todo-list">
    <div class="list-header">
      <el-radio-group v-model="todoStore.filter" size="large">
        <el-radio-button label="all">全部</el-radio-button>
        <el-radio-button label="active">未完成</el-radio-button>
        <el-radio-button label="completed">已完成</el-radio-button>
      </el-radio-group>
    </div>
    
    <TransitionGroup 
      name="list" 
      tag="ul"
      class="todos"
    >
      <li 
        v-for="todo in todoStore.filteredTodos" 
        :key="todo.id"
        class="todo-item"
        :class="{ 'is-completed': todo.isCompleted }"
      >
        <el-checkbox
          v-model="todo.isCompleted"
          @change="() => todoStore.toggleTodo(todo.id)"
          class="todo-checkbox"
        >
          {{ todo.value }}
        </el-checkbox>
        
        <el-button
          type="danger"
          :icon="Delete"
          circle
          @click="todoStore.deleteTodo(todo.id)"
          class="delete-btn"
        />
      </li>
    </TransitionGroup>
    
    <div v-if="!todoStore.filteredTodos.length" class="empty-state">
      <el-empty description="暂无待办事项" />
    </div>
  </div>
</template>

<script setup>
import { Delete } from '@element-plus/icons-vue'
import { useTodoStore } from '../stores/todo'

const todoStore = useTodoStore()
</script>

<style scoped lang="scss">
.todo-list {
  .list-header {
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: center;
  }
}

.todos {
  list-style: none;
  padding: 0;
}

.todo-item {
  background: var(--surface);
  border-radius: 12px;
  padding: 1rem;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  transition: all 0.3s ease;
  
  &.is-completed {
    background: var(--surface);
    opacity: 0.7;
    
    .todo-checkbox {
      text-decoration: line-through;
      color: var(--text-secondary);
    }
  }
  
  &:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-lg);
    
    .delete-btn {
      opacity: 1;
    }
  }
}

.todo-checkbox {
  flex: 1;
  margin-right: 1rem;
  
  :deep(.el-checkbox__label) {
    color: var(--text);
    font-size: 1rem;
    transition: all 0.3s ease;
  }
}

.delete-btn {
  opacity: 0;
  transition: all 0.3s ease;
  
  &:hover {
    transform: scale(1.1);
  }
}

.empty-state {
  padding: 2rem;
  text-align: center;
  color: var(--text-secondary);
}

// 列表动画
.list-enter-active,
.list-leave-active {
  transition: all 0.5s ease;
}

.list-enter-from {
  opacity: 0;
  transform: translateX(30px);
}

.list-leave-to {
  opacity: 0;
  transform: translateX(-30px);
}

@media (max-width: 768px) {
  .todo-item {
    padding: 0.75rem;
    
    .delete-btn {
      opacity: 1;
      transform: scale(0.9);
    }
  }
  
  .todo-checkbox {
    :deep(.el-checkbox__label) {
      font-size: 0.875rem;
    }
  }
}
</style> 