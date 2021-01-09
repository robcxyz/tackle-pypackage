"""Console script for {{project_slug}}."""
import sys
import os

from {{project_slug}} import __version__
from {{project_slug}}.config import Config
import yaml

import click


def version_msg():
    """Return the Cookiecutter version, location and Python powering it."""
    location = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return f'Version: {__version__} from {location} (Python {sys.version[:3]})'


@click.command(context_settings=dict(help_option_names=['-h', '--help']))
@click.version_option(__version__, '-V', '--version', message=version_msg())
@click.argument('input', required=False)
@click.option(
    u'--config-file',
    default=None,
    help=u'Path to config file.',
)
@click.option(
    u'--debug',
    is_flag=True,
    help=u'',
)
def main(
    input,
    config_file,
    debug,
):
    """
    Main entry point for {{project_slug}}.

    :param input: Something
    :param config_file: Path to the yaml config file.
    :param debug: Debug flag

    :return Something
    """
    if config_file:
        with open(config_file, encoding='utf-8') as f:
            config_contents = yaml.safe_load(f)
        config = Config(**config_contents)
    else:
        config = Config()

    print(input)
    if debug:
        with open('debug.yaml', 'w') as f:
            yaml.dump(config.dict(), f)


if __name__ == "__main__":
    main()
