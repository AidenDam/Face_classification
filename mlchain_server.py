from mlchain.base import ServeModel
from mlchain import mlconfig 

from classifier import Classfier 

model = Classfier(mlconfig.model_path, mlconfig.labels)

serve_model = ServeModel(model)