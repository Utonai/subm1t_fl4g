# subm1t-fl4g

>*2021.10.18编辑* 
>
>_此项目最近会进行重构（会删库的那种），因此该repo不会再更新_
>
> *~~最近是指啥时候。。。咕咕咕.mp3~~*
>
> _~~↑提桶跑路了属于是（~~_

## 依赖

* python3.6及以上

* requests



## 说明

该项目主要用于在AWD比赛中批量自动提交flag。  
主要参考：<https://github.com/0xaww/awd-submit-flag>


## 使用方法

1. 配置`config.conf`
2. 修改`attack.py`
3. 修改`submit.py`中的请求头信息（用于提交flag时
4. 按需运行以下程序：
    * `auto_atk.py` 自动攻击并提交flag（循环运行
    * `read_file.py` 在文件中读取并提交flag（单次运行
    * `cli.py` 命令行界面提交flag（按两次回车提交


## 文件调用
|文件名    |用途|
|:---   |:---   |
|config.conf    |配置文件|
|resolve_config.py  |解析config|
|attack.py    |攻击获取flag|
|submit.py  |提交flag|
|log.py |生成日志|
|auto_atk.py   |主要运行文件|
|read_file.py   |主要运行文件|
|cli.py   |主要运行文件|


## config.conf 详解

* `ip_list_file` 保存所有攻击目标IP的文件，其中每行保存一个IP

* `flag_list_file` 保存待提交flag的文件，其中每行保存一个flag

* `log_file` 运行`read_file.py`产生日志的保存路径

* `submit_method` 提交方式，可以通过curl或requests来进行提交
  
* `submit_address` 平台提交flag的地址

* `submit_token` 队伍token

* `success_request` 判断提交的flag正确的字段（需要根据手动提交的结果来确定，或根据官方文档来确定）

* `failed_request` 判断提交的flag错误或其他故障的字段（需要根据手动提交的结果来确定，或根据官方文档来确定）

* `round_time` 比赛每轮时间（秒）

* `rounds` 比赛总轮次（可以不配置，无影响）

* `submit_wait` 每次提交flag之间的停顿间隔（秒），部分平台设有提交间隔时配置




## 单次运行

当需要单次运行或进行单次测试时，可以对各个模块独立进行单次测试：
* `attack.py` : `python attack.py 192.168.1.101` （测试是否能够拿到flag）
* `submit.py` : `python submit.py  flag{114514}` （测试提交flag是否成功）





## 备注

* ~~亟待质检~~`read_file.py` `cli.py`已通过测试
* 文件读取flag暂未实现增量式读取
* `success.log`是获取flag成功的记录，其中可能会包括提交失败的记录 ~~（草~~
