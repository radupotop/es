#!/bin/bash

mysql -u root es < schema.sql
mysql -u root es < data.sql
