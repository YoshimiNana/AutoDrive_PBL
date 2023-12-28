## 自動運転の概要
* JetRacer（NVIDIA Jetson Nano を搭載した AI レースカー）によって自動運転を行う  
* 基本的なプログラムは公式の [NVIDIA AI IOT](https://github.com/NVIDIA-AI-IOT/jetracer) から使用  
## 実装した内容
* CNNのモデルを定義
* 車の前方に搭載したカメラから画像を取得
* 学習した画像を8方向に多クラス分類 → 車が進む方向を自動で予測（PBL_smp.ipynb）
  * 道を曲がりきれないときに、バックによる切り返しが可能
  * 8方向のラベル：東・西・南・北・北東・北西・南東・南西

https://github.com/YoshimiNana/AutoDrive_PBL/assets/93458998/ae81d4e8-1171-40a4-bd60-777e369751ad

