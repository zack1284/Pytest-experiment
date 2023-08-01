import pytest

@pytest.fixture()
def fixture_demo():
    # setup
    print("\n連線資料庫")
    yield
    # teardown
    print("清空髒資料")

def test_case(fixture_demo):
    print("執行test_case")
    assert True


if __name__ == '__main__':
    pytest.main(["-s"])