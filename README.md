# 一、项目背景介绍
Gazebo是一个较为强大的仿真软件，它通常跟ros一起用到。如今自动驾驶飞速发展，我们在自动驾驶时不可能直接使用实物，因为那样造成的人力物力的损失十分大。因此我们需要使用仿真来验证我们的算法，然后才是实物的验证。锥桶作为日常的交通信号被准确检查出来十分必要，使用gazebo开括算法验证的平台等。

# 二、数据介绍
本次数据集采用的是在AI studio上开源的数据集。符合VOC格式，在对基于PaddleX开发目标检测模型时，无需对数据格式进行转换。并且包含在gazebo中的桶锥的几百张图片，比较丰富。下面包含图像展示的程序imageshow.py。

# 三、模型介绍
由于本次项目使用的是paddlepaddle上的PaddleX套件。PaddleX目前提供了FasterRCNN和YOLOv3和PPYOLO三种检测结构，多种backbone模型。***本基线系统以骨干网络为ResNet50vdssld的PPYOLO算法为例。***
Paddle开源了相比于YOLOv4速度更快、精度更高的PP-YOLO模型，下面是PP-YOLO模型和目前SOTA的目标检测算在COCO test-dev数据集的精度和V100上预测速度的对比图。
    <div align="center">
  <img src="https://ai-studio-static-online.cdn.bcebos.com/2b3d6009198346078cc5e735839a579f32a58edaf25344fe96d3ad3efe79940b" width=500>
</div>
PP-YOLO是Paddle里基于YOLOv3精度速度优化的实战实践，通过几乎不增加预测计算量的优化方法尽可能地提高YOLOv3模型的精度，最终在COCO test-dev2017数据集上精度达到45.9%，单卡V100预测速度为72.9FPS，下表为PP-YOLO和YOLOv4模型在不同尺度输入下精度和速度的对比。
<div align="center">
  <img src="https://ai-studio-static-online.cdn.bcebos.com/f0effff830c64e90a0ea228ef5a8504dbe98be12350946fc96a640c08eec00dc" width=600>
</div>
注： 上表中数据均为在单卡Tesla V100上batch size=1测试结果，TRT-FP16为使用TensorRT且在FP16上的测试结果，TensorRT版本为5.1.2.2

# 四、模型训练
首先安装paddleX:
`pip install paddlex==1.3.10 rc -i https://mirror.baidu.com/pypi/simple`

然后通过train.py进行训练。

# 五、模型评估
训练模型后我们便可以通过test.py得出效果如图：


![image](https://user-images.githubusercontent.com/78524771/155888023-5aa200c3-9e82-4477-92c9-2891677599d4.png)
