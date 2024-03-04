import sys


def add(x, y):
    return x + y

def test_add():

    # 正＋正＝正
    assert add(1, 2) == 3 # 1+2=3
    assert add(2, 2) == 4 # 2+2=4
    
    # 正+負＝負
    assert add(-1, 2) == 1 # -1+2=1
    
    # 負+負=負
    assert add(-1, -3) == -4 # -1-3=-4

    # 零值
    assert add(0, 0) == 0 # 0+0=0

    # 字串相加
    assert add("Hi","Pikachu") == "HiPikachu"
    
    print("add 測試通過")



def test_add_max_and_min():

    min_int = -sys.maxsize - 1
    max_int = sys.maxsize
    
    # 最小值加 1
    assert add(min_int, 1) == min_int + 1

    # 最大值加 1
    assert add(max_int, 1) == max_int + 1

    # 最小值減 1
    assert add(min_int, -1) == min_int - 1

    # 最大值減 1
    assert add(max_int, -1) == max_int - 1
    print("add_max_min 測試通過")

if __name__ == "__main__":
    test_add()
    test_add_max_and_min()
    print("測試完成")