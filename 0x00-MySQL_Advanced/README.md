# 0x00. MySQL Advanced

## Overview
This project is focused on advanced SQL concepts using MySQL, including creating tables with constraints, optimizing queries, and implementing features like stored procedures, views, and triggers. It aims to enhance proficiency in database management and query optimization.

## Concepts
- Advanced SQL
- Table creation with constraints
- Query optimization using indexes
- Stored procedures and functions
- Views and triggers in MySQL

## Tasks

| Task # | Filename               | Description |
|--------|------------------------|-------------|
| 0      | [0-uniq_users.sql](./0-uniq_users.sql) | SQL script to create a table `users` with unique constraints on the `email` field. |
| 1      | [1-country_users.sql](./1-country_users.sql) | SQL script to create a table `users` with a country field that takes an enumerated value. |
| 2      | [2-fans.sql](./2-fans.sql) | SQL script to rank country origins of bands by the number of non-unique fans. |
| 3      | [3-glam_rock.sql](./3-glam_rock.sql) | SQL script to list bands with 'Glam rock' as their main style, ranked by their longevity. |
| 4      | [4-store.sql](./4-store.sql) | SQL script to create a trigger that decreases item quantity after a new order is added. |
| 5      | [5-valid_email.sql](./5-valid_email.sql) | SQL script to create a trigger that resets the `valid_email` attribute when an email is changed. |
| 6      | [6-bonus.sql](./6-bonus.sql) | SQL script to create a stored procedure `AddBonus` that adds a correction for a student. |
| 7           | [7-average_score.sql](./7-average_score.sql)   | Write a SQL script that creates a stored procedure `ComputeAverageScoreForUser` to compute and store the average score for a student. |
| 8           | [8-index_my_names.sql](./8-index_my_names.sql) | Write a SQL script that creates an index `idx_name_first` on the table names and the first letter of name. |
| 9           | [9-index_name_score.sql](./9-index_name_score.sql) | Write a SQL script that creates an index `idx_name_first_score` on the table names and the first letter of name and score. |
| 10          | [10-div.sql](./10-div.sql) | Write a SQL script that creates a function `SafeDiv` to divide the first number by the second or return 0 if the second number is 0. |
| 11          | [11-need_meeting.sql](./11-need_meeting.sql) | Write a SQL script that creates a view `need_meeting` that lists students with a score under 80 and no `last_meeting` or more than a month ago. |
| 12          | [100-average_weighted_score.sql](./100-average_weighted_score.sql) | Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUser` to compute and store the average weighted score for a student. |
| 13          | [101-average_weighted_score_all.sql](./101-average_weighted_score_all.sql) | Write a SQL script that creates a stored procedure `ComputeAverageWeightedScoreForUsers` to compute and store the average weighted score for all students. |

## Setup Environment
- **OS**: Ubuntu 18.04 LTS
- **MySQL Version**: 5.7.30
- To run MySQL in a container:  
  1. Start MySQL: `service mysql start`
  2. Execute SQL queries:  
     ```bash
     cat <filename.sql> | mysql -uroot -p <database_name>
     ```

Ensure MySQL is running, and the scripts are executed in the required environment.


