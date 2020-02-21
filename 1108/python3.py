class Solution:
    def defangIPaddr(self, address):
        import string
        s = address.replace('.', '[.]')  # '和"的差异
        return s
