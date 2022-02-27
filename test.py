import paddlex as pdx
import matplotlib.pyplot as plt 
import cv2

test_transforms = transforms.Compose([
    # 此处需要补充图像预处理代码
    transforms.Normalize(),
    transforms.ResizeByShort(),
    transforms.Resize(1024),
    transforms.RandomDistort()
])
model = pdx.load_model('output/PPYOLO_mobilenetv1/epoch_140')
image_name = 'data/barricade/JPEGImages/train_144.jpg'
result = model.predict("data/barricade/JPEGImages/train_144.jpg",transforms=test_transforms)
pdx.det.visualize(image_name, result, threshold=0.2, save_dir='./output/ResNet50_vd_ssld')

infer_img = cv2.imread("output/ResNet50_vd_ssld/visualize_train_144.jpg")
tra = cv2.cvtColor(infer_img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(15,10))
plt.imshow(tra)
plt.show()
