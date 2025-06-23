# remarcable-challenge

Repo for a code challenge from remarcable. A product catalog with 20 items, 10 tags, 5 categories, with search and filter systems.

Some leftover files remain from a tutorial followed earlier, so apologies for confusion.<br/>
[Tutorial is here.](https://code.visualstudio.com/docs/python/tutorial-django)<br/>

## To run the project

If you lack python, you can install it via [Chocolatey](https://community.chocolatey.org/packages/python#install).</br>

- Pull the repository
- Open a terminal or powershell window in the repo
- Instantiate the virtual environment with `.\venv\Scripts\Activate` (or `source .venv/bin/activate`)
- Run the server with `python manage.py runserver`

## Using the filters

- **Search** input form will look through product names and descriptions for your string.
- **Categories** dropdown filters products via category, 1 per item
- **Tags** are a selection list, please CTRL+Click to search multiple tags at once.
