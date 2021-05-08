#!/bin/bash

RED='\033[0;31m'
GREEN='\033[0;32m'
ORANGE='\033[0;33m'
BLINK='\033[6m'
NC='\033[0m' # No Color

function up_to_date {
    printf "${RED}mdCreator is up-to-date\n${NC}"
    printf "${GREEN}Launching...\n${NC}"
}

function update {
    printf "${ORANGE}Updating mdCreator...\n${NC}"
    git pull
    printf "${GREEN}mdCreator updated!\n${NC}"
    printf "${GREEN}Launching...\n${NC}"
}

printf "${RED}${BLINK}Checking for updates...\n${NC}"
[ $(git rev-parse HEAD) = $(git ls-remote $(git rev-parse --abbrev-ref @{u} | sed 's/\// /g') | cut -f1) ] && up_to_date || update