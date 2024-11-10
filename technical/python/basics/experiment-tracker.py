from sqlite3 import Timestamp
from tkinter import NONE
from typing import Dict, List, Optional
from datetime import date, datetime

class ExperimentTracker:
    def __init__(self) -> None:
        self.experiments: List[Dict] = []

    def log_experiment(
        self,
        model_name: str,
        parameters: Dict,
        accuracy: float,
        notes: Optional[str] = None
    ) -> None:
        if(param_count := len(parameters)) < 1:
            raise ValueError("Must provide atleast one parameter")
        
        experiment = {
            'Timestamp': datetime.now(),
            'model_name': model_name,
            'parameters': parameters,
            'accuracy': accuracy,
            'notes': notes,
            'param_count': param_count
        }
        self.experiments.append(experiment)

    def get_best_experiment(self) -> Dict:
        if not (exp_count := len(self.experiments)):
                raise ValueError("No experiments were logged")
        
        return max(self.experiments, key=lambda x: x['accuracy'])
    

    def __str__(self) -> str:
    # F-string with dictionary unpacking
        return f"""
            Experiment Tracker Status:
            {len(self.experiments)} experiments logged
            Best accuracy: {self.get_best_experiment()['accuracy']:.2f}
            """
    
    def get_failed_experiments(self) -> str:
        count_of_failed_experiments = sum( 1 for exp in self.experiments if exp['accuracy'] < 0.5)

        return f""" {count_of_failed_experiments} experiments failed"""


    def find_best_parameters(self, parameter_name: str) -> Dict:
        for exp in self.experiments:
                    
        best_experiment = max (self.experiments, key=lambda x : x[parameter_name])

        return f""" {best_experiment[parameter_name]} performed best with had the best average accuracy of {best.experiment['accuracy']} """



# Let's use it
tracker = ExperimentTracker()


tracker.log_experiment("CNN", {'learning_rate': 0.1}, 0.82)
tracker.log_experiment("CNN", {'learning_rate': 0.01}, 0.88)
tracker.log_experiment("CNN", {'learning_rate': 0.01}, 0.85)
best_params = tracker.find_best_parameters('learning_rate')

# # Dictionary with typical ML parameters
# model_params = {
#     'learning_rate': 0.01,
#     'epochs': 100,
#     'batch_size': 32
# }

# # Log some experiments
# tracker.log_experiment(
#     model_name="SimpleNN",
#     parameters=model_params,
#     accuracy=0.85,
#     notes="First try"
# )

# # Using dictionary unpacking to modify parameters
# tracker.log_experiment(
#     model_name="SimpleNN",
#     parameters={**model_params, 'learning_rate': 0.001},  # Modified learning rate
#     accuracy=0.88,
#     notes="Lower learning rate"
# )

# # Test 2; Erro Validation
# tracker.log_experiment(
#     model_name="SimpleNN",
#     parameters={'one kv pair': '.01'},
#     accuracy=0.85,
#     notes="First try"
# )

# tracker.log_experiment("TestModel", {'lr': 0.01}, 0.3, "Failed run")
# print(tracker.get_failed_experiments())
# Print status
print(tracker)
