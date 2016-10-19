import click
from os import listdir, makedirs
from os.path import isdir, join, exists
from click import ClickException


def create_at_path(path):
    if exists(path):
        raise ClickException("Role %s already exists" % path)

    # Create the directory layout
    makedirs(join(path, 'defaults'))
    makedirs(join(path, 'files'))
    makedirs(join(path, 'meta'))
    makedirs(join(path, 'tasks'))
    makedirs(join(path, 'templates'))

    # Create the empty main.yml files
    open(join(path, 'defaults', 'main.yml'), 'a').close()
    open(join(path, 'meta', 'main.yml'), 'a').close()
    open(join(path, 'tasks', 'main.yml'), 'a').close()


@click.command()
@click.argument('name')
def create_role(name):
    """ A simple tool that creates an ansible role with the
        reccomended directory layout """
    roles_dir = [member for member in listdir('.')
                 if isdir(member) and member == 'roles']

    if roles_dir:
        create_at_path(join(".", "roles", name))
    else:
        create_at_path(join(".", name))


if __name__ == '__main__':
    create_role()
