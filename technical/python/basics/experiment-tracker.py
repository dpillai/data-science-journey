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

# Let's use it
tracker = ExperimentTracker()

# Dictionary with typical ML parameters
model_params = {
    'learning_rate': 0.01,
    'epochs': 100,
    'batch_size': 32
}

# Log some experiments
tracker.log_experiment(
    model_name="SimpleNN",
    parameters=model_params,
    accuracy=0.85,
    notes="First try"
)

# Using dictionary unpacking to modify parameters
tracker.log_experiment(
    model_name="SimpleNN",
    parameters={**model_params, 'learning_rate': 0.001},  # Modified learning rate
    accuracy=0.88,
    notes="Lower learning rate"
)

# Print status
print(tracker)
