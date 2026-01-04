from walidator import is_walid
from tests.classes import Walid, Waleed, NotWalid


def test_is_walid_on_str_walid_true():
    assert is_walid('walid')


def test_is_walid_on_str_waleed_true():
    assert is_walid('waleed')


def test_is_walid_on_class_walid_true():
    assert is_walid(Walid())


def test_is_walid_on_class_waleed_true():
    assert is_walid(Waleed())


def test_is_walid_on_class_not_walid_false():
    assert not is_walid(NotWalid())


def test_is_walid_on_str_sinai_false():
    assert not is_walid('sinai')
