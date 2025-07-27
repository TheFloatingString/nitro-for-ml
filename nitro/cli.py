import click


@click.group()
@click.version_option()
def cli():
    "Nitro CLI"


@cli.command(name="run")
@click.option(
    "--all",
    help="Run all experiments",
    is_flag=True,
)
def nitro_cli(all):
    "Run all experiments"
    if all:
        print("Running all experiments")
    else:
        print("Running some experiments")
