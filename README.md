## 自動運転
* JetRacer（NVIDIA Jetson Nano を搭載した AI レースカー）によって自動運転を行う  
* 基本的なプログラムは公式の [NVIDIA AI IOT](https://sites.google.com/view/ehime-nlp/) から使用  

* CNNを定義し、学習した画像を8方向に多クラス分類することで、車が進む方向を自動で予測する機能を搭載（道を曲がりきれないときに、バックして切り返すことができる）
  * north
  * northeast
  * east
  * southeast
  * south
  * southwest
  * west
  * northwest

