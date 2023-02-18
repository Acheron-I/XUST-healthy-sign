<div align="center">
<h1 align="center">
西科大自动健康打卡(自用修改版)
2023.2.18 学校打卡平台有变，现在已经成功更新，目前请通过fork后改参数的方式使用，secrets和打卡成功推送明天会更新
 </h1>

</div>

# 本项目为自用修改版，了解更多请看原仓库



#2023.2.18 学校打卡平台有变，现在已经成功更新

# 注意事项及修改内容

1.此fork仅小范围使用，并不用做商业用途

2.默认配置仅适用于临潼校区骊山校园，每天下午17:30打卡,详细地址填为西安科技大学。雁塔校区自行修改`chekln.py`中参数

3.推送由server酱修改为Pushdeer在线版本，避免了server每天仅5条推送通知的限制。但是变量名称并没有变，仍然为`SERVERPUSHKEY`

(ps:虽然正常使用用不到5条，但考虑到一个人的Sendkey可能用于其他应用，且调整参数时会额外消耗推送限额，还是改成了pushdeer，后续会自驾转发服务器)

[Pushdeer](https://github.com/easychen/pushdeer)

4.补充了推送信息 打卡成功也会有提示

5.如果打卡失败，将在15分钟后重试，直至下一次成功，可能为学校打卡系统异常，此时建议手动cancle掉此次action并且手动打卡

写于2022.11.14

# 使用说明

1. **Fork 本项目**
  
2. ** 添加以下2个 Secret。**
  

| Name | Value |
| --- | --- |
| UID | ``UID`` |

| Name | Value |
| --- | --- |
| SERVERPUSHKEY | ``Key`` |

``UID``的获取： 自主进入健康打卡页面（如遇到需要先填写返校承诺书的情况先完成返校承诺书再继续进入健康打卡页面)，然后右上角
copy url， 将url尾部的uid=‘这就是我们要的uid’复制下来 （uid末尾的‘=’符号是uid的一部分）

``Key``的获取：下载pushdeer官方app或其他渠道，详情参见[Pushdeer](https://github.com/easychen/pushdeer)

4. **开启 Actions 并触发每日自动执行**

如果需要修改每日任务执行的时间，请修改 `startCheckingIn.yml`，找到下如下配置。

```yml
  schedule:
    - cron: '30 9 * * *'
    # cron表达式，Actions时区是UTC时间，所以下午18点要往前推8个小时。
    # 示例： 每天下午17点30执行 '30 9 * * *'
    # 本仓库默认中国时间(utc+8)的17：30分打卡
```

cron语法 - cron: '分钟 小时（utc+0,的时间 简单来说就是想要打卡的中国时间的小时-8小时） * * *'
https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows cron语法参考
