import click
from nitro.core import run_experiment
from pathlib import Path
import yaml
from rich import print as rprint


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
        for filepath in Path("config").glob("*.yaml"):
            with open(filepath, "r") as f:
                documents = list(yaml.safe_load_all(f))
            for doc in documents:
                # rprint(doc)
                run_experiment(doc)
    else:
        print("Running some experiments")
