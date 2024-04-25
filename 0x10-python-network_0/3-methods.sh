#!/bin/bash
# takes URL and display all methods that server accepts
curl -sI "$1" | grep "Allow:" | cut -d " " -f 2-
