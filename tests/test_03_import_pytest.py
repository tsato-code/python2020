import pytest
import sys

def test_sample():
        x = "this"
        assert 'h' in x


if __name__=="__main__":
    # ヘルプの表示
    # pytest.main(["-h"])
    sys.exit(pytest.main())


    