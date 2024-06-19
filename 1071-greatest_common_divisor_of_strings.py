class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        gcd = ''
        divisor = str2

        for ix in range(len(str2)):
            divisor = str2[0: len(str2) - ix]
            if self.isDivisor(str2, divisor):
                if self.isDivisor(str1, divisor):
                    gcd = divisor
                    break

        return gcd

    def isDivisor(self, str, divisor):
        """Checks whether a string is a divisor of another

        Args:
            str (str): The string to be divided
            divisor (str): The string that divides the other

        Returns:
            bool: True if `divisor` is a divisor of `str`, False otherwise.
        """
        step = len(divisor)
        for ix in range(0, len(str), step):
            if str[ix: ix + step] != divisor:
                return False

        return True