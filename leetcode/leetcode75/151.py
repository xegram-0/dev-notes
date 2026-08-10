class Solution:
    def reverseWords(self, s: str) -> str:
        list = s.split()
        list.reverse()

        return ' '.join(list)
# Optimized
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(reversed(s.split()))
# C
#include <string.h>

char* reverseWords(char* s) {
    int n = strlen(s);

    // Reverse whole string
    for (int i = 0, j = n - 1; i < j; i++, j--) {
        char temp = s[i];
        s[i] = s[j];
        s[j] = temp;
    }

    int write = 0;
    int read = 0;

    while (read < n) {
        // Skip spaces
        while (read < n && s[read] == ' ') {
            read++;
        }

        if (read >= n) {
            break;
        }

        if (write > 0) {
            s[write++] = ' ';
        }

        int wordStart = write;

        // Copy word
        while (read < n && s[read] != ' ') {
            s[write++] = s[read++];
        }

        // Reverse this word
        for (int i = wordStart, j = write - 1; i < j; i++, j--) {
            char temp = s[i];
            s[i] = s[j];
            s[j] = temp;
        }
    }

    s[write] = '\0';
    return s;
}
