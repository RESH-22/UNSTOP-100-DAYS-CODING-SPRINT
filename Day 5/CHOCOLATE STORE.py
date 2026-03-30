def process_queries(q, queries):
    stock = {}

    for query in queries:
        if query[0] == '1':
            choc = query[1]
            qty = int(query[2])

            stock[choc] = stock.get(choc, 0) + qty

        else:
            choc = query[1]
            qty = int(query[2])

            available = stock.get(choc, 0)

            sold = min(available, qty)
            print(sold)

            stock[choc] = available - sold


if __name__ == "__main__":
    q = int(input())
    queries = [input().split() for _ in range(q)]
    process_queries(q, queries)
