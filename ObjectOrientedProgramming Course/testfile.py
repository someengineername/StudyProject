class Solution:

    def __init__(self, m, n):
        self._m = m
        self._n = n

    def calculate_answer(self):
        from itertools import cycle

        temp_list = list(range(1, self._m + 1))

        cycler = cycle(temp_list)

        final_answer = []
        temp_answer = [next(cycler)]

        while ...:
            for _ in range(self._n - 1):
                temp_answer.append(next(cycler))
            final_answer.append(temp_answer)
            if temp_answer[-1] == 1:
                break
            temp_answer = [temp_answer[-1]]

        answer = ''.join(str(i) for i in list(map(lambda x: x[0], final_answer)))

        return answer


if __name__ == '__main__':
    solution1 = Solution(int(input()), int(input()))
    print(solution1.calculate_answer())
