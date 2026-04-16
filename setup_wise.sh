#!/bin/sh


wget -O vectors.tar.gz "https://filesender.open-science-cloud.ec.europa.eu/download.php?token=63a7235c-0265-4fac-bec7-4e4c6caa4c85&files_ids=2174933"
wget -O images.tar.gz "https://filesender.open-science-cloud.ec.europa.eu/download.php?token=12c6c6c4-4efe-4897-bb25-222345f135cf&files_ids=2174940"

tar -xzvf vectors.tar.gz -C /wise/projects
tar -xzvf images.tar.gz -C /wise/data

ls -lah /wise/projects
ls -lah /wise/data
