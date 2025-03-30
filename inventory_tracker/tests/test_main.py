import unittest
from models import Customer  # ✅ updated import

class TestCustomer(unittest.TestCase):
    def test_summary_no_orders(self):
        c = Customer("kate")
        self.assertEqual(c.get_summary(), "Kate: n/a")

    def test_summary_with_orders(self):
        c = Customer("kate")
        c.add_order("hats", 2, 20.0)
        c.add_order("socks", 1, 5.0)
        self.assertIn("Kate: hats - $40.00, socks - $5.00", c.get_summary())
        self.assertIn("Average Order Value: $22.50", c.get_summary())

if __name__ == "__main__":
    unittest.main()
