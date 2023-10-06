import psycopg2
from lib.recipe import Recipe

class RecipeRepository:
    def __init__(self, connection_string):
        self.connection_string = connection_string

    def all(self):
        recipes = []
        conn = None
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes')
            rows = cursor.fetchall()
            for row in rows:
                recipe = Recipe(row[0], row[1], row[2], row[3])
                recipes.append(recipe)
        except psycopg2.Error as e:
            print(f"Error fetching recipes: {e}")
        finally:
            if conn:
                conn.close()
        return recipes


    def find(self, recipe_id):
        conn = None
        try:
            conn = psycopg2.connect(self.connection_string)
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM recipes WHERE id = %s', [recipe_id])
            row = cursor.fetchone()
            if row:
                recipe = Recipe(row[0], row[1], row[2], row[3])
                return recipe
            else:
                raise RecipeNotFoundException(f"No recipe found with ID {recipe_id}")
        except psycopg2.Error as e:
            print(f"Error fetching recipe: {e}")
        finally:
            if conn:
                conn.close()
        return None
