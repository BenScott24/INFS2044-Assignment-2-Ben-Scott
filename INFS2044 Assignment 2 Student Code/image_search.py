import click


@click.group()
def main():
    pass

#
# Each of the functions below is the entry point of a use case for the command line application.
# Call your code from each of these functions, but do not include all of your code in the functions
# in this file.
#

@main.command()
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
def add(image_path):
    pass

@main.command()
@click.option('--all/--some', default=True, show_default=True, help='List images that match all/some query terms')
@click.argument('terms', nargs=-1, required=True)
def search(all, terms):
    pass


@main.command()
@click.option('--k', default=None, type=click.IntRange(1), show_default=True, help='Number of matches to return')
@click.argument('image_path', type=click.Path(exists=True, dir_okay=False))
def similar(k, image_path):
    pass

@main.command()
def list():
    pass


if __name__ == '__main__':
    main()
