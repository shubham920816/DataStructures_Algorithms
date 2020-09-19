class PeakFinder(object):

    def __init__(self, input_val=[]):
        """

        Args:
            input_val :
        """
        self.input = input_val

    def _logic(self, array=[]):
        """

        Args:
            array:

        Returns:

        """
        n = len(array)
        mid = int(n / 2)

        if n > 2:
            if (array[mid] >= array[mid + 1]) and (array[mid] >= array[(mid) - 1]):
                value = array[mid]
                return value

            elif array[mid - 1] >= array[mid]:
                temp_array = array[:mid]
                return self._logic(temp_array)
            elif array[mid + 1] >= array[mid]:
                temp_array = array[mid:]
                return self._logic(temp_array)
        elif n == 1:
            value = array[mid]
            return value
        else:
            if array[mid] > array[mid - 1]:
                return array[mid]
            else:
                return array[mid - 1]

    def run_peak_finder(self):
        """

        Returns:

        """
        value = self._logic(self.input)
        return (value)


if __name__ == "__main__":

    val = [1, 5, 35, 7, 8, 15, 20, 25, 30]
    t1 = PeakFinder(input_val=val)
    print(t1.run_peak_finder())
