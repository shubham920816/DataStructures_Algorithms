import os


class Peak_finder(object):

    def __init__(self, input=[]):
        self.input = input

    def _logic(self, array=[]):
        n = len(array)
        mid = int(n / 2)
        for i in range(0, n):
            if n > 2:
                if (array[mid] >= array[(mid) + 1]) and (array[mid] >= array[(mid) - 1]):
                    value = array[mid]
                    return value

                elif array[(mid) - 1] >= array[(mid)]:
                    temp_array = array[:(mid)]
                    return self._logic(temp_array)
                elif array[(mid) + 1] >= array[mid]:
                    temp_array = array[(mid):]
                    return self._logic(temp_array)
            elif n == 1:
                value = array[mid]
                return value
            else:
                if array[mid] > array[mid - 1]:
                    return array[mid]
                else:
                    return array[mid - 1]

    def runpeakfinder(self):
        val = self._logic(self.input)
        return (val)


if __name__ == "__main__":
    l = [1, 5, 35, 7, 8, 15, 20, 25, 30]
    t1 = Peak_finder(input=l)
    print(t1.runpeakfinder())
