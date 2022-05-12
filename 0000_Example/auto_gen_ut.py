import os
import shutil


def get_target_list(file):
    with open(file, encoding="utf-8") as f:
        target_name_list = f.read().strip().split("\n")

    return target_name_list


def handle_name(target):
    sidx = target.index("_")
    new = target[sidx + 1:]
    new = new.lower()
    new = new.replace(" ", "_")
    return new


def get_filename(target):
    new = handle_name(target)
    filename = new + "__test.py"
    return filename


def get_source(target):
    ori = "D://PythonProject//leetcode//" + target + ".py"

    name = handle_name(target)
    new = "D://PythonProject//leetcode//" + name + ".py"
    os.rename(ori, new)

    source = new
    return source


def get_dirname(target):
    dirname = target
    return dirname


def get_text():
    paragraphs = []

    paragraphs.append("""
import unittest
from dataclasses import dataclass

from tbd import Solution1
import time

total_loop = 1000
print("total_loop= ", total_loop)

"""
                      )

    paragraphs.append("""

@dataclass
class TestData:
    nums: None
    ans: int
    
""")

    paragraphs.append("""

def generate_data():
    data = [TestData([2,2,1],1),
            TestData([4,1,2,1,2],4),
            ]

    return data
    
""")

    paragraphs.append("""

class TestSol1(unittest.TestCase):

    def setUp(self):
        self.args = (generate_data())
        # print("self.args= ", self.args)

    def tearDown(self):
        self.args = None

    def test_twoSum(self):

        time_start = time.process_time()

        for count in range(total_loop):
            for arg in self.args:
                expected = arg.ans
                s= Solution1()
                actual = s.tbd(arg.n)
                self.assertEqual(expected, actual)

        time_end = time.process_time()

        print( self.__class__name +" runtime= ", time_end - time_start)


""")

    paragraphs.append("""

if __name__ == '__main__':
    unittest.main()
""")

    text = ""
    for p in paragraphs:
        text += p

    return text


def main():
    target_list = get_target_list("targetNameList.txt")

    for target in target_list:
        dirname = get_dirname(target)
        path = "D://PythonProject//leetcode//" + dirname
        if not os.path.isdir(path):
            os.mkdir(path)

        filename = get_filename(target)
        text = get_text()
        with open(path + "//" + filename, "w") as f:
            f.write(text)

        destination = path

        source = get_source(target)
        shutil.move(source, destination)

    print("finish")


if __name__ == '__main__':
    main()
