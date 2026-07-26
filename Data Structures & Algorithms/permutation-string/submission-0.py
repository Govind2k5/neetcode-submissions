class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        s1dict, s2dict = {chr(letter):0 for letter in range(ord('a'),ord('z')+1)},{chr(letter):0 for letter in range(ord('a'),ord('z')+1)}

        for i in range(len(s1)):
            s1dict[s1[i]]+=1
            s2dict[s2[i]]+=1

        matches = 0

        for i in s1dict.keys():
            if s1dict[i]==s2dict[i]:
                matches+=1
            else:
                matches+=0
        
        l= 0
        for r in range(len(s1),len(s2)):
            if matches == 26:
                return True
            
            s2dict[s2[r]] +=1
            if s1dict[s2[r]] == s2dict[s2[r]]:
                matches +=1
            elif s1dict[s2[r]] +1 == s2dict[s2[r]]:
                matches -=1
            
            s2dict[s2[l]]-=1
            if s1dict[s2[l]] == s2dict[s2[l]]:
                matches +=1
            elif s1dict[s2[l]] -1 == s2dict[s2[l]]:
                matches -=1
            
            l+=1
        return matches ==26

        
        