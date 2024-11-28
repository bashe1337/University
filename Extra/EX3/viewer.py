import dcalc

def create_list(*args, **kwargs):
    points = {}
    for i in range(len(args)):
        points[f"Point_{i}"] = args[i]
    points.update(kwargs)
    list = []
    for p, d in points.items():
        list.append(f"{p} = {dcalc.deg_to_gms(d)}")
    return list
print(create_list(172.25899161, 321.42304971, 12.697987681352, pole=21.89617856, put_1=140.85706440))