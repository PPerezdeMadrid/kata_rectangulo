
# Unittest

## AssertEqual
   ```python
   import unittest

   class TestAssertions(unittest.TestCase):
       def test_assertEqual(self):
           self.assertEqual(2 + 2, 4)
   ```

## AssertTrue y AssertFalse
   ```python
   import unittest

   class TestAssertions(unittest.TestCase):
       def test_assertTrue(self):
           self.assertTrue(5 > 3)

       def test_assertFalse(self):
           self.assertFalse(2 == 3)
   ```

## AssertIn y AssertNotIn
   ```python
   import unittest

   class TestAssertions(unittest.TestCase):
       def test_assertIn(self):
           lista = [1, 2, 3, 4]
           self.assertIn(3, lista)

       def test_assertNotIn(self):
           lista = [1, 2, 3, 4]
           self.assertNotIn(5, lista)
   ```

## AssertIs y AssertIsNot
   ```python
   import unittest

   class TestAssertions(unittest.TestCase):
       def test_assertIs(self):
           x = [1, 2, 3]
           y = x
           self.assertIs(x, y)

       def test_assertIsNot(self):
           x = [1, 2, 3]
           y = [1, 2, 3]
           self.assertIsNot(x, y)
   ```
