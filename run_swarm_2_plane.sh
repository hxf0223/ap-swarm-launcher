#!/bin/bash

uv run ap-sitl-swarm --model plane -n 2 --data-dir ~/tmp/arduplane --no-multicast --tcp-base-port 5760 --home 31.8269,117.2280,30 --follow --follow-leader 1 ~/tmp/arduplane/arduplane
