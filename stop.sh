#!/bin/bash
ps x | grep -v 'grep' | grep 'python -u.*' | awk '{ print $1 }' | xargs kill -SIGTERM
