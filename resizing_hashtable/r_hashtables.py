

# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# '''
# Fill this in

# Resizing hash table
# '''
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * self.capacity


# '''
# Research and implement the djb2 hash function
# '''
def hash(string, max):
    hash = 5381
    for c in string:
        hash = ((hash << 5) + hash ) + ord(c)
    return hash % max
# '''
# Fill this in.

# Hint: Used the LL to handle collisions
# '''
def hash_table_insert(hash_table, key, value):
    index = hash(hash_table,key)
    linked_pair = LinkedPair(key,value)

    if hash_table.storage[index] != None:
        hash_table.storage[index].next = linked_pair


# '''
# Fill this in.

# If you try to remove a value that isn't there, print a warning.
# '''
def hash_table_remove(hash_table, key):
    index = hash(key,hash_table.capacity)

    if hash_table.storage[index] != None:
        while hash_table.storage[index].next != key
            if hash_table.storage[index].next == key:
                hash_table.storage[index].next = [None]
    else:
        return None
# '''
# Fill this in.

# Should return None if the key is not found.
# '''
def hash_table_retrieve(hash_table, key):
    index = hash(key,hash_table.capacity)

    if hash_table.storage[index] != None:
        while hash_table.storage[index].next != None:
            return hash_table.storage[index].next
    else:
        return None
# '''
# Fill this in
# '''
def hash_table_resize(hash_table):
    if hash_table.capacity == hash_table.storage:
        hash_table.capacity * 2
        
def Testing():
    ht = HashTable(2)

    hash_table_insert(ht, "line_1", "Tiny hash table")
    hash_table_insert(ht, "line_2", "Filled beyond capacity")
    hash_table_insert(ht, "line_3", "Linked list saves the day!")

    print(hash_table_retrieve(ht, "line_1"))
    print(hash_table_retrieve(ht, "line_2"))
    print(hash_table_retrieve(ht, "line_3"))

    old_capacity = len(ht.storage)
    ht = hash_table_resize(ht)
    new_capacity = len(ht.storage)

    print("Resized hash table from " + str(old_capacity)
          + " to " + str(new_capacity) + ".")


Testing()




