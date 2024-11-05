import json
import pickle
import time

# サンプルデータ（辞書）
data = {
    "name": "example",
    "values": list(range(1000)),
    "nested": [{"a": i, "b": i**2} for i in range(100)]
}

# JSONシリアライズとデシリアライズの時間計測
start = time.time()
json_data = json.dumps(data)
json_load = json.loads(json_data)
end = time.time()
print("JSON processing time:", end - start)

# Pickleシリアライズとデシリアライズの時間計測
start = time.time()
pickle_data = pickle.dumps(data)
pickle_load = pickle.loads(pickle_data)
end = time.time()
print("Pickle processing time:", end - start)
