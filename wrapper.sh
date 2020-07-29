#!/usr/bin/env bash

case $1 in
    server) python3 -u server.py prod;;
    canary) python3 -u server.py canary ;;
    client) python3 -u client.py ;;
    *) echo "only client, server, or canary are supported options" >&2; exit 2 ;;
esac
