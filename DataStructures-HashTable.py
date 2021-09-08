class HashTable():
    def __init__(self, size):
        self.size = size
        self.data = [None] * self.size

    def __str__(self):
        return str(self.__dict__)

    def _hash(self, key):  # 0(1)
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % self.size
            # print(hash)
        return hash

    def set(self, key, value):  # O(1)
        address = self._hash(key)
        if not(self.data[address]):  # check for collisons
            self.data[address] = []
        # Append the value provided into the hash table
        self.data[address].append([key, value])
        return self.data

    def get(self, key):  # O(1), or O(n) w/ collisions
        address = self._hash(key)
        current_bucket = self.data[address]
        # print(currentBucket)
        if current_bucket:
            for i in range(len(current_bucket)):
                if current_bucket[i][0] == key:
                    return current_bucket[i][1]
        return None

    # This will take longer time O(n) because it loops through the entire array ex If the array is 50000 items it loops fully
    def keys(self):
        keys_array = []
        for i in range(len(self.data)):
            if self.data[i] != None:
                for j in range(len(self.data[i])):
                    keys_array.append(self.data[i][j][0])
        return keys_array


demo = HashTable(50)
demo.set("Grapes", 1000)
demo.set("Apples", 90)
demo.set("Oranges", 50)
demo.set("Monkey", 89)
demo.get("Oranges")
