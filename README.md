# Foodwaste-PaddleSeg
## Structure
```
.
├── README.md
├── data
│   ├── 异常数据
│   └── 正常数据
├── dataset
│   ├── exceptional
│   └── normal
└── work
    ├── analyze.py
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
红(192, 0, 0)：罐子
绿(0, 128, 0)：瓶子
其它：杯子、利乐包、水果泡沫网、方便面盒子
```

