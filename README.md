https://github.com/YoshimiNana/AutoDrive_PBL/assets/93458998/ae81d4e8-1171-40a4-bd60-777e369751ad
## 自動運転の概要
* JetRacer（NVIDIA Jetson Nano を搭載した AI レースカー）によって自動運転を行う  
* 基本的なプログラムは公式の [NVIDIA AI IOT](https://github.com/NVIDIA-AI-IOT/jetracer) から使用  
## 実装した内容
1. データの取得  
   車の前方に搭載したカメラから画像を取得

2. モデルの学習  
   CNNの分類モデルを定義。  
   取得した画像を利用して、8方向の多クラス分類の学習を行う。
   - 道を曲がりきれないときに、バックによる切り返しが可能
   - 8方向のラベル：東・西・南・北・北東・北西・南東・南西

3. 自動運転  
   リアルタイムで車の前方のカメラから画像を取得。  
   学習したモデルで車が進む方向を予測。（PBL_smp.ipynb）  

  

