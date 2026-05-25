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

def freq_count(arr):
    values = {}
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

            print(ip_address)
            ip_list.append(ip_address)
print(freq_count(ip_list))
        