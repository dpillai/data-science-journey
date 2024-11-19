#Build a farm data management system

farm_data = {
    "field_101": {
        "name": "North Quarter",
        "crop": "corn",
        "acres": 145,
        "soil_type": "loam",
        "last_yield": 180,
        "inputs": {
            "nitrogen": 180,
            "phosphorus": 60,
            "potassium": 40
        }
    },
    "field_102": {
        "name": "River Bottom",
        "crop": "soybeans",
        "acres": 88,
        "soil_type": "silty clay",
        "last_yield": 55,
        "inputs": {
            "nitrogen": 0,
            "phosphorus": 40,
            "potassium": 60
        }
    }
}

#Calculate total acres
def calculate_total_acres():
    """Calculate total acres by crop"""
    crop_acres = {}
    for field_id, field in farm_data.items():
        crop = field["crop"]
        acres = field["acres"]
        print(f"{crop}, {acres}")

        crop_acres[crop] = crop_acres.get(crop,0) + acres
        print(crop_acres)
    return crop_acres


def estimate_yield_value(farm_data, prices={"corn": 4.50, "soybeans": 12.00}):

    total_value = 0
    for field_id, field in farm_data.items():
        crop = field["crop"]
        acres = field["acres"]
        last_yield = field["last_yield"]
        
        total_value += acres * last_yield * prices[crop]
    return total_value

def calculate_fertilizer_usage(farm_data):
    """Your code here"""
    fert_usage = {}
    for field_id, field in farm_data.items():
        inputs = field.get("inputs")
        if inputs:
            fert_usage["N"] = fert_usage.get("N",0) + (inputs["nitrogen"] * field["acres"])
            fert_usage["P"] = fert_usage.get("P",0) + (inputs["phosphorus"] * field["acres"])
            fert_usage["K"] = fert_usage.get("K",0) + (inputs["potassium"]  * field["acres"])
    return fert_usage 

def find_fields_by_criteria(farm_data, soil_type=None, min_acres=0):
    """Your code here"""
    fields = {}
    for field_id, field_details in farm_data.items():
        if field_details["soil_type"] == soil_type or field_details["acres"] >= min_acres:
            fields[field_id] = {"soil_type" : field_details["soil_type"],
                                "acres": field_details["acres"]}
    return fields

def calculate_input_costs_per_acre(farm_data, input_prices={"nitrogen": 0.65, "phosphorus": 0.70, "potassium": 0.45}):
    """Your code here"""
    cost_per_acre = {}
    for field_id, field_details in farm_data.items():
        inputs = field_details["inputs"]
        if inputs:
            cost = (inputs["nitrogen"] * input_prices["nitrogen"] +
                             inputs["phosphorus"] * input_prices["phosphorus"] +
                             inputs["potassium"] * input_prices["potassium"]) / field_details["acres"]
        cost_per_acre[field_id] = cost
    return cost_per_acre

# print(calculate_total_acres())
#print(estimate_yield_value(farm_data))
print(calculate_fertilizer_usage(farm_data))
#print(find_fields_by_criteria(farm_data, "silty clay", 90))
#print(calculate_input_costs_per_acre(farm_data))