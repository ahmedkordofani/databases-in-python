import unittest
from lib.recipe import Recipe
from lib.recipe_repository import RecipeRepository

class TestRecipeRepository(unittest.TestCase):
    def setUp(self):
        # Set up a test database connection (you may use a testing database)
        self.connection_string = "recipe_directory"
        self.repository = RecipeRepository(self.connection_string)

    def test_all_recipes(self):
        # Test fetching all recipes from the database
        recipes = self.repository.all()
        self.assertIsInstance(recipes, list)
        # Add more assertions as needed to check the retrieved recipes

    def test_find_recipe_by_id(self):
        # Test finding a recipe by its ID
        recipe_id = 1  # Assuming you have a recipe with this ID in your test database
        recipe = self.repository.find(recipe_id)
        if recipe is not None:
            self.assertIsInstance(recipe, Recipe)
        else:
            self.assertIsNone(recipe)  # Recipe should be None when not found


if __name__ == '__main__':
    unittest.main()
