import unittest
from src.main import main

class TestMain(unittest.TestCase):
    def test_main_output(self):
        # 这里只做示例，实际可用 capsys 捕获输出
        self.assertIsNone(main())

if __name__ == "__main__":
    unittest.main()
