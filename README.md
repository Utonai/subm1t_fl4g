# subm1t-fl4g


## 依赖

* python3.6

* requests



## 说明

该项目主要用于在AWD比赛中批量自动提交flag。  
主要参考：<https://github.com/0xaww/awd-submit-flag>


## 使用方法

1. 配置`config.conf`
2. 修改`attack.py`
3. 修改`submit.py`中的请求头信息
4. 运行`loopp.py`


## 文件调用
|文件名    |用途|
|:---   |:---   |
|config.conf    |配置文件|
|resolve_config.py  |解析config|
|attack.py    |获取flag|
|submit.py  |提交flag|
|log.py |生成日志|
|loopp.py   |主要运行文件|



## config.conf 详解

* `ip_list_file` 保存所有目标IP的文件，其中每行保存一个IP

* `submit_method` 提交方式，可以通过curl或requests来进行提交
  
* `submit_address` 平台提交flag的地址

* `submit_token` 队伍token

* `success_request` 判断提交的flag正确的字段（需要根据手动提交的结果来确定，或根据官方文档来确定）

* `failed_request` 判断提交的flag错误或其他故障的字段（需要根据手动提交的结果来确定，或根据官方文档来确定）

* `round_time` 比赛每轮时间（秒）

* `rounds` 比赛总轮次（可以不配置，无影响）

* `submit_wait` 每次提交flag之间的停顿间隔（秒），部分平台会设有提交间隔，没有就写0




## 单次运行

当需要单次运行或进行单次测试时，可以对各个模块独立进行单次测试：
* `attack.py` : `python attack.py 192.168.1.101` （测试是否能够拿到flag）
* `submit.py` : `python submit.py 192.168.1.101 flag{114514}` （测试提交flag是否成功）





## 备注

* 亟待质检
* round_time处可能有时延越来越大的问题，暂时咕咕（
* `success.log`是获取flag成功的记录，可能会有提交失败的记录
