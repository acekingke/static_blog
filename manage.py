# manage.py

from flask.ext.script import Manager
from flask import Flask, render_template,g, request, url_for
from blog import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"
@manager.command
def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():

        options = {}
        for arg in rule.arguments:
            print 'rule arg:', arg
        methods = ','.join(rule.methods)
        #url = url_for(rule.endpoint, **options)

        url = url_for(rule.endpoint, **options)
        #line = urllib.unquote("{:50s} {:20s} {}".format(rule.endpoint, methods, url))
        output.append(url)

    for line in sorted(output):
        print line
if __name__ == "__main__":
    manager.run()