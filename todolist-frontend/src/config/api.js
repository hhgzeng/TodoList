const API_CONFIG = {
  // BASE_URL: import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/',
  BASE_URL: import.meta.env.VITE_API_BASE_URL || 'https://todolist-wb4m.onrender.com',
  ENDPOINTS: {
    GET_TODOS: '/api/get-todo',
    ADD_TODO: '/api/add-todo',
    UPDATE_TODO: '/api/update-todo/',
    DELETE_TODO: '/api/del-todo/'
  }
}

export default API_CONFIG 