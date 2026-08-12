class Solution:
    def compress(self, chars: List[str]) -> int:
        s = []
        count = 0
        s.append(chars[0])
        var = chars[0]
        n = len(chars)
        for i, char in enumerate(chars):
            if var == char:
                count += 1
            elif var != char and count == 1:
                var = char
                s.append(char)
                count = 1
                continue
            elif var != char:
                s += list((str(count)))
                s.append(char)
                var = char
                count = 1
        if count == 1:
            pass
        else:
            countstr = list(str(count))
            s += (countstr)

        chars[:] = s
        return len(chars)
        
    # Solution
  class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        read = 0

        while read < len(chars):
            char = chars[read]
            count = 0

            while read < len(chars) and chars[read] == char:
                read += 1
                count += 1

            chars[write] = char
            write += 1

            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        return write
