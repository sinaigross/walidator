WALIDS = [
    'walid',
    'waleed'  # actually the correct spelling
]


class Walid:
    pass


def is_walid(maybe_walid):
    return isinstance(maybe_walid, Walid) or \
           (
                   isinstance(maybe_walid, str) and
                   maybe_walid.lower() in WALIDS
           )
