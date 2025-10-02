def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    # 修复：处理负数乘法
    if b < 0:
        a, b = -a, -b
    result = 0
    for i in range(b):
        result += a
    return result

def divide(a, b):
    if b == 0:
        # 修复：抛出异常而不是返回 None
        raise ValueError("Division by zero is not allowed")
    return a / b

# 新增功能：求余数
def modulus(a, b):
    if b == 0:
        raise ValueError("Modulus by zero is not allowed")
    return a % b
