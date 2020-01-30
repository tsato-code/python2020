from invoke import task


@task
def clean(ctx):
    print("Cleaning!")
    ctx.run("rm -rf docs/_build")


@task(clean)
def build(ctx):
    print("Building!")
