#!/bin/bash

if [ "$1" == "start" ]; then
  # 启动后端
  source env/bin/activate && python todolist_backend/manage.py runserver &
  BACKEND_PID=$!

  # 启动前端
  cd todolist-frontend && npm run dev &
  FRONTEND_PID=$!

  echo "Backend PID: $BACKEND_PID"
  echo "Frontend PID: $FRONTEND_PID"

elif [ "$1" == "stop" ]; then
  # 停止后端
  pkill -f manage.py
  echo "Backend stopped."

  # 停止前端
  pkill -f "npm run dev"
  echo "Frontend stopped."

else
  echo "Usage: $0 {start|stop}"
fi
