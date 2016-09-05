import os

import cherrypy


class main():

    def index(self):
        return file('index.html')

    index.exposed=True

    def fun(self):
        pass

    fun.exposed = True

    def shutdown(self):
        cherrypy.engine.exit()

if __name__ == '__main__':
    cherrypy.config.update(
        {'server.socket_host': '172.16.170.87'})
    conf = {
        '/': {
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': 'public'
        }
    }
    cherrypy.quickstart(main(), '/', conf)