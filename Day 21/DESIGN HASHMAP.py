def process_queries(queries):
    size = 1000  # size of hash table
    hashmap = [[] for _ in range(size)]
    
    def hash_function(key):
        return key % size
    
    def insert(key, value):
        idx = hash_function(key)
        bucket = hashmap[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update
                return
        
        bucket.append((key, value))  # insert
    
    def get(key):
        idx = hash_function(key)
        bucket = hashmap[idx]
        
        for k, v in bucket:
            if k == key:
                return v
        
        return -1
    
    def delete(key):
        idx = hash_function(key)
        bucket = hashmap[idx]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return
    
    result = []
    
    for query in queries:
        if query[0] == 1:
            _, key, value = query
            insert(key, value)
        
        elif query[0] == 2:
            _, key = query
            result.append(get(key))
        
        elif query[0] == 3:
            _, key = query
            delete(key)
    
    return result


# Input / Output handling
if __name__ == "__main__":
    n = int(input().strip())
    queries = []
    
    for _ in range(n):
        arr = list(map(int, input().split()))
        queries.append(tuple(arr))
    
    res = process_queries(queries)
    
    for val in res:
        print(val)
