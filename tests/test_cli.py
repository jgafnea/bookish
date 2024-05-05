from unittest.mock import patch

import pytest

from libget.cli import main


def test_without_arguments():
    with pytest.raises(SystemExit) as e:
        with patch("sys.argv", [""]):
            main()

    assert e.type == SystemExit
    assert e.value.code == 2
