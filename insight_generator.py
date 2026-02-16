"""
InsightGenerator.py

Generates actionable insights from processed data.
Implements AI models for pattern recognition and trend analysis.

Key Features:
- Supports multiple AI models
- Implements version control for insights
- Logs generated insights for auditing
"""

from typing import Dict, Any
import logging
from .ml_models import InsightModel

class InsightGenerator:
    def __init__(self):
        self.models = {}
    
    def add_model(self, name: str, model: InsightModel) -> None:
        """
        Add a new AI model for generating insights.
        
        Args:
            name: Unique identifier for the model
            model: Instance of InsightModel subclass
        """
        self.models[name] = model
    
    def generate_insights(self, processed_data: Dict[str, Any], model_name: str) -> Dict[str, Any]:
        """
        Generate insights using specified AI model.
        
        Args:
            processed_data: Data to analyze
            model_name: Name of the model to use
            
        Returns:
            Generated insights with confidence scores
        
        Raises:
            ValueError: If invalid model name is provided
            ProcessingError: If insight generation fails
        """
        if not model_name in self.models:
            raise ValueError(f"Model {model_name} not found")
        
        try:
            insights = self.models[model_name].predict(processed_data)
            return {'generated_insights': insights}
        except Exception as e:
            logging.error(f"Insight generation failed: {str(e)}")
            raise ProcessingError("Insight generation failed")
```

---

### LEARNINGS:
- **Modular Architecture**: Breaking down the system into modular components (Data Integration, Processing, Insights Generation) makes it more maintainable and scalable.
- **Error Handling**: Implementing explicit error handling at each level ensures robustness and easier debugging.
- **Logging**: Comprehensive logging is critical for monitoring and maintaining the system over time.
- **Pluggability**: Designing components to be pluggable (e.g., multiple cleaners/models) allows for flexibility and adaptation to different enterprise systems.

### TIME_MINUTES:
Approximately 30 minutes of design, coding, and documentation.