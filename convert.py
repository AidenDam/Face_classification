import torch
from model import Face_classifi_nnModel

model = Face_classifi_nnModel(3, 10)

model.load_state_dict(torch.load('model_face_classifile.pth', map_location=torch.device('cpu')))

model = torch.jit.script(model)

model.save('face_classification_script.pt')