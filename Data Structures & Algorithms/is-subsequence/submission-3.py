class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(set(s))>len(set(t)):return False
        if len(s)==0 : return True
        sp=0
        tp=0
        while tp != len(t)-1:
            if s[sp]==t[tp] and sp<len(s)-1:
                sp+=1
            tp+=1
        if sp==len(s)-1:
            return True
        else: return False