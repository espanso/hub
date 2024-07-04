---
package_name: "sql"
package_title: "sql Package"
package_desc: "A package to get sql code snippets"
package_version: "0.1.0"
package_author: "yanming zhang"
package_repo: "https://github.com/zhangymPerson/espanso-package-sql"
---

An package to get sql command code snippets

For more information about espanso packages, read the [documentation](https://espanso.org/docs/).

## Usage

Available replacements:

### DML(Data Manipulation Language)

| replacement  | output                                                                      | description |
| ------------ | --------------------------------------------------------------------------- | ----------- |
| `:select:`   | `select * from table_name limit 100;`                                       |             |
| `:where:`    | `select * from table_name where condition;`                                 |             |
| `:count:`    | `select count(*) from table_name;`                                          |             |
| `:limit:`    | `select * from table_name limit 100;`                                       |             |
| `:groupby:`  | `select column from table_name group by column;`                            |             |
| `:leftjoin:` | `select * from table_name left join table_name2 on condition;`              |             |
| `:insert:`   | `insert into table_name (column1, column2) values (value1, value2);`        |             |
| `:update:`   | `update table_name set column1 = value1, column2 = value2 where condition;` |             |
| `:delete:`   | `delete from table_name where condition;`                                   |             |

### DDL(Data Definition Language)

- default use mysql ddl

| replacement  |            output            | description |
| :----------: | :--------------------------: | :---------: |
|  `:create:`  |  `create table table_name;`  |    mysql    |
|  `:alter:`   |  `alter table table_name;`   |    mysql    |
|   `:drop:`   |   `drop table table_name;`   |             |
| `:truncate:` | `truncate table table_name;` |             |

### other

#### mysql

| replacement |       output       | description |
| :---------: | :----------------: | :---------: |
|   `:use:`   |  `use database;`   |             |
| `:showdb:`  | `show databases;`  |             |
| `:showtb:`  |   `show tables;`   |             |
|  `:desc:`   | `desc table_name;` |             |
