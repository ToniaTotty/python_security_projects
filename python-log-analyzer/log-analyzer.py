print("new cyber task")

count = 0

# with open("sample_logs.txt", "r") as file:
#     for item in file:
#         splitted = item.split()
#         if splitted[4] == "failed":
#             print(splitted)

#         # if "failed" in item:
#         #     count += 1
#         # splitted = item.split()
#         # if "ip=" in splitted:
#         #     print()
# print(f"we have {count} failed attempts")

ip_list = []
values = {}

def freq_count(arr):
    for i in arr:
        if values.get(i):
            value = values.get(i) + 1
            values.update({i:value})
        else:
            values.update({i:1})
    return values

with open("sample_logs.txt", "r") as file:
    for item in file:
        splitted = item.split()

        if splitted[4] == "failed":
            ip_part = splitted[6]
            ip_address = ip_part.split("=")[1]
            ip_list.append(ip_address)
print(freq_count(ip_list))

# print(values)
for key, value in values.items():
    # print(f"{key} has made {value} attempt(s)")
    if value >= 4:
        print(f"[ALERT] {key} has made {value} attempt(s)")
    elif value == 3:
        print(f"[WARNING] {key} has made {value} attempt(s)")
    else:
        print(f"[INFO] {key} has made {value} attempt(s)")