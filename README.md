# Foodwaste-PaddleSeg
## Structure
```
.
├── README.md
├── data
│   ├── exceptional
│   └── normal
├── dataset
│   ├── images
│   ├── labels
│   ├── test_list.txt
│   ├── train_list.txt
│   └── val_list.txt
├── origin_data
│   ├── 异常数据
│   └── 正常数据
├── output
│   └── analyze
└── work
    ├── analyze.py
    ├── partiton.py
    └── preprocess.py
```
## Normalization
```
[0, 32) -> 0
[32, 96) -> 64
[96, 160) -> 128
[160, 224) -> 192
[224, 256) -> 255
```

## Illustration
```
蓝(0， 0， 128)：塑料袋
紫(64, 0, 128)：纸
黄(128, 128, 0)：泡沫
深红(128, 0, 0)：罐子
红(192, 0, 0)：纸
绿(0, 128, 0)：瓶子
灰(128, 128, 128)：杯子
深黄(192, 128, 0)：利乐包
粉(128, 0, 128)：水果泡沫网
淡蓝(64, 128, 128)：方便面盒子
```

## 标注协议

PaddleSeg采用单通道的标注图片，每一种像素值代表一种类别，像素标注类别需要从0开始递增，例如0，1，2，3表示有4种类别。标注类别最多为256类。

PaddleSeg支持伪彩色图作为标注图片，在原来的单通道图片基础上，注入调色板。在基本不增加图片大小的基础上，却可以显示出彩色的效果。

## Scripts

### 训练

```
python train.py \
       --config configs/quick_start/bisenet.yml \
       --do_eval \
       --use_vdl \
       --save_interval 500 \
       --save_dir output
```

### 验证

```
python val.py \
       --config configs/quick_start/bisenet.yml \
       --model_path output/best_model/model.pdparams
```

### 预测

```
python predict.py \
       --config configs/quick_start/bisenet.yml \
       --model_path output/best_model/model.pdparams \
       --image_path dataset/images/1057628.png \
       --save_dir output/result
```

### 配置策略

```yaml
batch_size: 4
iters: 1000

train_dataset:
  type: Dataset
  dataset_root: dataset
  train_path: dataset/train_list.txt
  num_classes: 10
  transforms:
    - type: Resize
      target_size: [512, 512]
    - type: RandomHorizontalFlip
    - type: Normalize
  mode: train

val_dataset:
  type: Dataset
  dataset_root: dataset
  val_path: dataset/val_list.txt
  num_classes: 10
  transforms:
    - type: Resize
      target_size: [512, 512]
    - type: Normalize
  mode: val

optimizer:
  type: sgd
  momentum: 0.9
  weight_decay: 4.0e-5

lr_scheduler:
  type: PolynomialDecay
  learning_rate: 0.01
  end_lr: 0
  power: 0.9

loss:
  types:
    - type: CrossEntropyLoss
  coef: [1, 1, 1, 1, 1]

model:
  type: BiSeNetV2
  pretrained: Null
```
