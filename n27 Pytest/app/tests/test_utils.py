from app.utils import root

def test_root() -> None:
    result = root(25)

    print(f"Result of root 25: {result}")
    assert result == 5