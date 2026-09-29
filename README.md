# V2EX 每日奖励（Sitoi/dailycheckin 青龙入口）

此仓库只发布一个可独立调度的包装脚本，调用 [Sitoi/dailycheckin](https://github.com/Sitoi/dailycheckin) 的 V2EX provider。它从环境变量读取 Cookie，所有网络请求限制为 30 秒；只有读到当日登录奖励才返回成功，不依赖上游 CLI 的退出码。

## 安装与运行

安装验证过的依赖版本，随后在青龙配置 `V2EX_COOKIE`，定时执行：

```bash
python3 -m pip install -r requirements.txt
python3 checkin.py
```

也可直接传入上游使用的 `V2EX` JSON 账号列表；若两者都有，以 `V2EX` 为准。脚本不保存 Cookie 到仓库。上游的签到输出与“连续天数”查询是不同的业务状态，连续天数接口失败时不能把已确认的每日奖励抹为失败。

可选 `V2EX_PROXY`、`V2EX_USER_AGENT`。输出一行 `BENEFIT_RESULT` JSON，`success=true` 且退出码为 0 才表示所有账号签到已确认；失败返回非零，且不打印 Cookie 或账号名。Cookie 只留在进程内存中。原项目为 MIT 许可证；升级上游版本前需核对 provider 的接口与结果字段。
