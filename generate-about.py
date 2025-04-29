import os
import re
import math

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
    directory = "posts/."
    recipes = parse_recipe_files(directory)
    sorted_recipes = sorted(recipes, key=lambda x: x[1].lower())
    halfway_index = (len(recipes) - 1) // 2

    print("<div style='text-align: center; font-size: 1.1rem;'>")
    print("<div style='display: inline-block;'>")
    for i, (filename, title) in enumerate(sorted_recipes):
            print(f"  <a href='/posts/{filename}'>{title}</a><br>")
            if i == halfway_index:
                print("</div>")
                print("<div style='display: inline-block; vertical-align: top;'>")
    print("</div>")
    print("</div>")

if __name__ == "__main__":
    main()
