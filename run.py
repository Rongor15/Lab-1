import dash_bootstrap_components as dbc

from dash import Dash, Input, Output, dcc, html
from pages import test, students, country


external_stylesheets = [dbc.themes.MINTY]  
run = Dash(__name__, external_stylesheets=external_stylesheets,  use_pages=True)
run.config.suppress_callback_exceptions = True


SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "19rem",
    "padding": "2rem 1rem",
    "background-color": "#1a4876", 
}


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Олимпиада по математике", className="display-6"),

        html.Hr(),
        html.P(
            "Учебный проект студентов БСБО-14-21", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Задачи", href="/", active="exact"),
                dbc.NavLink("Студенты", href="/page-1", active="exact"),
                dbc.NavLink("Карта", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)
content = html.Div(id="page-content", style=CONTENT_STYLE)

run.layout = html.Div([dcc.Location(id="url"), sidebar, content])
@run.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return test.layout
    elif pathname == "/page-1":
        return students.layout
    elif pathname == "/page-2":
        return country.layout
    # Если пользователь попытается перейти на другую страницу, верните сообщение 404. Мы изменим её в следующей практической.
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )
if __name__ == '__main__':
        run.run_server(debug=True)