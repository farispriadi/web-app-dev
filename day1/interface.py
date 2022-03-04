import dash
from dash import html
from dash import dcc

# dash object
app = dash.Dash(__name__)
server = app.server

# layout
app.layout = html.Div([
                        #Div Utama
                        # html.Div(
                        #   [html.H3("Header Block")], 
                        #   style={'background-color':'#b6bcd6', 
                        #           'border': '4px #8a92b5 solid',
                        #           'width': '100%'}
                        # ),
                        html.Div(
                            # Div Tengah 
                            [
                                html.Div(
                                    [
                                        # html.H3("User Input Block"),
                                        # style={'background-color':'#b6bcd6', 
                                        #   'border': '4px #8a92b5 solid',
                                        #   'width': '500px',
                                        #   'height': '200px'}  

                                        html.Div(
                                                html.H3("User Input Block"),
                                                style={
                                                    'width': '100%'
                                                    }
                                            ),
                                        # Div Label
                                        html.Div([
                                                    html.Label(""),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    html.Label("Pressure (psig)"),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    html.Label("Temperature (F)"),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),

                                        # Div Start Range
                                        html.Div([
                                                    html.Label("From"),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    dcc.Input(id='p-start', value=0,type='number'),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    dcc.Input(id='t-start', value=0,type='number'),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),

                                        # Div End Range
                                        html.Div([
                                                    html.Label("To"),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    dcc.Input(id='p-end', value=0,type='number'),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    dcc.Input(id='t-end', value=0,type='number'),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),

                                        # Div Step Range
                                        html.Div([
                                                    html.Label("Step"),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    dcc.Input(id='step', value=0,type='number'),
                                                ],
                                                style={
                                                    'width': '60%',
                                                    'padding-top': '4px',
                                                    'text-align' : 'left'
                                                    }
                                            ),

                                        # Div Button
                                        html.Div([
                                                    html.Label(" "),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                        html.Div([
                                                    html.Button("Run",
                                                        id='calculate',
                                                        n_clicks=0, 
                                                        style={
                                                                'width': '40%',
                                                            }),
                                                ],
                                                style={
                                                    'width': '100%',
                                                    'padding-top': '20px',
                                                    # 'padding-left': '50px',
                                                    # 'text-align':'right'

                                                    }
                                            ),
                                        html.Div([
                                                    html.Label(" "),
                                                ],
                                                style={
                                                    'width': '30%',
                                                    'padding-top': '4px'
                                                    }
                                            ),
                                    ], 
                                    style={'background-color':'#b6bcd6', 
                                            'border': '4px #8a92b5 solid',
                                            'display':'flex',
                                            'flex-wrap': 'wrap',
                                            'width': '500px',
                                            }   
                                ),
                                html.Div(
                                    [   html.Div([html.H3("Result Block")]),
                                        dcc.Graph(id='plot', 
                                        figure={'data': [ 
                                                {'x':[1,2,3], # menggunakan low level interface (list & dict)
                                                'y':[1,4,9], 
                                                'marker':{
                                                            'color':'navy'
                                                        },                                      
                                                'name':'simple line'},

                                            ],
                                            'layout': {
                                                'title' : 'P vs T',
                                                'plot_bgcolor': '#8a92b5',
                                                'paper_bgcolor': '#b6bcd6',
                                                'responsive': 'auto',
                                                'font': {'color': 'black'},
                                            }
                                        })
                                    ], 
                                    style={'background-color':'#b6bcd6',
                                            'border': '4px #8a92b5 solid',
                                            'width': '600px',
                                            # 'height': '200px',
                                            }
                                ),
                            ],
                            style={'background-color':'#b6bcd6', 
                                    'border': '4px #8a92b5 solid',
                                    'width': '100%',
                                    'display': 'flex',
                                    'flex-wrap': 'wrap',}
                        ),
                        # html.Div(
                        #   [html.H3("Footer Block")], 
                        #   style={'background-color':'#b6bcd6', 
                        #           'border': '4px #8a92b5 solid',
                        #           'width': '100%'}
                        # ),

                    ],
                    style={'background-color':'#d1d4e3', 
                            'padding':'10px 10px 10px 10px',
                            'height': '100%',
                            'display': 'flex',
                            'flex-wrap': 'wrap',
                            'text-align':'center'}
                )

# main
if __name__ == "__main__":
    app.run_server()