WALIDS = [
    'walid',
    'waleed'  # actually the correct spelling
]


def is_walid(maybe_walid):
    maybe_walid = maybe_walid if isinstance(maybe_walid, str) \
        else type(maybe_walid).__name__
    return maybe_walid.lower() in WALIDS
