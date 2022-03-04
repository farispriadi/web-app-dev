import dash
from dash import html
from dash import dcc

# Untuk meenghubungkan model perlu menambahkan import ini
from dash.dependencies import Input, Output, State

# Numpy untuk model perhitungan 
import numpy as np

# Model sederhana berupa fungsi untuk mengenerate 
def get_P_data(start,end, step):
    P = np.linspace(start,end,step)
    return P

def get_T_data(start,end, step):
    T = np.linspace(start,end,step)
    return T


layout = dict(
    autosize=True,
    automargin=True,
    margin=dict(l=60, r=30, b=50, t=10),
    plot_bgcolor= "#8a92b5",
    paper_bgcolor="#b6bcd6",
    hovermode="closest",
    xaxis = dict(title='Pressure (psig)'),
    yaxis = dict(title='Temperature (F)'),
    legend=dict(x=0.1, y=1.2),
    font=dict(
        color="navy"
    )
)

# dash object
app = dash.Dash(__name__)
server = app.server

# layout
app.layout = html.Div([
                        # Div Utama
                        html.Div(
                          [html.H3("Header Block")], 
                          style={'background-color':'#b6bcd6', 
                                  # 'border': '4px #8a92b5 solid',
                                  'width': '100%'}
                        ),

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
                                            # 'border': '4px #8a92b5 solid',
                                            'display':'flex',
                                            'flex-wrap': 'wrap',
                                            'width': '500px',
                                            }   
                                ),
                                html.Div(
                                    [   html.Div([html.H3("Result Block")]),
                                        dcc.Graph(id='plot', 
                                        figure={
                                                    "data": [],
                                                    "layout": layout,
                                                },)
                                    ], 
                                    style={'background-color':'#b6bcd6',
                                            # 'border': '4px #8a92b5 solid',
                                            'width': '600px',
                                            # 'height': '200px',
                                            }
                                ),
                            ],
                            style={'background-color':'#b6bcd6', 
                                    # 'border': '4px #8a92b5 solid',
                                    'width': '100%',
                                    'display': 'flex',
                                    'flex-wrap': 'wrap',}
                        ),

                        html.Div(
                          [html.H3("Footer Block")], 
                          style={'background-color':'#b6bcd6', 
                                  # 'border': '4px #8a92b5 solid',
                                  'width': '100%'}
                        ),

                    ],
                    style={'background-color':'#b6bcd6"', 
                            'padding':'10px 10px 10px 10px',
                            'height': '100%',
                            'display': 'flex',
                            'flex-wrap': 'wrap',
                            'text-align':'center'}
                )

@app.callback(Output('plot','figure'),
        [Input('calculate','n_clicks')],
        [
            State('p-start', 'value'),
            State('p-end', 'value'),
            State('t-start', 'value'),
            State('t-end', 'value'),
            State('step', 'value')
        ]
    )
def update_result(n_clicks,p_start,p_end,t_start,t_end,step):
    if n_clicks >=1:
        P_data = get_P_data(p_start,p_end,step)
        T_data = get_T_data(t_start,t_end,step)
        
        data = [
                dict(
                    type="scatter",
                    x=P_data, 
                    y= T_data,
                    mode='lines+markers',
                    line=dict(width=1, color='navy'),
                    labels=["Pressure (psig)", "Temperature (F)"],
                    name="P vs T"
                ),

            
                
            ]

        layout["showlegend"] = True
        layout["autosize"] = True
        layout["xaxis"] = dict(title='Pressure (psig)')
        layout["yaxis"] = dict(title='Temperature (F)')
    else:
        data = []
        
    figure = dict(data=data, layout=layout)

    return figure
        
# main
if __name__ == "__main__":
    app.run_server(debug=False)