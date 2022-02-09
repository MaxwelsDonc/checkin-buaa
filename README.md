# CheckinBUAA
北京航空航天大学/北航/BUAA 健康情况自动填报/自动打卡

本项目目前运行方式包括：服务器直接部署运行，腾讯云函数SCF自动运行
## 1. 服务器直接部署运行
### 打卡主程序配置
直接下载main.py函数并上传至服务器或者个人电脑，并安装相关的python环境。
在main函数中的89行填写学号，91行填写登陆密码之后，运行就可以了。
函数默认每天的下午5点零1分进行健康填报，如果需要可以在源代码中对程序进行更改。

<img width="542" alt="image" src="https://user-images.githubusercontent.com/99311937/153231166-be32ab3d-186a-4c82-aff7-e26d991bc6e6.png">

### 推送相关的配置
进入网址：https://www.pushplus.plus，进行登陆和绑定，网站会给你一个token号

<img width="601" alt="image" src="https://user-images.githubusercontent.com/99311937/153231909-066d7b66-3e63-4e0f-b9dc-4e37760f0f91.png">
将这个token号填入程序第93行，运行程序就可以，相关效果如下所示：

<img width="395" alt="image" src="https://user-images.githubusercontent.com/99311937/153232360-d0bf665b-35da-4f20-9272-f7f8e481947a.png">
## 2.腾讯云函数SCF自动运行
1-首先登陆腾讯服务器，并进入云函数界面：https://console.cloud.tencent.com/scf。
<img width="1904" alt="image" src="https://user-images.githubusercontent.com/99311937/153232853-5d870fba-0ab4-455b-925d-7e31c114909b.png">
2-然后点击函数服务-新建
<img width="1426" alt="image" src="https://user-images.githubusercontent.com/99311937/153233567-388de8d4-4ec3-42d9-91f5-17647cb746da.png">
3-之后基础配置如下图，这里的函数名称可以自行进行选取，python版本选择3.6版本，因为3.7和3.7之后的版本需要手动安装依赖库，比较麻烦。
<img width="1385" alt="image" src="https://user-images.githubusercontent.com/99311937/153233801-ddaf2f29-920e-4a44-9e30-c311fc392e51.png">
4-紧接着将Tencent_SCF_Version.py的代码粘贴到IDE里面，
<img width="1352" alt="image" src="https://user-images.githubusercontent.com/99311937/153234566-2281879e-1909-40e5-bb5a-dc6129b77374.png">
5-然后打开高级配置，相关配置如图所示，截图中没有显示的部分，均按照默认配置即可。
你的token号如果不需要推送到手机就填写-1，如果需要推送到手机就参考上面的“推送相关配置”中的token的获取这一部分。
<img width="1148" alt="image" src="https://user-images.githubusercontent.com/99311937/153234861-ce3cf58d-53c4-4a5f-835e-6eb0a9e3e463.png">
6-之后进行触发器的配置，相关配置如图所示，这里我们选择每天的下午5点01分进行打卡。
<img width="943" alt="image" src="https://user-images.githubusercontent.com/99311937/153235710-c8016950-16ae-44d3-91db-528df1fbdd28.png">
7-最后点击完成，完成函数的创建，之后就可以每天自动打卡并推送到手机啦！如果发现没有打卡成功，请检查一下学号密码是否填写错误～
