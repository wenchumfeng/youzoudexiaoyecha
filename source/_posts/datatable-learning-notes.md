---
title: DataTable 库学习笔记
date: 2025-08-22 19:44:00
tags: [编程, DataTable, Python]
categories: 学习笔记
---

# DataTable 库学习笔记

记录自学 Python DataTable 库的基础内容，包含基本用法和代码示例。

<!-- more -->

## 安装与环境配置

- 安装 DataTable：
  ```bash
  pip install datatable
  ```
- 确认安装：
  ```python
  import datatable as dt
  print(dt.__version__)
  ```

## 基本操作

### 1. 读取数据
- 从 CSV 文件读取数据：
  ```python
  from datatable import dt
  # 假设有一个 sales.csv 文件，包含列：id, product, price, quantity
  df = dt.fread("sales.csv")
  print(df)
  ```
- 示例输出（假设 sales.csv 内容）：
  ```
     | id  product    price  quantity
     |----|---------|-------|---------
   0 | 1   Apple     0.5    100
   1 | 2   Banana    0.3    150
   2 | 3   Orange    0.4    120
  ```

### 2. 数据筛选
- 使用 `f` 表达式筛选列：
  ```python
  # 选择 product 和 price 列
  selected = df[:, ["product", "price"]]
  print(selected)
  ```
- 示例输出：
  ```
     | product  price
     |--------|------
   0 | Apple   0.5
   1 | Banana  0.3
   2 | Orange  0.4
  ```
- 按条件过滤行：
  ```python
  # 筛选 quantity 大于 100 的行
  filtered = df[dt.f.quantity > 100, :]
  print(filtered)
  ```
- 示例输出：
  ```
     | id  product  price  quantity
     |----|-------|------|--------
   0 | 2   Banana  0.3   150
   1 | 3   Orange  0.4   120
  ```

### 3. 数据分组与聚合
- 分组并计算均值：
  ```python
  # 按 product 分组，计算 price 的平均值
  grouped = df[:, dt.mean(dt.f.price), dt.by("product")]
  print(grouped)
  ```
- 示例输出：
  ```
     | product  price
     |--------|------
   0 | Apple   0.5
   1 | Banana  0.3
   2 | Orange  0.4
  ```

### 4. 合并数据集
- 按键合并两个 Frame：
  ```python
  # 创建第二个数据集
  df2 = dt.Frame({"id": [1, 2, 4], "category": ["Fruit", "Fruit", "Vegetable"]})
  # 按 id 合并
  joined = df[:, :, dt.join(df2, on="id")]
  print(joined)
  ```
- 示例输出：
  ```
     | id  product  price  quantity  category
     |----|-------|------|--------|---------
   0 | 1   Apple   0.5   100     Fruit
   1 | 2   Banana  0.3   150     Fruit
   2 | 3   Orange  0.4   120     None
  ```

## 常见问题

- **数据类型不匹配**：确保输入数据类型一致，例如使用 `dt.cast()` 转换类型：
  ```python
  # 将 price 列转换为 float32 类型
  df["price"] = df["price"].cast(dt.Type.float32)
  print(df.types)
  ```
- **性能优化**：对于大文件，使用 `nthreads` 参数控制并行处理：
  ```python
  dt.options.nthreads = 4
  # 示例：处理大型 CSV 文件
  large_df = dt.fread("large_dataset.csv")
  ```

## 资源
- 官方文档：`https://datatable.readthedocs.io/`
- 社区论坛：Stack Overflow、DataTable GitHub Issues