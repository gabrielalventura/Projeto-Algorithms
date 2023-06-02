from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("python", 1.45)

    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(23, 2)

    assert encrypt_message("python", 6) == "nohtyp"

    assert encrypt_message("python", 3) == "htyp_no"
