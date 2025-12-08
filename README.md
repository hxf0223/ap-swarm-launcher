# ap-swarm-launcher #

Simplified ArduPilot SITL launcher for multi-drone simulations. Runs multiple
ArduPilot SITL instances in parallel, managed by a central process supervisor
that merges the standard output streams of individual processes and configures
the SITL instances to start the drones from a grid-like formation.

## 1. 安装环境 ##

```bash
# export all_proxy="http://192.168.11.139:7890"
curl -LsSf https://astral.sh/uv/install.sh | sh

# 确认是否在 PATH 中，安装路径为：
# ~/.local/bin/uv
which uv
```

包镜像配置（可选）

```bash
mkdir -p ~/.config/uv
cat > ~/.config/uv/uv.toml <<EOF
```

```bash
# ~/.config/uv/uv.toml

[global]
# 全局缓存目录
cache-dir = "~/.cache/uv"

# Python虚拟环境目录
venv-dir = "~/.local/share/uv/venvs"

# 索引配置
[[index]]
name = "ustc"
url = "https://mirrors.ustc.edu.cn/pypi/simple"
default = true

# 可选：添加备用镜像源
[[index]]
name = "tsinghua"
url = "https://pypi.tuna.tsinghua.edu.cn/simple"
default = false

# 可选：官方源作为备用
[[index]]
name = "pypi"
url = "https://pypi.org/simple"
default = false
```

## 2. 运行示例 ##

```bash
# 使能 virtual environment 并安装依赖
uv sync

# 启动一个 ArduPlane SITL 实例，位置在中国合肥
uv run ap-sitl-swarm --model plane --no-multicast --tcp-base-port 5760 --home 31.8269,117.2280,30 ~/tmp/arduplane/arduplane

# 启动两个 ArduPlane SITL 实例，设置数据目录为 ~/tmp/arduplane
uv run ap-sitl-swarm --model plane -n 2 --data-dir ~/tmp/arduplane --no-multicast --tcp-base-port 5760 --home 31.8269,117.2280,30 ~/tmp/arduplane/arduplane

# 让除 1 号之外的所有无人机跟随 1 号机器（FOLL_SYSID = 1）
uv run ap-sitl-swarm --model plane -n 2 --data-dir ~/tmp/arduplane --no-multicast --tcp-base-port 5760 --home 31.8269,117.2280,30 --follow --follow-leader 1 ~/tmp/arduplane/arduplane
```

* 默认参数文件`parm`来自`ArduPilot`源码：
  * `Tools/autotest/default_params/copter.parm`；
  * `Tools/autotest/models/plane.parm`；
* `follow`功能实现代码：`libraries/AP_Follow/AP_Follow.cpp`。固定翼没有`Follow`功能，比如`copter`的跟随相关代码：
  * `libraries/AP_Follow/AP_Follow.cpp`；

## 其他参考 SITL 脚本及文档

* [sitl-cli](https://github.com/iWaheeb/sitl-cli)
* [pymavlink-examples](https://github.com/peakyquest/pymavlink-examples)
* [ArduPilot Follow Mode](https://ardupilot.org/copter/docs/follow-mode.html)
* [ArduPilot Follow Example Script](https://github.com/ArduPilot/ardupilot/blob/master/libraries/SITL/examples/Follow/plane_quad.sh)
* [github -- ArduPilot Gazebo Plugin](https://github.com/ArduPilot/ardupilot_gazebo)

