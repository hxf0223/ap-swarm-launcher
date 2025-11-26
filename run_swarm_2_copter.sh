#!/bin/bash

uv sync
uv run ap-sitl-swarm --model copter -n 2\
    --data-dir ~/tmp/ardu \
    --tcp-base-port 5760 \
    --home 31.8269,117.2280,30 \
    --follow --follow-leader 1 ~/tmp/ardu/arducopter
