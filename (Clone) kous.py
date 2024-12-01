# Databricks notebook source
# MAGIC %sql
# MAGIC create table employee
# MAGIC (id int,
# MAGIC name string)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC insert overwrite table employee values(1,kous),(2,kabil),(3,kousy)

# COMMAND ----------


