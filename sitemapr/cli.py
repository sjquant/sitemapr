# sitemapr/cli.py

import typer

app = typer.Typer()


@app.command()
def main():
    typer.echo("Hello, this is sitemapr!")


if __name__ == "__main__":
    app()
