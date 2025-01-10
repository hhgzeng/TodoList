import { defineStore } from 'pinia'
import axios from 'axios'
import API_CONFIG from '../config/api.js'

const { BASE_URL, ENDPOINTS } = API_CONFIG

// 创建axios实例
const apiClient = axios.create({
  baseURL: BASE_URL,
  headers: {
    'Content-Type': 'application/json',
    'Accept': 'application/json'
  }
})

export const useTodoStore = defineStore('todo', {
  state: () => ({
    todos: [],
    filter: 'all',
    loading: false,
    error: null
  }),

  getters: {
    filteredTodos: (state) => {
      switch (state.filter) {
        case 'active':
          return state.todos.filter(todo => !todo.isCompleted)
        case 'completed':
          return state.todos.filter(todo => todo.isCompleted)
        default:
          return state.todos
      }
    },
    
    completionStats: (state) => {
      const total = state.todos.length
      const completed = state.todos.filter(todo => todo.isCompleted).length
      const percentage = total === 0 ? 0 : Math.round((completed / total) * 100)
      return { total, completed, percentage }
    }
  },

  actions: {
    async fetchTodos() {
      this.loading = true
      try {
        const response = await apiClient.get(ENDPOINTS.GET_TODOS)
        this.todos = response.data.data
      } catch (error) {
        this.error = '获取待办事项失败'
        console.error('Error fetching todos:', error)
      } finally {
        this.loading = false
      }
    },

    async addTodo(value) {
      try {
        const response = await apiClient.post(ENDPOINTS.ADD_TODO, {
          value,
          isCompleted: false
        })
        this.todos.unshift(response.data.data)
      } catch (error) {
        this.error = '添加待办事项失败'
        console.error('Error adding todo:', error)
      }
    },

    async toggleTodo(id) {
      try {
        const response = await apiClient.post(ENDPOINTS.UPDATE_TODO, { id })
        const index = this.todos.findIndex(todo => todo.id === id)
        if (index !== -1) {
          this.todos[index] = response.data.data
        }
      } catch (error) {
        this.error = '更新待办事项失败'
        console.error('Error updating todo:', error)
      }
    },

    async deleteTodo(id) {
      try {
        await apiClient.post(ENDPOINTS.DELETE_TODO, { id })
        this.todos = this.todos.filter(todo => todo.id !== id)
      } catch (error) {
        this.error = '删除待办事项失败'
        console.error('Error deleting todo:', error)
      }
    },

    setFilter(filter) {
      this.filter = filter
    },

    clearError() {
      this.error = null
    }
  }
}) 