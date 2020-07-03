#!/bin/bash

mysql --user=root --password="$1" --database=league_stats --execute="insert into league_user_type values (null, \"player\", now(), now(), 1); insert into league_user_type values (null, \"coach\", now(), now(), 1); insert into league_user_type values (null, \"admin\", now(), now(), 1);"
