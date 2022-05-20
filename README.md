# xdu-TrafficLight
## 一、设计方案

1. 采用排队论模型生成车辆队列进行模拟

2. 红绿灯的时长控制和转换规则

   - 根据题目要求，南北走向的车流量是东西走向的两倍，考虑到车辆堆积问题，需对红绿灯时长进行合理控制。不妨设车辆直行、左转、右转比例一致，则南北车道包含两个直行车道，一个左转车道，直行绿灯时长应为左转时长的1/2。南北车道的车道数量和车流量均为东西车道两倍，考虑到东西车道右转和直行公用的车辆碰撞问题，直行和右转不能并行，故东西车道车辆更容易堆积，则东西绿灯时长为南北时长的3/2倍。设一次循环总时长为150s，则南北直行绿灯时长为20s，左转时长40s，右转绿灯常亮，红灯时长为90s；东西绿灯时长为90s，红灯时长为60s。
   - 转换规则参考大多数交通路口的红绿灯规则，循环自南北方向绿灯开始，先直行后左转，之后转红灯，右转绿灯常亮，东西方向红绿对应相反。

3. 验证方案假设：同一车道车辆积攒超过四辆归类为交通拥堵，通过计算总车辆拥堵时间对比方案性能。

4. 验证方案：通过平均时间分配与经过上述优化后的时间分配进行对比，根据泊松分布随机生成车辆队列到达时间与行驶方向，计算车辆拥堵时间对比时间分配性能，并通过时间优化率进行检验。

5. 输出展示方案

   采用 <a href="https://www.python.org/">Python</a> 语言的图像处理标准库 <a href="https://pillow.readthedocs.io/ ">Pillow</a> 制作 GIF 进行动画展示，或使用命令行检测验证方案。

   

   

## 二、测试方案

1. 运行50次测试比较平均优化性能，结果如下：

2. 

   <h1 align="center">
       <img src="https://i.jpg.dog/file/jpg-dog/fe044887ad097aabdc525fd11c7010fa.jpg" alt="XDU-tlsc" width="720">
   </h1>

   如图可见，纵轴是平均堵塞时间(s)，横轴为测试次数，我们的时间分配方案对应的堵塞时间(蓝色曲线)明显小于平均分配两方向红绿灯长度(红色曲线)，从而得知优化方案较为合理。

   <h1 align="center">
       <img src="https://i.jpg.dog/file/jpg-dog/296c46cfefa15a975ba463dd62892516.jpg" alt="XDU-tlsc" width="720">
   </h1>

   计算50次测试的时间优化率，可见对比平均分配红绿灯时长，我们的方案优化率大概能减少20%左右的堵塞时间。

3. 将每一帧动画输入在 process 文件夹下，对每一帧动画进行检查，确保对应无误。

4. 使用GIF进行动画效果展示。

   

   <h1 align="center">
       <img src="https://media.giphy.com/media/ED7vgf1krif6Awk1Sn/giphy.gif" alt="XDU-tlsc" width="480">
   </h1>

   

   
   

 

## 三、使用说明

1. 安装 Python 3 并勾选 Add Python to PATH 选项。

2. 使用 cmd 执行命令

   ~~~~
   pip install requirements.txt
   ~~~~

   安装运行环境依赖。

3. 在项目文件夹下使用 cmd 执行命令

   ~~~~
   Python main.py
   ~~~~

   生成 GIF 展示效果，并生成 png 文件，GIF 保存在项目根目录下， png文件保存在 process文件夹下。

4. 在项目文件夹下使用 cmd 执行命令

   ~~~~
   Python arrange.py
   ~~~~

   启用命令行展示程序，该指令将在 cmd 窗口显示红绿灯转换效果。 

