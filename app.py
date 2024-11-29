import dash
from layouts.home_layout import layout
from callbacks.update_home import register_callbacks
import dash_bootstrap_components as dbc



app = dash.Dash(name=__name__,external_stylesheets=[dbc.themes.MINTY],
                assets_folder="Assets" ,
                title="DashBoard",
                update_title="DashBoard",)

# Set the layout
app.layout = layout
# Register callbacks
register_callbacks(app)


if __name__ == "__main__":
    app.run_server(debug=False)
