import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# ---------------------------------------------------------------------------
# Mock data simulation for instant execution of the clone dashboard
# (Replace this section with the real DataFrame from parser.py when using your XML)
# ---------------------------------------------------------------------------
mock_data = {
    'sport_type': ['Running', 'Cycling', 'FunctionalStrengthTraining', 'Running', 'Cycling', 'Swimming'],
    'duration': [45.2, 60.0, 50.0, 30.5, 90.0, 45.0],
    'total_distance': [5.2, 22.1, 0.0, 3.8, 35.0, 1.5],
    'total_calories':,
    'start_date': pd.to_datetime(['2026-10-01 07:00:00', '2026-10-02 18:30:00', '2026-10-03 09:00:00', 
                                  '2026-10-04 06:45:00', '2026-10-05 10:00:00', '2026-10-05 16:00:00']),
    'source_device': ['Apple Watch', 'Apple Watch Ultra', 'Apple Watch', 'Apple Watch', 'Apple Watch Ultra', 'Apple Watch']
}
df = pd.DataFrame(mock_data)
# ---------------------------------------------------------------------------

# Initialize the Dashboard Web App
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io'])

app.layout = html.Div(style={'backgroundColor': '#121212', 'color': '#FFFFFF', 'padding': '25px', 'fontFamily': 'SF Pro Display, Arial'}, children=[
    
    # Apple Fitness style inspired UI Header
    html.Div([
        html.H1("Apple Sports & Activity Dashboard Clone", style={'color': '#FA243C', 'marginBottom': '5px'}),
        html.P("Offline sports telemetry analysis extracted from Apple Watch devices", style={'color': '#8E8E93', 'fontSize': '16px'}),
    ], style={'borderBottom': '1px solid #2C2C2E', 'paddingBottom': '15px', 'marginBottom': '25px'}),
    
    # Filters Grid section
    html.Div([
        html.Label("Select Sport Modality:", style={'fontWeight': 'bold', 'color': '#00E676'}),
        dcc.Dropdown(
            id='sport-filter',
            options=[{'label': i, 'value': i} for i in df['sport_type'].unique()],
            value=df['sport_type'].unique()[0],
            style={'color': '#000000', 'width': '300px', 'marginTop': '8px'}
        )
    ], style={'marginBottom': '30px'}),
    
    # Summary Metrics KPI Cards Container
    html.Div(id='cards-container', style={'display': 'flex', 'gap': '20px', 'marginBottom': '30px'}),
    
    # Main Interactive Visual Graphs Section
    html.Div([
        html.Div([
            dcc.Graph(id='calories-trend-graph')
        ], className='six columns', style={'backgroundColor': '#1C1C1E', 'borderRadius': '8px', 'padding': '10px'}),
        
        html.Div([
            dcc.Graph(id='duration-distance-graph')
        ], className='six columns', style={'backgroundColor': '#1C1C1E', 'borderRadius': '8px', 'padding': '10px'}),
    ], className='row'),
])

# Reactive Interface Control Callbacks 
@app.callback(
    [Output('cards-container', 'children'),
     Output('calories-trend-graph', 'figure'),
     Output('duration-distance-graph', 'figure')],
    [Input('sport-filter', 'value')]
)
def update_dashboard(selected_sport):
    # Filter dataset records based on interface choice
    filtered_df = df[df['sport_type'] == selected_sport].sort_values(by='start_date')
    
    # KPI Metrics calculations
    total_workouts = len(filtered_df)
    total_calories = filtered_df['total_calories'].sum()
    total_time = filtered_df['duration'].sum()
    
    # Structured HTML rendering for metrics cards
    cards = [
        html.Div([html.H4("Workouts"), html.H2(f"{total_workouts}")], style={'backgroundColor': '#1C1C1E', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'textAlign': 'center', 'borderLeft': '4px solid #FA243C'}),
        html.Div([html.H4("Total Energy"), html.H2(f"{total_calories} kcal")], style={'backgroundColor': '#1C1C1E', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'textAlign': 'center', 'borderLeft': '4px solid #00E676'}),
        html.Div([html.H4("Total Duration"), html.H2(f"{total_time:.1f} min")], style={'backgroundColor': '#1C1C1E', 'padding': '20px', 'borderRadius': '8px', 'flex': '1', 'textAlign': 'center', 'borderLeft': '4px solid #2F80ED'}),
    ]
    
    # Graph 1: Active Caloric Burn Historical Bar Chart
    fig_calories = px.bar(
        filtered_df, x='start_date', y='total_calories', text_auto=True,
        title=f'Active Energy Burned — {selected_sport}',
        labels={'start_date': 'Workout Date', 'total_calories': 'Active Calories (kcal)'},
        template='plotly_dark'
    )
    fig_calories.update_layout(plot_bgcolor='#1C1C1E', paper_bgcolor='#1C1C1E', colorway=['#FA243C'])
    
    # Graph 2: Training Volume Scatter Plot Relation (Time x Distance)
    fig_specs = px.scatter(
        filtered_df, x='duration', y='total_distance', size='total_calories', hover_data=['source_device'],
        title=f'Workout Volume (Duration x Distance) — {selected_sport}',
        labels={'duration': 'Duration (minutes)', 'total_distance': 'Distance Covered (km)'},
        template='plotly_dark'
    )
    fig_specs.update_layout(plot_bgcolor='#1C1C1E', paper_bgcolor='#1C1C1E', colorway=['#00E676'])
    
    return cards, fig_calories, fig_specs

if __name__ == '__main__':
    # Runs the local cloned server. Access via browser at http://127.0.0.1:8050
    app.run_server(debug=True)
