"""
THE BASE MLCHAIN SERVER 
"""
# Import mlchain 
from mlchain.base import ServeModel
from mlchain import mlconfig 


# IMPORT YOUR CLASS HERE - YOU ONLY CARE THIS
from classifier import classfier # Import your class here 

model = classfier(mlconfig.model_path, mlconfig.labels) # Init your class first 
# END YOUR WORK HERE


# Wrap your class by mlchain ServeModel
serve_model = ServeModel(model)

# THEN GO TO CONSOLE: 
# mlchain run -c mlconfig.yaml 