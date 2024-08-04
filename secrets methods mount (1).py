# Databricks notebook source
dbutils.fs.mount(
    source = "wasbs://wafacontainer@wafastoragede.blob.core.windows.net/",   
    mount_point = "/mnt/data",
    extra_configs = {"<conf-key>":dbutils.secrets.get(scope = "<scope-name>", key = "<key-name>")}

)

# COMMAND ----------

# MAGIC %md
# MAGIC hey  we  fixed the bug
