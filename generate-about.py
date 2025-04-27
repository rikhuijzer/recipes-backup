import os
import re

def parse_recipe_files(directory):
    """
    Parse Markdown files in the given directory and extract recipe titles.

    Args:
        directory (str): Path to the directory containing Markdown files.

    Returns:
        list[tuple[str, str]]: List of tuples containing the filename without extension and the recipe title.
    """
    recipes = []
    for filename in os.listdir(directory):
        if filename.endswith(".md"):
            filepath = os.path.join(directory, filename)
            with open(filepath, "r") as file:
                lines = file.readlines()
                # Skip frontmatter and find the first heading
                title = None
                in_frontmatter = False
                for line in lines:
                    if line.strip() == "---":
                        in_frontmatter = not in_frontmatter
                    elif not in_frontmatter and line.startswith("# "):
                        title = line.strip().lstrip("# ").strip()
                        break
                if title:
                    filename_without_extension = os.path.splitext(filename)[0]
                    recipes.append((filename_without_extension, title))
    return recipes

def main():
    directory = "posts/."  # current working directory
    recipes = parse_recipe_files(directory)
    sorted_recipes = sorted(recipes, key=lambda x: x[1].lower())
    for filename, title in sorted_recipes:
            print(f"- [{title}](/posts/{filename})")

if __name__ == "__main__":
    main()
