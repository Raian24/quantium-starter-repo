import pandas as pd
from dash import Dash, html, dcc, Input, Output
import plotly.express as px

df = pd.read_csv("formatted_output.csv")
df["date"] = pd.to_datetime(df["date"])

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),

    html.Label("Select Region:"),
    dcc.RadioItems(
        id="region-selector",
        options=[
            {"label": "All", "value": "all"},
            {"label": "North", "value": "north"},
            {"label": "East", "value": "east"},
            {"label": "South", "value": "south"},
            {"label": "West", "value": "west"},
        ],
        value="all",
        inline=True
    ),

    dcc.Graph(id="sales-chart")
])

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-selector", "value")
)
def update_chart(selected_region):
    filtered_df = df.copy()

    if selected_region != "all":
        filtered_df = filtered_df[filtered_df["region"] == selected_region]

    filtered_df = filtered_df.sort_values("date")
    daily_sales = filtered_df.groupby("date", as_index=False)["sales"].sum()

    fig = px.line(
        daily_sales,
        x="date",
        y="sales",
        labels={"date": "Date", "sales": "Sales"},
        title=f"Pink Morsel Sales Over Time - {selected_region.title()}"
    )

    return fig

if __name__ == "__main__":
    app.run(debug=True)