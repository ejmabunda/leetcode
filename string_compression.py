import re

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        chars_str = ''.join(chars)
        list_ix, chars_ix = 0, 0

        while chars_ix < len(chars_str):
            pattern = chars_str[chars_ix] + '+'
            g = re.search(pattern, chars_str[chars_ix:])

            g_len = len(g.group(0))

            if g_len > 1:
                del chars[list_ix + 1: list_ix + g_len]
                if g_len >= 10:
                    for i, n in enumerate(str(g_len)):
                        chars.insert(list_ix + 1 + i, n)
                else:
                    chars.insert(list_ix + 1, str(g_len))
                list_ix += 2
            else:
                list_ix += 1
            chars_ix += g_len
