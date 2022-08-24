from cProfile import label
from pickletools import uint8
import torch
from torchvision import transforms as T
import numpy as np
import cv2
from PIL import Image
torch.set_grad_enabled(False)

class classfier:
    def __init__(self, model_path, labels):
        self.model = torch.jit.load(model_path)

        self.labels = labels

        self.transform = transformer = T.Compose(
            [T.Resize((32, 32), interpolation = T.InterpolationMode.BICUBIC),
            T.ToTensor(),
            T.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])]
        )

    def forward(self, img: torch.Tensor):
        res = self.model(img)
        return res

    def _preprocessing(self, img: np.ndarray) -> torch.Tensor:
        process_img = Image.fromarray(img)
        process_img = self.transform(process_img)
        return process_img

    def predict_single_image(self, img: np.ndarray):
        process_img = self._preprocessing(img)
        process_img = torch.unsqueeze(process_img, dim=0)

        out = self.forward(process_img)

        out = torch.nn.Softmax(dim=1)(out)

        idx = out.argmax(dim=1).item()

        res = {
            "class_name": self.labels[idx],
            "confidence_score": out[0][idx].item()
        }

        return res

if __name__ == '__main__':
    rand_in = np.random.randint(255, size=(224, 224, 3), dtype=np.uint8)

    model = classfier('face_classification_script.pt')

    print(model.predict_single_image(rand_in))