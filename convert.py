import torch
from models.model import Face_classify_nnModel

model = Face_classify_nnModel(3, 10)

model.load_state_dict(torch.load('weights/model_face_classification.pth', map_location=torch.device('cpu')))

model = torch.jit.script(model)

model.save('face_classification_script.pt')