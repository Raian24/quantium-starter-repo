import pandas as pd
from dash import Dash, html, dcc
import plotly.express as px

# Load processed data from Task 2
df = pd.read_csv("formatted_output.csv")

# Convert date column and sort
df["date"] = pd.to_datetime(df["date"])
df = df.sort_values("date")

# Group by date to get total daily sales
daily_sales = df.groupby("date", as_index=False)["sales"].sum()

# Build line chart
fig = px.line(
    daily_sales,
    x="date",
    y="sales",
    title="Pink Morsel Sales Over Time",
    labels={
        "date": "Date",
        "sales": "Sales"
    }
)

app = Dash(__name__)

app.layout = html.Div([
    html.H1("Pink Morsel Sales Visualiser"),
    dcc.Graph(figure=fig)
])

if __name__ == "__main__":
    app.run(debug=True)