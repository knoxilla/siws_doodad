"""Console script for siws_doodad."""
import sys
import click


@click.command()
def main(args=None):
    """Console script for siws_doodad."""
    click.echo("Replace this message by putting your code into "
               "siws_doodad.cli.main")
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
