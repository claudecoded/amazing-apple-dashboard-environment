from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd

# Import local clone layout architectures
from app import app, update_dashboard
from ECG_analyze.ecg_service import load_ecg_recording, generate_ecg_waveform

# Main global layout with multi-page navigation router simulation
app.layout = html.Div(style={'backgroundColor': '#121212', 'color': '#FFFFFF', 'minHeight': '100vh', 'fontFamily': 'Arial'}, children=[
    dcc.Location(id='url', refresh=False),
    
    # Navigation Hub Header Layout
    html.Nav(style={'backgroundColor': '#1C1C1E', 'padding': '15px', 'display': 'flex', 'gap': '30px', 'borderBottom': '1px solid #2C2C2E'}, children=[
        dcc.Link('🏆 Sports & Workouts', href='/sports', style={'color': '#FFFFFF', 'textDecoration': 'none', 'fontWeight': 'bold'}),
        dcc.Link('❤️ Apple Watch ECG Analysis', href='/ecg', style={'color': '#FFFFFF', 'textDecoration': 'none', 'fontWeight': 'bold'})
    ]),
    
    # Dynamic content injection target
    html.Div(id='page-content', style={'padding': '25px'})
])

@app.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/ecg':
        # Render missing ECG UI analysis component layout view
        return html.Div([
            html.H2("Electrocardiogram Diagnostic View", style={'color': '#FA243C'}),
            html.P("Renders raw microvolt signals extracted from Apple Watch digital crown sensors.", style={'color': '#8E8E93'}),
            html.Div([
                # Isolated container for the missing dynamic graph element
                dcc.Graph(id='ecg-wave-display', figure=generate_ecg_waveform(load_ecg_recording('.import/sample_ecg.csv')))
            ], style={'backgroundColor': '#1C1C1E', 'borderRadius': '8px', 'padding': '20px', 'marginTop': '20px'})
        ])
    else:
        # Default route rolls back to standard dashboard grid structure view
        # Requires the existing app.layout subcomponents to render correctly here
        return html.Div("Navigate to sports using the toolbar menu hook options.")

if __name__ == '__main__':
    # Changes entry execution sequence point to mirror dieterich-lab structure setup
    app.run_server(host='0.0.0.0', port=8050, debug=True)
