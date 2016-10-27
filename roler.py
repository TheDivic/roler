import click
from os import listdir, makedirs, environ
from os.path import isdir, join, exists, abspath
from click import ClickException
from shutil import copytree


def create_at_path(name, path, my):
    if exists(path):
        raise ClickException("Role %s already exists" % path)

    roledir = environ.get("ROLER_ROLEDIR")

    if my and roledir and exists(join(roledir, name)):
        copytree(join(roledir, name), path)
        print("Copied role: %s" % abspath(path))
        return

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

    # Output created role path
    print("Created role: %s" % abspath(path))


@click.command()
@click.argument('name')
@click.option('--my/--no-my', default=False,
              help='If ROLER_ROLEDIR envar is set it will copy the role from that directory')
def create_role(name, my):
    """ A simple tool that creates an ansible role with the
        reccomended directory layout """
    roles_dir = [member for member in listdir('.')
                 if isdir(member) and member == 'roles']

    if roles_dir:
        create_at_path(name, join(".", "roles", name), my)
    else:
        create_at_path(name, join(".", name), my)


if __name__ == '__main__':
    create_role()
