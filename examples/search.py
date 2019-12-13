from pywikihow import WikiHow, search_wikihow


max_results = 1  # default for optional argument is 10
how_tos = search_wikihow("how to learn programming", max_results)
assert len(how_tos) == 1
how_tos[0].print()


# for efficiency and to get unlimited entries, the best is to use the generator
for how_to in WikiHow.search("how to learn python"):
    how_to.print()
