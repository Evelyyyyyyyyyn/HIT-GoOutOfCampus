HIT每日定时申请出校脚本
====

> 缘由：临时出校临时出校，就是临时想起来要出校才申请的，但是就申请到走到校门这段时间，不够咱学校的系统反应，以致于每次都看门岗保安脸色。遂索性写个脚本，每天凌晨（1点半）都给我申请掉！

## 使用方法

1. fork本项目，项目中点击上方`Settings` ---> 左边的`Secrets` ---> `New repository secret`添加两个`secret`：

    - ID: `学号`
    - PASSWORD: `统一认证密码`

1. 点击上方`Actions` --> 左边找到`申请出校` --> 点击启用

## 感谢

[HIT-clock](https://github.com/Dr-TSNG/HIT-clock)  
[HIT-out-script](https://github.com/1170300817/HIT-out-script)  
[Alook实现HIT一键申请出校](https://www.jianshu.com/p/caa4eba50057)
