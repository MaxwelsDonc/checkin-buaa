# CheckinBUAA
***重要声明: 本代码仅供参考学习使用，下载后请在24小时之内删除。*
*请大家支持学校的防疫工作，不要滥用自动打卡程序。***

北京航空航天大学 \| 北航 \| BUAA \| 健康情况自动填报 \| 自动打卡

![forks](https://img.shields.io/github/forks/MaxwelsDonc/checkin-buaa?style=flat-square) ![github](https://img.shields.io/github/watchers/MaxwelsDonc/checkin-buaa?style=flat-square) ![stars](https://img.shields.io/github/stars/MaxwelsDonc/checkin-buaa?style=flat-square)

## 特性优点
- 支持多平台部署
- 支持相关推送服务
- 提供完善的使用文档
## 快速开始
### 打卡主程序运行方式
本项目目前运行方式包括：
**[服务器直接部署运行(不推荐)](#服务器直接部署运行)**\||**[腾讯云函数SCF自动运行（推荐）](#腾讯云函数scf自动运行推荐)**\||**[Github Action](#github-action)**
请点击上面你希望的运行选项进行运行.

---

### 推送相关的配置
进入网址：https://www.pushplus.plus 进行登陆和绑定，网站会给你一个token号

- 之后进行主函数配置[main.py](/sever-deloy/main.py)
  目前主函数的配置包含三个变量: name, key, token.
    > name="账号名/打卡学号"
    > key="登陆密码"
    > token="推送的tokne"(可选)

    其中token变量和手机推送相关,需要进入[pushplus官网](https://www.pushplus.plus)进行手动获得

- 主函数配置完成之后可以直接进行运行
  > python3 main.py

    目前设定为每天18:01进行程序打卡,程序需要一直挂在在服务器上进行运行;
    如果运行失败会进行相关的提示;
    如果打卡位置更改,请停止打卡程序或者在18:01前进行手动打卡,目前仅支持学校内部打卡;
#### 腾讯云函数SCF自动运行（推荐）
- 首先登陆腾讯云网页，并进入[云函数界面](https://console.cloud.tencent.com/scf), 然后点击函数服务-新建.

![](/figure/scf-2.png)

- 之后基础配置如下图，这里的函数名称可以自行进行选取，python版本选择3.6版本，因为3.7和3.7之后的版本需要手动安装依赖库，比较麻烦
![](/figure/scf-3.png)

- 紧接着将Tencent_SCF_Version.py的代码粘贴到IDE里面
![](/figure/scf-4.png)

- 然后打开高级配置，相关配置如图所示，截图中没有显示的部分，均按照默认配置即可。 你的token号如果不需要推送到手机就填写-1，如果需要推送到手机就参考上面的“推送相关配置”中的token的获取这一部分。
![](/figure/scf-5.png)

- 之后进行触发器的配置，相关配置如图所示，这里我们选择每天的下午5点01分进行打卡。

![](/figure/scf-6.png)

- 最后点击完成，完成函数的创建，之后就可以每天自动打卡并推送到手机啦！如果发现没有打卡成功，请检查一下学号密码是否填写错误～
#### Github Action
目前有待完善
### 打卡消息推送至手机
目前仅支持pushplus进行推送.