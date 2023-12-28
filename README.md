## 自動運転
* JetRacer（NVIDIA Jetson Nano を搭載した AI レースカー）によって自動運転を行う  
* 基本的なプログラムは公式の [NVIDIA AI IOT](https://github.com/NVIDIA-AI-IOT/jetracer) から使用  

* CNNを定義し、学習した画像を8方向に多クラス分類することで、車が進む方向を自動で予測する機能を搭載（PBL_smp.ipynb）
  * 道を曲がりきれないときに、バックによる切り返しが可能
  * 8方向のラベル：東・西・南・北・北東・北西・南東・南西

<img width="580" alt="image" src="https://github.com/YoshimiNana/AutoDrive_PBL/assets/93458998/2c1e945d-3fa4-4d2d-9aff-de0f3d0b7529">
