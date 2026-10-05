import os
import pandas as pd
import plotly.graph_objects as go

def load_ecg_recording(csv_file_path):
    """
    Reads a raw ECG text export file from Apple Watch hardware sensors.
    The file contains timestamps and microvolt readings.
    """
    if not os.path.exists(csv_file_path):
        return None
    
    # Apple Watch ECG exports typically contain headers in the first rows
    # skipping metadata to read actual signal waveforms
    df_ecg = pd.read_csv(csv_file_path, skiprows=12, names=['sample_index', 'microvolts'])
    return df_ecg

def generate_ecg_waveform(df_ecg):
    """Generates an interactive electrocardiogram chart."""
    if df_ecg is None or df_ecg.empty:
        return go.Figure()
        
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=df_ecg['sample_index'], 
        y=df_ecg['microvolts'], 
        mode='lines', 
        name='ECG Signal',
        line=dict(color='#FA243C', width=1.5)
    ))
    
    fig.update_layout(
        title="Apple Watch ECG Sensor Waveform Analysis",
        xaxis_title="Samples",
        yaxis_title="Voltage (µV)",
        template='plotly_dark',
        plot_bgcolor='#1C1C1E',
        paper_bgcolor='#1C1C1E'
    )
    return fig
