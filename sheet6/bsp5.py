best_sequids = {'f3', 'g9', 'e2', 'r0'}
optimal_sequids = {'e2','e3','e4','f3','n1'}
# determine how many distinct sequence identifiers are in both lists.
print(f"identifiers in both lists: {best_sequids ^ optimal_sequids}")
print(f"that is {(len(best_sequids ^ optimal_sequids))} distinct identifiers.")
# ^ items that are in list 1 or list 2 but not both --> machen Listen unterscheidbar
# determine which identifiers are only in the first list.
best_sequids - optimal_sequids
# all identifiers in both lists:
# letters in list 1 or list 2 or both
print(f"all identifiers that are listed: {best_sequids | optimal_sequids}")

# determine which identifiers are unique in each one of the lists
print(f"identifiers in list 1 OR list 2: {best_sequids ^ optimal_sequids}")
# ^ excludes identifiers which are present in both lists (list 1 OR list 2 but not in both)

# determine which are unique in list 1 so we can find out, which one of the previous listed identifiers belong
# to list 1
print(f"identifiers only in list 1: {best_sequids - optimal_sequids}")

# determine which are unique in list 2 so we can find out, which one of the previous listed identifiers belong
# to list 2
print(f"identifiers only in list 2: {optimal_sequids - best_sequids}")
