import click

@click.group()
def cli():
  "nitro"

@cli.command(name="command")
def first_command():
    click.echo("hi from nitro")
