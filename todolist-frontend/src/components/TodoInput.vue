<template>
  <div class="todo-input-container">
    <div class="input-wrapper" :class="{ 'is-focused': isFocused }">
      <el-input
        v-model="newTodo"
        placeholder="添加新的待办事项..."
        class="todo-input"
        @keyup.enter="handleSubmit"
        @focus="isFocused = true"
        @blur="isFocused = false"
      >
        <template #prefix>
          <el-icon class="input-icon"><Edit /></el-icon>
        </template>
      </el-input>
      
      <el-button
        class="submit-btn"
        type="primary"
        :disabled="!newTodo.trim()"
        @click="handleSubmit"
      >
        <el-icon><Plus /></el-icon>
        添加任务
      </el-button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { Edit, Plus } from '@element-plus/icons-vue'
import { useTodoStore } from '../stores/todo'

const todoStore = useTodoStore()
const newTodo = ref('')
const isFocused = ref(false)

const handleSubmit = async () => {
  const value = newTodo.value.trim()
  if (!value) return
  
  await todoStore.addTodo(value)
  newTodo.value = ''
}
</script>

<style scoped lang="scss">
.todo-input-container {
  margin-bottom: 2rem;
  max-width: 800px;
  margin-left: auto;
  margin-right: auto;
  width: 100%;
}

.input-wrapper {
  background: var(--surface);
  border-radius: 16px;
  padding: 1rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  display: flex;
  gap: 1rem;
  transition: all 0.3s ease;
  
  &.is-focused {
    border-color: var(--primary);
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
    transform: translateY(-2px);
  }
  
  &:hover {
    transform: translateY(-2px);
  }
}

.todo-input {
  flex: 1;
  
  :deep(.el-input__wrapper) {
    background: transparent;
    box-shadow: none !important;
    padding-left: 0;
    
    &.is-focus {
      box-shadow: none !important;
    }
  }
  
  :deep(.el-input__inner) {
    height: 44px;
    color: var(--text);
    font-size: 1rem;
    
    &::placeholder {
      color: var(--text-secondary);
      font-size: 0.95rem;
    }
  }
  
  .input-icon {
    font-size: 1.25rem;
    color: var(--primary);
    margin-right: 0.5rem;
  }
}

.submit-btn {
  height: 44px;
  padding: 0 1.5rem;
  border-radius: 12px;
  font-weight: 500;
  font-size: 0.95rem;
  background: var(--primary);
  border: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  transition: all 0.3s ease;
  
  &:not(:disabled):hover {
    transform: translateY(-1px);
    filter: brightness(1.1);
  }
  
  &:disabled {
    opacity: 0.5;
    cursor: not-allowed;
    background: var(--text-secondary);
  }
  
  .el-icon {
    font-size: 1.1rem;
  }
}

@media (max-width: 768px) {
  .todo-input-container {
    padding: 0;
  }
  
  .input-wrapper {
    padding: 0.75rem;
    flex-direction: column;
    gap: 0.75rem;
  }
  
  .todo-input {
    :deep(.el-input__inner) {
      height: 40px;
    }
  }
  
  .submit-btn {
    height: 40px;
    width: 100%;
    justify-content: center;
  }
}
</style> 