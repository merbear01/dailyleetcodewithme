class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """
        
        arr = []
        products.sort()
        prefix = ""
        
        for char in searchWord:
            prefix += char
            matches = []
            
            for items in products:
                if items.startswith(prefix):
                    matches.append(items)
                if len(matches) == 3:
                        break
            arr.append(matches)
        return arr