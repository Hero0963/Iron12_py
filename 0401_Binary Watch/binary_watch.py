from typing import List


# solution1
class Solution1:
    """
    time: O(1)
    space: O(1)
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # init
        self.size = 10
        self.num = turnedOn
        self.led_minute_num = 6
        self.hour_max_val = 12
        self.minute_max_val = 60
        self.ans = []

        # traverse all cases
        for i in range(2 ** self.size):
            self.leds = [0] * self.size
            tmp = i
            pos = self.size - 1

            # assign leds values
            while tmp > 0:
                r = tmp % 2
                if r != 0:
                    self.leds[pos] = 1

                tmp //= 2
                pos -= 1

            # print("==========")
            # print(i, pos, self.leds)

            if not self.is_correct_num():
                continue

            hours, minutes = self.convert_led_to_time()
            # print("********")
            # print(self.leds)
            # print(hours, minutes)
            if self.is_legal_time(hours, minutes):
                time = self.convert_to_required_format(hours, minutes)
                self.ans.append(time)

        # print(self.ans)
        return self.ans

    def is_correct_num(self) -> bool:
        count = 0
        for val in self.leds:
            if val == 1:
                count += 1

        if count != self.num:
            return False

        return True

    def convert_led_to_time(self) -> (int, int):
        hours, minutes = 0, 0
        for idx, val in enumerate(self.leds):
            if val == 0:
                continue

            if idx < self.led_minute_num:
                tmp = 1 << idx
                minutes += tmp
            else:
                tmp = 1 << (idx - self.led_minute_num)
                hours += tmp

        return hours, minutes

    def is_legal_time(self, hours: int, minutes: int) -> bool:
        if hours < self.hour_max_val and minutes < self.minute_max_val:
            return True

        return False

    def convert_to_required_format(self, hours: int, minutes: int) -> str:
        ts = ""
        if minutes < 10:
            ts = "0"

        time_str = str(hours) + ":" + ts + str(minutes)

        return time_str


# solution2
class Solution2:
    """
    time: O(1)
    space: O(1)
    """

    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        # init
        self.num = turnedOn
        self.hour_max_val = 12
        self.minute_max_val = 60
        self.ans = []

        # traverse all cases
        for h in range(self.hour_max_val):
            for m in range(self.minute_max_val):
                if (bin(h) + bin(m)).count("1") == self.num:
                    time = self.convert_to_required_format(h, m)
                    self.ans.append(time)

        return self.ans

    def convert_to_required_format(self, hours: int, minutes: int) -> str:
        ts = ""
        if minutes < 10:
            ts = "0"

        time_str = str(hours) + ":" + ts + str(minutes)

        return time_str
