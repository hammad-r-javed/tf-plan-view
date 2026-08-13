#!/bin/bash

PROJ_DIR=$(pwd)

function print_logline {
    echo "[$(date +\"%d-%m-%y\")][$(date +\"%T\")] [client] $1"
}

function build_client {
    print_logline "client build process start"

    mkdir out
    elm-format --yes src/elm/*
    elm make src/elm/Main.elm --output out/index.html

    print_logline "client build process end"
}

build_client
