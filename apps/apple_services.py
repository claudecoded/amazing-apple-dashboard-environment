import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

def get_apple_services_layout():
    """
    Generates the UI layout for the complete Apple Connected Ecosystem Hub,
    tracking App Store, Apple TV, Creator Studio subscriptions, system settings,
    and background application states.
    """
    # Dataset mapping active background storage and usage for expanded services
    services_data = {
        'Application / Platform': [
            'Apple Creator Studio (Final Cut/Logic)', 
            'Minecraft (iOS & macOS Save State)', 
            'Apple TV Streaming Cache', 
            'App Store Purchased Packages', 
            'Weather System Telemetry', 
            'System Settings & Cloud Profiles'
        ],
        'Storage Used (GB)': [45.2, 12.8, 28.4, 18.1, 2.5, 4.2]
    }
    df_services = pd.DataFrame(services_data)
    
    # Advanced data distribution donut chart
    fig_services = px.pie(
        df_services, 
        values='Storage Used (GB)', 
        names='Application / Platform', 
        hole=0.4, 
        template='plotly_dark'
    )
    
    fig_services.update_layout(
        plot_bgcolor='#1C1C1E', 
        paper_bgcolor='#1C1C1E', 
        font_family="-apple-system, BlinkMacSystemFont, Arial",
        colorway=['#FF2D55', '#4CD964', '#5AC8FA', '#007AFF', '#FF9500', '#8E8E93'],
        margin=dict(l=20, r=20, t=20, b=20)
    )

    # Core interface layout matrix
    layout = html.Div(style={'backgroundColor': '#000000', 'color': '#FFFFFF'}, children=[
        html.H2("Expanded Connected Apple Services Hub", style={'color': '#FFFFFF', 'fontWeight': '700', 'margin': '0 0 5px 0'}),
        html.P("Real-time subsystem monitoring, application deployment, and sandbox profile syncing.", style={'color': '#8E8E93', 'fontSize': '15px', 'marginBottom': '30px'}),
        
        # Upper Matrix: App Store, Apple TV, and Minecraft Environment Services
        html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '20px'}, children=[
            
            # App Store Telemetry Card Component
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #007AFF', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("🏪 App Store", style={'color': '#007AFF', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("Updates: All Current", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Linked Token: 24 active app runtimes", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ]),
            
            # Apple TV Subsystem Streaming Card Component
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #FF9500', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("📺 Apple TV Platform", style={'color': '#FF9500', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("Stream Mode: Up to Date", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Active pipeline: Linked to Sports App", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ]),
            
            # Minecraft Cross-Platform Container Sync Card Component
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #4CD964', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("🎮 Minecraft (iOS/macOS)", style={'color': '#4CD964', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("iCloud Save State: Synced", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Worlds detected: 3 active metadata logs", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ])
        ]),

        # Lower Matrix: Apple Creator Studio, Weather (Clima), and Settings Subsystems
        html.Div(style={'display': 'flex', 'gap': '20px', 'marginBottom': '30px'}, children=[
            
            # Apple Creator Studio Professional App Bundle Card Component (Final Cut, Logic, Pixelmator Pro)
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #FF2D55', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("🎨 Apple Creator Studio", style={'color': '#FF2D55', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("License: Active Subscription", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Unlocked: Final Cut Pro & Pixelmator Pro", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ]),
            
            # Weather System Live Telemetry Sync Card Component
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #5AC8FA', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("☀️ Weather Telemetry (Clima)", style={'color': '#5AC8FA', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("Sync Status: Real-time Live", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Maringá, PR: 24°C - Atmospheric logs active", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ]),
            
            # System Settings Config Container Card Component
            html.Div(className="apple-card", style={'flex': '1', 'borderLeft': '4px solid #8E8E93', 'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '20px', 'border': '1px solid #2C2C2E'}, children=[
                html.H4("⚙️ Settings Subsystem", style={'color': '#8E8E93', 'margin': '0 0 10px 0', 'fontSize': '13px', 'letterSpacing': '1px', 'fontWeight': 'bold'}),
                html.H3("Environment: Validated", style={'margin': '0 0 5px 0', 'fontSize': '18px', 'fontWeight': '700'}),
                html.P("Apple Account Profiles: Secured via Sandbox", style={'color': '#8E8E93', 'margin': '0', 'fontSize': '14px'})
            ])
        ]),
        
        # Dedicated Graphic Data Distribution Allocation Panel Visual Component
        html.Div(style={'backgroundColor': '#1C1C1E', 'borderRadius': '14px', 'padding': '24px', 'border': '1px solid #2C2C2E'}, children=[
            html.H4("Cross-Platform Application & Ecosystem Storage Distribution", style={'margin': '0 0 15px 0', 'fontSize': '18px', 'fontWeight': '700'}),
            dcc.Graph(figure=fig_services)
        ])
    ])
    return layout
