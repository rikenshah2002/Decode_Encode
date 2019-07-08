# Main Logic of My App
# Backend


class Main:
    def to_encode(self, word):
        import time
        import random as r
        # Used Random for :
        # It always create unique string even if same string applied many times
        j = r.randint(0, 9)
        k = r.randint(0, 9)
        to_add_in_j = r.randint(0, 9)
        to_add_in_k = r.randint(0, 9)
        first_to_add = j
        last_to_add = k

        to_decode = ''
        global time_start
        time_start = time.perf_counter()
        for i in range(len(word)):
            if i % 2 == 0:
                if word[i] == ' ':
                    to_decode += str(chr(ord(word[i])))
                else:
                    j += to_add_in_j

                    to_decode += str(chr(ord(word[i]) + j))
            else:
                if word[i] == ' ':
                    to_decode += str(chr(ord(word[i])))
                else:
                    k += to_add_in_k
                    to_decode += str(chr(ord(word[i]) + k))
        to_decode = str(first_to_add) + str(to_add_in_j) + to_decode + str(to_add_in_k) + str(last_to_add)
        # print(to_decode)
        return to_decode

    def to_decode(self, to_decode):
        # import time
        ans = ''
        j = int(to_decode[0])
        k = int(to_decode[-1])
        to_add_in_j = int(to_decode[1])
        to_add_in_k = int(to_decode[-2])
        to_decode = to_decode[2:-2]
        for i in range(len(to_decode)):
            if i % 2 == 0:
                if to_decode[i] == ' ':
                    ans += str(chr(ord(to_decode[i])))
                else:
                    j += to_add_in_j

                    ans += str(chr(ord(to_decode[i]) - j))
            else:
                if to_decode[i] == ' ':
                    ans += str(chr(ord(to_decode[i])))
                else:
                    k += to_add_in_k

                    ans += str(chr(ord(to_decode[i]) - k))
        # print("Before Decoding:\n", to_decode)
        # print("After Decoding:\n", ans)
        # print ('\nTotal Time Taken:', time.perf_counter()-time_start, 'sec.')
        return ans


if __name__ == '__main__':
    run = Main()
    encoded = run.to_encode(input('Enter sentence or word:'))
    run.to_decode(encoded)
