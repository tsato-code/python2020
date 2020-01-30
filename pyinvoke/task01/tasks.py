from invoke import task


@task(help={"name": "あなたの名前"})
def hi(ctx, name):
    """
    あなたにあいさつします。
    """
    print("Hi {}!".format(name))
