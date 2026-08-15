#!/usr/bin/env bash

set -euo pipefail

PROJ_DIR=$(pwd)
CMD='\e[0;34m'
NC='\e[0m'

function log {
    echo -e "${CMD}[$(date +\"%d-%m-%y\")][$(date +\"%T\")] [client] ${1}${NC}"
}

log "client build process start"

if [[ ! -d out ]]; then
    mkdir out
fi

elm-format --yes src/elm/*
elm make src/elm/Main.elm --output out/index.html

log "client build process end"
