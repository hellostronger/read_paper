# 测试模型API调用

# 1. 流式请求测试
curl -X POST "http://8.155.38.83:3000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-va5W0H0rfdpApJmPWpYiNZ9j2vrY3IttJ0v9xCQ9yTixAwGi" \
  -d '{
    "model": "minimaxai/minimax-m2.1",
    "messages": [
      {
        "role": "user",
        "content": "你好，请简单介绍一下自己"
      }
    ],
    "max_tokens": 100,
    "stream": true
  }'

# 2. 获取可用模型列表
curl -X GET "http://8.155.38.83:3000/v1/models" \
  -H "Authorization: Bearer sk-va5W0H0rfdpApJmPWpYiNZ9j2vrY3IttJ0v9xCQ9yTixAwGi"

# 3. 简单流式测试（单行版）
curl -s -X POST "http://8.155.38.83:3000/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer sk-va5W0H0rfdpApJmPWpYiNZ9j2vrY3IttJ0v9xCQ9yTixAwGi" \
  -d '{"model": "minimaxai/minimax-m2.1", "messages": [{"role": "user", "content": "hello"}], "max_tokens": 50, "stream": true}'
