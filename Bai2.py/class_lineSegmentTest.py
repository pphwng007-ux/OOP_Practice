
import math


# =========================
# CLASS POINT
# =========================
class Point:

    # Hàm xây dựng mặc định
    def __init__(self, x=0, y=1):
        self.__x = x
        self.__y = y

    # Nhập tọa độ
    def read(self):
        self.__x, self.__y = map(int, input().split())

    # In tọa độ
    def print(self):
        print(f"({self.__x}, {self.__y})")

    # Dời điểm
    def move(self, dx, dy):
        self.__x += dx
        self.__y += dy

    # Lấy x
    def getX(self):
        return self.__x

    # Lấy y
    def getY(self):
        return self.__y

    # Tính khoảng cách
    def distance(self, P=None):

        # Khoảng cách đến gốc tọa độ
        if P is None:
            return math.sqrt(self.__x ** 2 + self.__y ** 2)

        # Khoảng cách đến điểm P
        return math.sqrt(
            (self.__x - P.getX()) ** 2 +
            (self.__y - P.getY()) ** 2
        )


# =========================
# CLASS LINESEGMENT
# =========================
class LineSegment:

    # Hàm xây dựng
    def __init__(self, *args):

        # Không đối số
        if len(args) == 0:
            self.__d1 = Point(8, 5)
            self.__d2 = Point(1, 0)

        # 2 đối tượng Point
        elif len(args) == 2 and isinstance(args[0], Point):
            self.__d1 = args[0]
            self.__d2 = args[1]

        # 4 số nguyên
        elif len(args) == 4:
            self.__d1 = Point(args[0], args[1])
            self.__d2 = Point(args[2], args[3])

        # Sao chép sâu
        elif len(args) == 1 and isinstance(args[0], LineSegment):

            s = args[0]

            self.__d1 = Point(
                s.__d1.getX(),
                s.__d1.getY()
            )

            self.__d2 = Point(
                s.__d2.getX(),
                s.__d2.getY()
            )

    # Nhập đoạn thẳng
    def read(self):

        x1, y1, x2, y2 = map(int, input().split())

        self.__d1 = Point(x1, y1)
        self.__d2 = Point(x2, y2)

    # In đoạn thẳng
    def print(self):

        print(
            f"[({self.__d1.getX()}, {self.__d1.getY()}); "
            f"({self.__d2.getX()}, {self.__d2.getY()})]"
        )

    # Tịnh tiến đoạn thẳng
    def move(self, dx, dy):

        self.__d1.move(dx, dy)
        self.__d2.move(dx, dy)

    # Tính độ dài
    def length(self):

        return self.__d1.distance(self.__d2)

    # Tính góc
    def angle(self):

        dx = self.__d2.getX() - self.__d1.getX()
        dy = self.__d2.getY() - self.__d1.getY()

        angle = math.degrees(math.atan2(dy, dx))

        if angle < 0:
            angle += 360

        return round(angle)


# =========================
# CLASS TEST
# =========================
class LineSegmentTest:

    # Kịch bản 1
    @staticmethod
    def testCase1():

        A = Point(2, 5)
        B = Point(20, 35)

        AB = LineSegment(A, B)

        AB.move(35, 51)

        print("Doan thang AB sau khi tinh tien:")
        AB.print()

    # Kịch bản 2
    @staticmethod
    def testCase2():

        CD = LineSegment()

        print("Nhap toa do doan thang CD:")
        CD.read()

        print(f"|CD| = {CD.length():.2f}")

    # Kịch bản 3
    @staticmethod
    def testCase3():

        n = int(input("Nhap so doan thang: "))

        ds = []

        for i in range(n):

            print(f"Nhap doan thang thu {i + 1}:")

            x1, y1, x2, y2 = map(int, input().split())

            s = LineSegment(x1, y1, x2, y2)

            ds.append(s)

        # Sắp xếp tăng dần theo chiều dài
        ds.sort(key=lambda x: x.length())

        print("\nDanh sach doan thang tang dan theo chieu dai:")

        for s in ds:
            s.print()

    # Hàm main
    @staticmethod
    def main():

        print("========== TEST CASE 1 ==========")
        LineSegmentTest.testCase1()

        print("\n========== TEST CASE 2 ==========")
        LineSegmentTest.testCase2()

        print("\n========== TEST CASE 3 ==========")
        LineSegmentTest.testCase3()


# =========================
# CHẠY CHƯƠNG TRÌNH
# =========================
if __name__ == "__main__":
    LineSegmentTest.main()

