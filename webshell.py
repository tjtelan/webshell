import bottle

from webshell import model, view, controller

app = bottle.app()

if __name__ == '__main__':
    app.run(host='localhost', port=8080, reloader=True, debug=True)
