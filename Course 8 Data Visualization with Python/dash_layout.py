# Import required packages
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, callback, Output, Input

# Add DataFrame
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "NYC", "MTL", "NYC"]
})

# Create a Dash application
app = Dash(__name__)

# Define the layout
app.layout = html.Div(children=[
    html.H1(
        children='Dashboard',
        style={
            'textAlign': 'center'
        }
    ),

    # Create dropdown
    dcc.Dropdown(
        id='city-dropdown',
        options=[
            {'label': 'New York City', 'value': 'NYC'},
            {'label': 'Montréal', 'value': 'MTL'},
            {'label': 'San Francisco', 'value': 'SF'}
        ],
        value='NYC'  # Providing a value to the dropdown
    ),

    # Bar graph
    dcc.Graph(id='example-graph-2', figure=px.bar(df, x="Fruit", y="Amount", color="City", barmode="group"))
])

# Run the application
if __name__ == '__main__':
    app.run_server()
