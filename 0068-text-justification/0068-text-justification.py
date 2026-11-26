
class Solution:
    def fullJustify(self, words, maxWidth):
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Pack as many words as possible
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            # Words in the current line
            line_words = words[i:j]
            num_words = len(line_words)

            # Last line or single-word line
            if j == n or num_words == 1:
                line = " ".join(line_words)
                line = line + " " * (maxWidth - len(line))
            else:
                total_spaces = maxWidth - line_length
                gaps = num_words - 1

                spaces_per_gap = total_spaces // gaps
                extra_spaces = total_spaces % gaps

                line = ""

                for k in range(gaps):
                    line += line_words[k]
                    line += " " * (spaces_per_gap + (1 if k < extra_spaces else 0))

                line += line_words[-1]

            result.append(line)
            i = j

        return result
