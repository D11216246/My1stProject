# 任務二：safe_division 的單元測試
# 使用 Python unittest 框架進行測試

import unittest
import sys
from io import StringIO
from safe_division import safe_division


class TestSafeDivision(unittest.TestCase):
    """safe_division 函式的單元測試"""
    
    def test_normal_division(self):
        """測試正常的除法運算"""
        self.assertEqual(safe_division(10, 2), 5.0)
        self.assertEqual(safe_division(15, 3), 5.0)
        self.assertEqual(safe_division(20, 4), 5.0)
    
    def test_division_with_floats(self):
        """測試浮點數除法"""
        self.assertAlmostEqual(safe_division(7, 2), 3.5)
        self.assertAlmostEqual(safe_division(1, 3), 0.3333333333333333)
        self.assertAlmostEqual(safe_division(22, 7), 3.142857142857143)
    
    def test_division_by_zero(self):
        """測試除以零的情況（應回傳 None）"""
        # 捕捉 print 輸出
        captured_output = StringIO()
        sys.stdout = captured_output
        
        result = safe_division(10, 0)
        
        # 恢復 stdout
        sys.stdout = sys.__stdout__
        
        self.assertIsNone(result)
        self.assertIn("錯誤：除數不可為零！", captured_output.getvalue())
    
    def test_negative_numbers(self):
        """測試負數除法"""
        self.assertEqual(safe_division(-10, 2), -5.0)
        self.assertEqual(safe_division(10, -2), -5.0)
        self.assertEqual(safe_division(-10, -2), 5.0)
    
    def test_zero_dividend(self):
        """測試被除數為零的情況"""
        self.assertEqual(safe_division(0, 5), 0.0)
        self.assertEqual(safe_division(0, 100), 0.0)
    
    def test_division_result_less_than_one(self):
        """測試結果小於 1 的除法"""
        self.assertEqual(safe_division(1, 2), 0.5)
        self.assertEqual(safe_division(1, 4), 0.25)
        self.assertEqual(safe_division(3, 4), 0.75)
    
    def test_large_numbers(self):
        """測試大數除法"""
        self.assertEqual(safe_division(1000000, 1000), 1000.0)
        self.assertEqual(safe_division(999999, 3), 333333.0)
    
    def test_division_by_one(self):
        """測試除以 1 的情況"""
        self.assertEqual(safe_division(42, 1), 42.0)
        self.assertEqual(safe_division(-42, 1), -42.0)
    
    def test_same_numbers(self):
        """測試相同數字相除（應為 1）"""
        self.assertEqual(safe_division(5, 5), 1.0)
        self.assertEqual(safe_division(100, 100), 1.0)
        self.assertEqual(safe_division(-7, -7), 1.0)


class TestSafeDivisionEdgeCases(unittest.TestCase):
    """測試邊界情況"""
    
    def test_very_small_divisor(self):
        """測試非常小的除數（但不為零）"""
        result = safe_division(1, 0.0001)
        self.assertAlmostEqual(result, 10000.0)
    
    def test_float_zero_divisor(self):
        """測試浮點數 0.0 作為除數"""
        captured_output = StringIO()
        sys.stdout = captured_output
        
        result = safe_division(10, 0.0)
        
        sys.stdout = sys.__stdout__
        
        self.assertIsNone(result)
    
    def test_multiple_divisions(self):
        """測試連續多次除法操作"""
        results = [
            safe_division(100, 10),
            safe_division(50, 5),
            safe_division(30, 0),
            safe_division(40, 4)
        ]
        self.assertEqual(results[0], 10.0)
        self.assertEqual(results[1], 10.0)
        self.assertIsNone(results[2])
        self.assertEqual(results[3], 10.0)


if __name__ == '__main__':
    # 執行所有測試
    unittest.main(verbosity=2)
