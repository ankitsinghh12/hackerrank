class Solution:
    def defangIPaddr(self, address):
        ans=address.replace(".","[.]")
        return ans