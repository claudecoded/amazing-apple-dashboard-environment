import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Mock data synchronization
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

# Injecting FontAwesome stylesheet directly via CDN for Apple Watch sports icon simulation
app = dash.Dash(
    __name__, 
    external_stylesheets=[
        'https://codepen.io',
        'https://cloudflare.com'
    ]
)

app.layout = html.Div(style={'backgroundColor': '#000000', 'minHeight': '100vh', 'padding': '30px'}, children=[
    
    # Premium Apple Fitness Navigation Header
    html.Div([
        html.Div([
            html.H1([
                html.I(className="fa-solid(icon='apple-heart')", style={'color': '#FF2D55', 'marginRight': '12px'}),
                "Fitness Activity"
            ], style={'color': '#FFFFFF', 'margin': '0', 'fontWeight': '700', 'fontSize': '32px'}),
            html.P("Apple Watch Telemetry & Workout Insights Engine", style={'color': '#8E8E93', 'margin': '5px 0 0 0', 'fontSize': '15px'})
        ]),
        # Custom sport filter input
        html.Div([
            dcc.Dropdown(
                id='sport-filter',
                options=[{'label': f"🏅 {i}", 'value': i} for i in df['sport_type'].unique()],
                value=df['sport_type'].unique()[0],
                clearable=False,
                style={'width': '260px'}
            )
        ])
    ], style={'display': 'flex', 'justifyContent': 'space-between', 'alignItems': 'center', 'borderBottom': '1px solid #1C1C1E', 'paddingBottom': '20px', 'marginBottom': '30px'}),
    
    # Real-looking Apple Rings KPI Card Row Layout
    html.Div(id='cards-container', style={'display': 'flex', 'gap': '20px', 'marginBottom': '30px'}),
    
    # Interactive Analytical Graphs Grid Layout
    html.Div([
        html.Div([
            dcc.Graph(id='calories-trend-graph')
        ], className='six columns', style={'padding': '5px'}),
        
        html.Div([
            dcc.Graph(id='duration-distance-graph')
        ], className='six columns', style={'padding': '5px'}),
    ], className='row'),
])

@app.callback(
    [Output('cards-container', 'children'),
     Output('calories-trend-graph', 'figure'),
     Output('duration-distance-graph', 'figure')],
    [Input('sport-filter', 'value')]
)
def update_dashboard(selected_sport):
    filtered_df = df[df['sport_type'] == selected_sport].sort_values(by='start_date')
    
    total_workouts = len(filtered_df)
    total_calories = filtered_df['total_calories'].sum()
    total_time = filtered_df['duration'].sum()
    
    # Renderized structure injecting customized apple CSS styling classes
    cards = [
        html.Div(className="apple-card ring-move", children=[
            html.H4([html.I(className="fa-solid fa-fire", style={'marginRight': '8px'}), "MOVE"], style={'color': '#FF2D55', 'fontSize': '14px', 'margin': '0 0 10px 0', 'letterSpacing': '1px'}),
            html.H2(f"{total_calories} Kcal", style={'color': '#FFFFFF', 'margin': '0', 'fontWeight': '700'})
        ], style={'flex': '1'}),
        
        html.Div(className="apple-card ring-exercise", children=[
            html.H4([html.I(className="fa-solid fa-clock", style={'marginRight': '8px'}), "EXERCISE"], style={'color': '#00E676', 'fontSize': '14px', 'margin': '0 0 10px 0', 'letterSpacing': '1px'}),
            html.H2(f"{total_time:.1f} Min", style={'color': '#FFFFFF', 'margin': '0', 'fontWeight': '700'})
        ], style={'flex': '1'}),
        
        html.Div(className="apple-card ring-stand", children=[
            html.H4([html.I(className="fa-solid fa-dumbbell", style={'marginRight': '8px'}), "SESSIONS"], style={'color': '#007AFF', 'fontSize': '14px', 'margin': '0 0 10px 0', 'letterSpacing': '1px'}),
            html.H2(f"{total_workouts} Workouts", style={'color': '#FFFFFF', 'margin': '0', 'fontWeight': '700'})
        ], style={'flex': '1'}),
    ]
    
    # Chart styling configurations overrides to force seamless integration with pure black layout
    fig_calories = px.bar(
        filtered_df, x='start_date', y='total_calories',
        title=f'Active Caloric Burn Trend — {selected_sport}',
        template='plotly_dark'
    )
    fig_calories.update_layout(
        plot_bgcolor='#1C1C1E', paper_bgcolor='#1C1C1E', 
        colorway=['#FF2D55'], font_family="-apple-system",
        margin=dict(l=40, r=20, t=50, b=40)
    )
    
    fig_specs = px.scatter(
        filtered_df, x='duration', y='total_distance', size='total_calories',
        title=f'Workout Volume Mapping — {selected_sport}',
        template='plotly_dark'
    )
    fig_specs.update_layout(
        plot_bgcolor='#1C1C1E', paper_bgcolor='#1C1C1E', 
        colorway=['#00E676'], font_family="-apple-system",
        margin=dict(l=40, r=20, t=50, b=40)
    )
    
    return cards, fig_calories, fig_specs

if __name__ == '__main__':
    app.run_server(debug=True)
