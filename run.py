"app has to exist within __init__.py"
from flask_word import app


"now the only purpose of this file is to run app"
"cond True when run this script directly(Not imported)"
if __name__ == '__main__':
    app.run(debug=True)
