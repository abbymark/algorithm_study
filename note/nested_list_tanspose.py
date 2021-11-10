# short circuits at shortest nested list if table is jagged:
list(map(list, zip(*l)))

# discards no data if jagged and fills short nested lists with None
list(map(list, itertools.zip_longest(*l, fillvalue=None)))