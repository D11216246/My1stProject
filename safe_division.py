# 防呆計算機 - Safe Division Function
# 任務一：撰寫防呆 safe_division 函式
# 功能：防止除以零的錯誤

def safe_division(a, b):
    """
    安全除法函式，防止除以零錯誤
    
    參數:
        a: 被除數 (dividend)
        b: 除數 (divisor)
    
    回傳:
        如果 b 不為零，回傳 a / b 的結果
        如果 b 為零，回傳 None 並提示錯誤訊息
    
    範例:
        >>> safe_division(10, 2)
        5.0
        >>> safe_division(10, 0)
        錯誤：除數不可為零！
        None
    """
    if b == 0:
        print("錯誤：除數不可為零！")
        return None
    return a / b


if __name__ == "__main__":
    # 示範用法
    print("=== 防呆計算機示範 ===")
    print(f"10 ÷ 2 = {safe_division(10, 2)}")
    print(f"15 ÷ 3 = {safe_division(15, 3)}")
    print(f"10 ÷ 0 = {safe_division(10, 0)}")
    print(f"7 ÷ 2 = {safe_division(7, 2)}")
