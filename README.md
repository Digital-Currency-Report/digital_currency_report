# Digital Currency Report 自动升级 [API]

### 说明

- 开发语言 python 3.8 | 包管理工具 poetry -> 必须是 3.8+
- 数据库 postgres

### 说明
> 开发分支请合并到 staging, 请勿直接 PR 到 master 分支
> 
> 开发流程: feature -> staging -> master
> 
> 接口文档链接 -> http://127.0.0.1:8000/docs


#### 前置条件：
- docker

#### 开发环境：
- docker
- docker-compose
- make

#### 1、初始化项目

```
make dev
```

#### 2、初始化数据库

1. 创建数据库[默认为 digital_currency_report]

   如需修改数据库名修改 .env 文件中 DB_TABLE 字段

2. 初始化数据库

```
make exec
cd database
alembic upgrade head
```