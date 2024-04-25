#!/bin/bash
# takes a url and sent request, then display size of body
curl -s "$1" | wc -c
