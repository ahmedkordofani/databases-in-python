from lib.recipe_repository import RecipeRepository

def main():
    try:
        # Define your database connection string with the correct details
        connection_string = "dbname=recipe_directory host=localhost port=5432"
        
        # Create an instance of the RecipeRepository
        recipe_repository = RecipeRepository(connection_string)
        
        # Fetch all recipes from the database
        recipes = recipe_repository.all()
        
        # Print out the list of recipes
        for recipe in recipes:
            print(f"Recipe ID: {recipe.id}, Name: {recipe.name}, Cooking Time (min): {recipe.cooking_time_minutes}, Rating: {recipe.rating}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
