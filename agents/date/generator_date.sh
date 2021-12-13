#!/bin/bash

echo "nrel_date <- sc_node_norole_relation;;" >> date.scs
for ((i=1960; i < 2020; i++))
do
echo "date_$i => nrel_date: [$i];;" >> date.scs 
done
