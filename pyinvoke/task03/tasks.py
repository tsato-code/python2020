from invoke import Collection, task
import docs


@task
def deploy(c):
    c.run("python setup.py sdist")
    c.run("twine upload dist/*")


namespace = Collection(docs, deploy)
