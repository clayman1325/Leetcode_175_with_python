class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
      dict = Counter(words)
      array = []
      for x in dict:
        array.append((-dict[x],x))
      array.sort()
      result = []

      while k > 0:
        elem = array.pop(0)[1]
        result.append(elem)
        k -= 1

      return result