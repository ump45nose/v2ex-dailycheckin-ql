# V2EX 每日奖励（Sitoi/dailycheckin 青龙入口）

此仓库只发布一个可独立调度的包装脚本，不复制 [Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin) 的代码。它从青龙环境变量读取 `V2EX_COOKIE`，在仅供本次执行的临时目录内创建权限为 `0600` 的配置，调用上游 `V2EX` 签到任务，然后删除临时配置。

## 安装与运行

先按上游说明安装 `dailycheckin` 及依赖，确认当前 Python 能导入该包。随后在青龙配置 `V2EX_COOKIE`，定时执行：

```bash
python3 checkin.py
```

也可直接传入上游使用的 `V2EX` JSON 账号列表；若两者都有，以 `V2EX` 为准。脚本不保存 Cookie 到仓库。上游的签到输出与“连续天数”查询是不同的业务状态，连续天数接口失败时不能把已确认的每日奖励抹为失败。

本入口只负责安全传参，不修改上游签到流程。原项目为 MIT 许可证；上游版本、配置格式及接口变化以原项目为准。
