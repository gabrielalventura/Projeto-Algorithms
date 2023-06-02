from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("python", "B")

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(23, 2)

    assert encrypt_message("python", 9) == "nohtyp"

    assert encrypt_message("python", 3) == "typ_noh"

    assert encrypt_message("python", 2) == "noht_yp"
