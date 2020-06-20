import re

mapping_keys = ["index-name", "shard number", "primary or replica", "state",
                "document count", "store size", "node ip", "node name"]
result_dict = {"primary": 0, "replica": 0, "primary_size": 0, "replica_size": 0}

def get_store_size(store_size):
    if store_size.endswith("gb"):
        store_size_numeric = float(store_size.replace("gb", ""))
        store_size_numeric_mb = store_size_numeric * 1024
    else:
        store_size_numeric_mb = float(store_size.replace("mb", ""))
    return store_size_numeric_mb

def get_modified_store_size(total_store_size):
    if total_store_size >= 1024:
        s = total_store_size/1024
        s = str(round(s, 1)) + "gb"
    else:
        s = str(total_store_size) + "mb"
    return s

with open("shards_data.txt", "r") as fr:
    for line in fr:
        line_parts = line.split()
        line_mapping_dict = dict(zip(mapping_keys, line_parts))
        store_size = 0
        if "store size" in line_mapping_dict:
            store_size = get_store_size(line_mapping_dict["store size"])
        if line_mapping_dict["primary or replica"] == "p":
            result_dict["primary"] += 1
            result_dict["primary_size"] += store_size
        else:
            result_dict["replica"] = result_dict["replica"] + 1
            result_dict["replica_size"] += store_size
result_dict["primary_size"] = get_modified_store_size(result_dict["primary_size"])
result_dict["replica_size"] = get_modified_store_size(result_dict["replica_size"])
print(result_dict)


