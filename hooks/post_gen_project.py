import os

from distutils.util import strtobool

PLUGIN_NAME = '{{ cookiecutter.name }}'
PLUGIN_PATH = os.path.join('doc', 'plugins', PLUGIN_NAME)
LICENSE_TIDDLER_PATH = os.path.join('src', 'License.tid')
INCLUDE_GITHUB_FORK_RIBBON = '{{ cookiecutter.include_github_fork_ribbon }}'

def main() -> None:
    os.mkdir(os.path.join('doc', 'plugins'))
    try:
        os.symlink(f'../../src', PLUGIN_PATH)
    except FileExistsError:
        # Exists from a previous run (-f/--overwrite-if-exists).
        pass
    with open('LICENSE') as f:
        license = f.read()
    with open(LICENSE_TIDDLER_PATH, 'a') as f:
        f.write(license)
    if not str2bool(INCLUDE_GITHUB_FORK_RIBBON):
        os.remove(os.path.join('doc', 'tiddlers', 'system', 'github-fork-ribbon.tid'))


def str2bool(value) -> bool:
    return bool(strtobool(value))


if __name__ == '__main__':
    main()
