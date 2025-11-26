#!/bin/bash

uv sync
uv run ap-sitl-swarm --model plane -n 2\
    --data-dir ~/tmp/ardu \
    --tcp-base-port 5760 \
    --home 31.8269,117.2280,30\
    ~/tmp/ardu/arduplane
