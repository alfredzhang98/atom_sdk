
# MySQL 版本特征比较

## MySQL 5.7 建表示例

```sql
CREATE TABLE example_table_57 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## MySQL 8.0 建表示例

```sql
CREATE TABLE example_table_80 (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    attributes JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

## 版本特征比较

| 特征 | MySQL 5.7 | MySQL 8.0 | 示例 |
| ---- | --------- | --------- | ---- |
| JSON 数据类型 | 不支持 | 支持 | MySQL 8.0: `ALTER TABLE example_table ADD COLUMN info JSON;` |
| 字符集和排序规则 | utf8mb4 较不完善 | utf8mb4 完全支持 | PyMySQL 连接：`charset='utf8mb4'` |
| 窗口函数 | 不支持 | 支持 | MySQL 8.0: `SELECT name, RANK() OVER (ORDER BY created_at) FROM example_table;` |
| 公共表表达式 | 不支持 | 支持 | MySQL 8.0: `WITH cte AS (SELECT * FROM example_table) SELECT * FROM cte;` |
| 角色管理 | 不支持 | 支持 | MySQL 8.0: `CREATE ROLE 'example_role';` |
| 密码策略 | 较少选项 | 更多密码管理选项 | MySQL 8.0: `SET GLOBAL validate_password.policy=LOW;` |
