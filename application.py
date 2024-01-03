import dash
from dash import html, dcc

app = dash.Dash(__name__)
application = app.server

app.layout = html.Div(
    children=[
        html.H1(children="Dash Dashboard"),
        dcc.Graph(
            id="example-graph",
            figure={
                "data": [
                    {"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar", "name": "SF"},
                    {"x": [1, 2, 3], "y": [2, 4, 5], "type": "bar", "name": "Montreal"},
                ],
                "layout": {"title": "Dash Data Visualization"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
