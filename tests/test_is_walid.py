from walidator import is_walid, Walid


def test_is_walid_on_str_walid_true():
    assert is_walid('walid')


def test_is_walid_on_str_waleed_true():
    assert is_walid('waleed')


def test_is_walid_on_class_walid_true():
    assert is_walid(Walid())


def test_is_walid_on_str_sinai_false():
    assert not is_walid('sinai')
