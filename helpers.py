from pathlib import Path


def revenue_by_group(df, group_column):
    """
    Calculate total revenue for a selected column
    and rank the results from highest to lowest.
    """
    return (
        df.groupby(group_column)["revenue"]
        .sum()
        .sort_values(ascending=False)
    )


def save_chart(fig, filename):
    """
    Save a Matplotlib figure to the charts folder.
    """
    charts_folder = Path("charts")
    charts_folder.mkdir(exist_ok=True)

    file_path = charts_folder / filename

    fig.savefig(
        file_path,
        dpi=300,
        bbox_inches="tight"
    )