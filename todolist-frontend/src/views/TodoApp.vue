<template>
  <div class="todo-app">
    <ThemeToggle />
    
    <div class="container">
      <header class="app-header">
        <h1>Todo List</h1>
        <p class="subtitle">保持专注，逐个击破</p>
      </header>
      
      <main class="app-main">
        <ProgressStats
          :total="todoStore.completionStats.total"
          :completed="todoStore.completionStats.completed"
          :percentage="todoStore.completionStats.percentage"
        />
        
        <TodoInput />
        
        <TodoList />
      </main>
    </div>
    
    <el-alert
      v-if="todoStore.error"
      :title="todoStore.error"
      type="error"
      show-icon
      closable
      @close="todoStore.clearError"
      class="error-alert"
    />
    
    <div v-if="todoStore.loading" class="loading-overlay">
      <el-loading background="rgba(0, 0, 0, 0.7)" />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useTodoStore } from '../stores/todo'
import ThemeToggle from '../components/ThemeToggle.vue'
import ProgressStats from '../components/ProgressStats.vue'
import TodoInput from '../components/TodoInput.vue'
import TodoList from '../components/TodoList.vue'

const todoStore = useTodoStore()

onMounted(() => {
  todoStore.fetchTodos()
})
</script>

<style scoped lang="scss">
.todo-app {
  min-height: 100vh;
  padding: 2rem 0;
  background: var(--background);
}

.app-header {
  text-align: center;
  margin-bottom: 3rem;
  
  h1 {
    font-size: 3rem;
    font-weight: 700;
    color: var(--text);
    margin-bottom: 0.5rem;
    background: linear-gradient(135deg, var(--primary) 0%, #4f46e5 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
  }
  
  .subtitle {
    font-size: 1.125rem;
    color: var(--text-secondary);
  }
}

.app-main {
  max-width: 800px;
  margin: 0 auto;
}

@media (max-width: 768px) {
  .todo-app {
    padding: 1rem 0;
  }
  
  .app-header {
    margin-bottom: 2rem;
    
    h1 {
      font-size: 2rem;
    }
    
    .subtitle {
      font-size: 1rem;
    }
  }
}

.error-alert {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  z-index: 1000;
}

.loading-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.1);
  z-index: 999;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style> 