# Imports the pandas library and gives it the nickname 'pd'. Pandas is used for data analysis and manipulation.
import pandas as pd
from datetime import datetime

def load_and_analyze_fields(data):
    fields = []
    crop_yields = {}
    soil_types = set() #Using a set ensures we don't have duplicates
    
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
    
sample_data = [
    {'field_id': 'F001', 'crop': 'Corn', 'planting_date': '2024-04-15', 'soil_type': 'Loam', 'yield': 156.2},
    {'field_id': 'F002', 'crop': 'Soybeans', 'planting_date': '2024-05-01', 'soil_type': 'Clay', 'yield': 45.8},
    {'field_id': 'F003', 'crop': 'Corn', 'planting_date': '2024-04-18', 'soil_type': 'Sandy Loam', 'yield': 168.5}
]

results = load_and_analyze_fields(sample_data)

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