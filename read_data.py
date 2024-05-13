from torch.utils.data import Dataset
from PIL import Image
import os
class Mydata(Dataset):
    def __init__(self, root_dir, label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path=os.path.join(self.root_dir,self.label_dir)
        self.img_path = os.listdir(self.path)

    def __getitem__(self, idx):
     img_name = self.img_path[idx]
     img_item_path = os.path.join(self.root_dir,self.labei_dir,img_name)
     img = Image.open(img_item_path)
     label = self.labei_dir
     return img, label
    def __len__(self):
        return len(self,img_path)

root_dir = "hymenoptera_data/train"
ants_label_dir = "ants"
ants_dataset = Mydata(root_dir,ants_label_dir)
print(ants_dataset)
train_dataset = ants_dataset