with open ("raw_data.txt", "r") as file:
    data = file.read()
    data_list = data.strip().split(",")
    item = data_list[0].strip()