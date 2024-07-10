class Solution(object):
    def minOperations(self, logs):
        folders = []
        for items in logs:
            if items == "../":
                if folders:
                    folders.pop()
            elif items == "./":
                continue
            else:
                folders.append(items)
        return len(folders)
            