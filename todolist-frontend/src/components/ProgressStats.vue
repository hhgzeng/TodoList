<template>
  <div class="progress-stats" :class="{ 'is-completed': percentage === 100 }">
    <div class="stats-content">
      <div class="stats-text">
        <h3>任务完成度</h3>
        <p>{{ completed }}/{{ total }} 已完成</p>
      </div>
      <div class="progress-bar">
        <div 
          class="progress-fill"
          :style="{ width: `${percentage}%` }"
        >
          <span class="progress-text">{{ percentage }}%</span>
        </div>
      </div>
    </div>
    <el-icon class="completion-icon" v-if="percentage === 100">
      <CircleCheckFilled />
    </el-icon>
  </div>
</template>

<script setup>
import { CircleCheckFilled } from '@element-plus/icons-vue'

defineProps({
  total: {
    type: Number,
    required: true
  },
  completed: {
    type: Number,
    required: true
  },
  percentage: {
    type: Number,
    required: true
  }
})
</script>

<style scoped lang="scss">
.progress-stats {
  background: var(--surface);
  border-radius: 16px;
  padding: 1.5rem;
  margin-bottom: 2rem;
  box-shadow: var(--shadow);
  border: 1px solid var(--border);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  
  &.is-completed {
    background: var(--success);
    border-color: var(--success);
    
    .stats-text {
      h3, p {
        color: white;
      }
    }
    
    .progress-bar {
      background: rgba(255, 255, 255, 0.2);
    }
    
    .progress-fill {
      background: white;
      
      .progress-text {
        color: var(--success);
      }
    }
    
    .completion-icon {
      color: white;
    }
  }
}

.stats-content {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.stats-text {
  h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--text);
  }
  
  p {
    color: var(--text-secondary);
    font-size: 0.875rem;
  }
}

.progress-bar {
  height: 24px;
  background: var(--background);
  border-radius: 12px;
  overflow: hidden;
  position: relative;
}

.progress-fill {
  height: 100%;
  background: var(--primary);
  border-radius: 12px;
  transition: width 0.6s ease;
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-text {
  color: white;
  font-size: 0.875rem;
  font-weight: 500;
}

.completion-icon {
  position: absolute;
  top: 1rem;
  right: 1rem;
  font-size: 1.5rem;
}

@media (max-width: 768px) {
  .progress-stats {
    padding: 1rem;
  }
  
  .progress-bar {
    height: 20px;
  }
  
  .stats-text h3 {
    font-size: 1rem;
  }
}
</style> 