class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      dic1 = {}
      dic2 = {}
      if len(s) != len(t):
          return False
      for x in range(len(s)):
          if s[x] in dic1:
              dic1[s[x]] += 1
          else: 
              dic1[s[x]] = 1
      for x in range(len(t)):
          if t[x] in dic1:
              dic1[t[x]] -= 1
          else: 
              dic1[t[x]] = 1

      for x in dic1:
          if dic1[x] != 0:
              return False
      return True