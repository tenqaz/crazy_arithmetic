class Solution:

    def openLock(self, deadends: List[str], target: str) -> int:

        queue = ["0000"]
        level = 0
        deadends_set = set(deadends)
        visited = set()
        visited.add("0000")

        while queue:

            for i in range(len(queue)):

                item = queue.pop(0)

                if item in deadends_set:
                    continue

                if item == target:
                    return level

                for j in range(4):
                    plus_item = self.plus(item, j)
                    if plus_item not in visited:
                        visited.add(plus_item)
                        queue.append(plus_item)

                    mins_item = self.mins(item, j)
                    if mins_item not in visited:
                        visited.add(mins_item)
                        queue.append(mins_item)

            level += 1

        return -1

    def plus(self, item, j):
        item_list = list(item)

        if item[j] == '9':
            item_list[j] = '0'
        else:
            item_list[j] = chr(ord(item[j]) + 1)

        return "".join(item_list)

    def mins(self, item, j):
        item_list = list(item)

        if item[j] == '0':
            item_list[j] = '9'
        else:
            item_list[j] = chr(ord(item[j]) - 1)

        return "".join(item_list)
    

if __name__ == '__main__':
    deadends = ["0201", "0101", "0102", "1212", "2002"]
    target = "0202"
    print(Solution().openLock(deadends, target))