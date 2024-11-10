# Imports the pandas library and gives it the nickname 'pd'. Pandas is used for data analysis and manipulation.
import pandas as pd
from datetime import datetime
import csv

def load_and_analyze_fields(data_file):
    fields = []
    crop_yields = {}
    soil_types = set() #Using a set ensures we don't have duplicates

    data = read_field_data_pandas(data_file)
    #print(data)
    
    for field in data:
        field_id = str(field['field_id'])
        yield_value = float(field['yield'])
        planting_date = field['planting_date']
        crop_type = field['crop']
        soil_type = field['soil_type']

        fields.append({
        'field_id': field_id,
        'yield': yield_value,
        'crop' : crop_type,
        'soil_type': soil_type,
        'planting_date' : planting_date
        })

        if crop_type not in crop_yields:
                crop_yields[crop_type] = []
        crop_yields[crop_type].append(yield_value)

        soil_types.add(soil_type)

    analysis = {
         'total_fields': len(fields),
         'soil_types': list(soil_types),
         'crop_statistics': {},
         'high_yield_fields': []
    }

    for crop, yields in crop_yields.items():
         avg_yield = sum(yields)/len(yields)
         analysis['crop_statistics'][crop] = {
              'average_yield': round(avg_yield, 2),
              'total_fields': len(yields),
              'min_yield': round(min(yields), 2),
              'max_yield': round(max(yields),2)
         }

    return analysis

def read_field_data_pandas(filename):
    """
    Read field data from a CSV file using pandas
    """
    try:
        df = pd.read_csv(filename)
        #print(df)
        # Convert DataFrame to list of dictionaries
        return df.to_dict('records')
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading file: {e}")
        return None

def group_fields_by_soil(filename):
    results = read_field_data_pandas(filename)

    soil_types = set()
    field_list_by_soil = {}

    for field in results:
         soil_types.add(field['soil_type'])
    
    for type in list(soil_types):
        field_list_by_soil[type] = []
        for field in results:
             if type == field['soil_type']:
                  field_list_by_soil[type].append(str(field['field_id']))
    
    return field_list_by_soil

def get_earliest_planting_date(filename):
    results = read_field_data_pandas(filename)
    return min(field['planting_date'] for field in results)

results = load_and_analyze_fields("sample_data.csv")

print("\nField Analysis Results:")
print(f"Total Fields: {results['total_fields']}")
print(f"Soil Types: {', '.join(results['soil_types'])}")
print("\nCrop Statistics:")

for crop, stats in results['crop_statistics'].items():
    print(f"\n{crop}:")
    print(f"  Average Yield: {stats['average_yield']}")
    print(f"  Field Count: {stats['total_fields']}")
    print(f"  Yield Range: {stats['min_yield']} - {stats['max_yield']}")
    print(f"\nHigh Yield Fields: {', '.join(results['high_yield_fields'])}")

field_list_by_soil = group_fields_by_soil("sample_data.csv")

for soil,field_list in field_list_by_soil.items():
     print(f"\n{soil}:")
     print(f" Field list: {field_list}") 

print(get_earliest_planting_date("sample_data.csv"))