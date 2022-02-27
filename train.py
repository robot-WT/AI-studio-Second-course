import os
from paddlex.det import transforms
import paddlex as pdx

# 定义训练和验证时的transforms
train_transforms = transforms.Compose([
    # 此处需要补充图像预处理代码
    transforms.Normalize(),
    #transforms.RandomHorizontalFlip(),
    transforms.ResizeByShort(),
    transforms.RandomDistort()
])
eval_transforms = transforms.Compose([
    # 此处需要补充图像预处理代码
    transforms.Normalize(),
    #transforms.Resize(26),
    #transforms.RandomHorizontalFlip(),
    transforms.ResizeByShort(),
    transforms.RandomDistort()
])
train_dataset = pdx.datasets.VOCDetection(
    data_dir='data/barricade/',
    file_list='data/barricade/train_data_list.txt',
    label_list='data/barricade/labels.txt',
    transforms=train_transforms,
    shuffle=True
)

model = pdx.det.PPYOLO(num_classes=len(train_dataset.labels), backbone='ResNet50_vd_ssld')
model.train(
    num_epochs=300,
    train_dataset=train_dataset,
    train_batch_size=16,
    learning_rate=0.000125,
    lr_decay_epochs=[210, 240],
    save_dir='output/PPYOLO_mobilenetv1')
