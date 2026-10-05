import xml.etree.ElementTree as ET
import pandas as pd

def parse_apple_health_workouts(xml_path):
    """
    Parses the Apple Health export.xml file focusing specifically on 
    activity records and sports data (Workouts).
    """
    print("Starting Apple XML data file parsing...")
    context = ET.iterparse(xml_path, events=('end',))
    
    workout_list = []
    
    for event, elem in context:
        if elem.tag == 'Workout':
            # Extract main sports attributes collected by the Apple Watch
            workout_data = {
                'sport_type': elem.get('workoutActivityType'),
                'duration': float(elem.get('duration', 0)), # in minutes
                'duration_unit': elem.get('durationUnit'),
                'total_distance': float(elem.get('totalDistance', 0)),
                'distance_unit': elem.get('totalDistanceUnit'),
                'total_calories': float(elem.get('totalEnergyBurned', 0)), # Kcal
                'energy_unit': elem.get('totalEnergyBurnedUnit'),
                'start_date': pd.to_datetime(elem.get('startDate')),
                'end_date': pd.to_datetime(elem.get('endDate')),
                'source_device': elem.get('sourceName') # e.g., Apple Watch
            }
            workout_list.append(workout_data)
            
            # Clear element from memory to optimize handling huge XML files
            elem.clear()
            
    df = pd.DataFrame(workout_list)
    
    # Quick clean-up of activity types (Removes Apple's default prefix)
    if not df.empty:
        df['sport_type'] = df['sport_type'].str.replace('HKWorkoutActivityType', '')
        
    return df

# Example of isolated usage:
# df_sports = parse_apple_health_workouts('export.xml')
# df_sports.to_csv('my_workouts.csv', index=False)
