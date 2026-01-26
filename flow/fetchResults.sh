#!/usr/bin/env bash

touch results.txt

for ((variant = 50; variant <= 500; variant = variant + 30)); do
    design="gf12/ariane"

    mv "results.txt" "./logs/${design}/${variant}/"
    cd "./logs/${design}/${variant}/"
    python3 ../../../../getMetrics.py | tee -a results.txt
    mv "results.txt" "../../../../"
    cd -
done
