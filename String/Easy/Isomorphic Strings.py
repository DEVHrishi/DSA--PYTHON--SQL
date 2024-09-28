'''Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true'''

class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		if len(set(s)) != len(set(t)):
			return False
		hash_map = {}
		for char in range(len(t)):
			if t[char] not in hash_map:
				hash_map[t[char]] = s[char]
			elif hash_map[t[char]] != s[char]:
				return False
		return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # define dictionary
        word_map = {}
        word_map2 = {}

        for i in range(len(s)):
            # if s[i] not in map1 and t[i] not in map2 then map1[s[i]] = t[i] and map2[t[i]] = s[i]
            if s[i] not in word_map and  t[i] not in word_map2:
                word_map[s[i]] = t[i]
                word_map2[t[i]] = s[i]
            # if s[i] in map1 and t[i] in map2 
            elif s[i] in word_map and t[i] in word_map2:
                if word_map[s[i]] != t[i] or word_map2[t[i]] != s[i]:
                    return False
            # if s[i] in map1 but not in map2
            elif s[i] in word_map and t[i] not in word_map2:
                if word_map[s[i]] != t[i]:
                    return False
                else:
                    word_map2[t[i]] = s[i]
            # if t[i] in map2 but not in map1
            elif s[i] not in word_map and t[i] in word_map2:
                if word_map2[t[i]] != s[i]:
                    return False
                else:
                    word_map[s[i]] = t[i]
            
        return True