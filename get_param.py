def get_param(f, query_param):
    query = query_param.split('|')
    res = map(lambda v: v.strip(), f)
    for item in query:
        query_split = item.split(':')
        cmd = query_split[0]
        if cmd == "filter":
            val = query_split[1]
            res = filter(lambda v, text=val: text in v, res)
        if cmd == "map":
            val = int(query_split[1])
            res = map(lambda v, ind=val: v.split(' ')[ind] in v, res)
        if cmd == "unique":
            res = set(res)
        if cmd == "sort":
            val = query_split[1]
            if val == 'desc':
                res = sorted(res, reverse=True)
            else:
                res = sorted(res)
        if cmd == "limit":
            val = int(query_split[1])
            res = list(res)[:val]
        return res
