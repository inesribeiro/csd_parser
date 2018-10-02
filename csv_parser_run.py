import matplotlib.pyplot as plt
import pandas as pd
import click
@click.group()
def cli():
    """Can display and plot csv files."""
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Displays the column names and their data type."""
    df = pd.read_csv(filename)
    print(df.dtypes)

@cli.command()
@click.argument('filename')
@click.option('--column', default=None, help='Name of column to plot. If not used, all columns will be plotted.')
def plot(filename, column):
    """Plots a histogram of a column of the csv file."""
    df = pd.read_csv(filename)
    if column == None:
        df.hist()
    else:
        df[column].hist()
        plt.title(column)
    plt.show()
    
if __name__ == '__main__':
    cli()