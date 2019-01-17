from api import app


def index():
    return ('hello user')

if __name__ == '__main__':
    app.run(debug=True)
