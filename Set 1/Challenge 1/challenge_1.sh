#!/usr/bin/env bash
#
# Description:
# Solution to the task: https://www.cryptopals.com/sets/1/challenges/1
#
# Usage:
# ./challenge_1.sh
#

HEX_STRING=49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d

# The output should be SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t.
echo $HEX_STRING | xxd -r -p | base64
