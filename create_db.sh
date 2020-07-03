#!/bin/bash

db_pass=$1

# create database
mysql --user=root --password="$db_pass" --execute="create database if not exists league_stats;"

# change dbpassword in settings.py
sed -i "s/replace_me_with_root_password/$db_pass/" league_stats/settings.py
