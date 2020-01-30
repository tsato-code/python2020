from invoke import task


@task
def read(ctx):
    print("Read yaml file!")
    print("  |--> {}".format(ctx.hoge.abcd))
    print("  |--> {}".format(ctx.hoge.efgh))
