#!/usr/bin/env bash

set -euo pipefail

PROJ_DIR=$(pwd)
CMD='\e[0;34m'
ERR='\e[0;31m'
NC='\e[0m'

function log {
    echo -e "${CMD}[$(date +\"%d-%m-%y\")][$(date +\"%T\")] [app] ${1}${NC}"
}

function log_err {
    echo -e "${ERR}[$(date +\"%d-%m-%y\")][$(date +\"%T\")] [app] ${1}${NC}"
}

log "app build process start"

cd ui
if ! ./build.sh; then
    log_err "client build failed - exiting app build"
    exit 1
fi
cd ../

if [[ ! -d static ]]; then
    mkdir static
fi
cp ui/out/* static/

mypy .
pytest .

pyinstaller \
    --onefile \
    tf_plan_view.py

log "app build process end"
