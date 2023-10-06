import unittest
from lib.recipe import Recipe

class TestRecipe(unittest.TestCase):
    def test_recipe_attributes(self):
        # Test creating a Recipe instance and checking its attributes
        recipe = Recipe(1, "Spaghetti Carbonara", 30, 4)

        self.assertEqual(recipe.id, 1)
        self.assertEqual(recipe.name, "Spaghetti Carbonara")
        self.assertEqual(recipe.cooking_time_minutes, 30)
        self.assertEqual(recipe.rating, 4)

if __name__ == '__main__':
    unittest.main()
