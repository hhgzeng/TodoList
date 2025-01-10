<template>
  <button 
    class="theme-toggle" 
    @click="toggleTheme"
    :title="isDark ? '切换到亮色模式' : '切换到暗色模式'"
  >
    <el-icon :size="24" class="toggle-icon">
      <Sunny v-if="isDark" />
      <Moon v-else />
    </el-icon>
  </button>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue'
import { Sunny, Moon } from '@element-plus/icons-vue'
import { lightTheme, darkTheme } from '../styles/theme'

const isDark = ref(false)

const applyTheme = (theme) => {
  Object.entries(theme).forEach(([key, value]) => {
    document.documentElement.style.setProperty(`--${key.replace(/([A-Z])/g, '-$1').toLowerCase()}`, value)
  })
}

const toggleTheme = () => {
  isDark.value = !isDark.value
  localStorage.setItem('theme', isDark.value ? 'dark' : 'light')
}

watch(isDark, (newValue) => {
  applyTheme(newValue ? darkTheme : lightTheme)
})

onMounted(() => {
  const savedTheme = localStorage.getItem('theme')
  isDark.value = savedTheme === 'dark'
  applyTheme(isDark.value ? darkTheme : lightTheme)
})
</script>

<style scoped lang="scss">
.theme-toggle {
  position: fixed;
  top: 2rem;
  right: 2rem;
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 50%;
  width: 48px;
  height: 48px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: var(--shadow);
  
  &:hover {
    transform: scale(1.1);
    background: var(--primary);
    border-color: var(--primary);
    .toggle-icon {
      color: white;
    }
  }
  
  .toggle-icon {
    color: var(--text);
    transition: color 0.3s ease;
  }
}

@media (max-width: 768px) {
  .theme-toggle {
    top: 1rem;
    right: 1rem;
    width: 40px;
    height: 40px;
  }
}
</style> 