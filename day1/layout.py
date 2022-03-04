import dash
from dash import html
from dash import dcc

# dash object
app = dash.Dash(__name__)
server = app.server

# layout
app.layout = html.Div([
                        #Div Utama
                        html.Div(
                            [html.H3("Div Atas")], 
                            style={'background-color':'#b6bcd6', 
                                    'border': '4px #8a92b5 solid',
                                    'width': '100%'}
                        ),
                        html.Div(
                            # Div Tengah 
                            [
                                html.Div(
                                    [html.H3("Div Kiri")], 
                                    style={'background-color':'#b6bcd6', 
                                            'border': '4px #8a92b5 solid',
                                            'width': '500px',
                                            'height': '200px'}
                                ),
                                html.Div(
                                    [html.H3("Div Kanan")], 
                                    style={'background-color':'#b6bcd6',
                                            'border': '4px #8a92b5 solid',
                                            'width': '600px',
                                            'height': '200px'}
                                ),

                            ], 
                            style={'background-color':'#b6bcd6', 
                                    'border': '4px #8a92b5 solid',
                                    'width': '100%',
                                    'display': 'flex',
                                    'flex-wrap': 'wrap',}
                        ),
                        
                        html.Div(
                            [html.H3("Div Bawah")], 
                            style={'background-color':'#b6bcd6', 
                                    'border': '4px #8a92b5 solid',
                                    'width': '100%'}
                        ),

                    ],
                    style={'background-color':'#d1d4e3', 
                            'padding':'10px 10px 10px 10px',
                            'display': 'flex',
                            'flex-wrap': 'wrap',
                            'text-align':'center'}
                )

# main
if __name__ == "__main__":
    app.run_server()