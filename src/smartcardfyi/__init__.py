"""smartcardfyi — Smart card encyclopedia API client for developers.

Look up smart card types, chip platforms, standards, manufacturers,
and certifications from SmartCardFYI.

Usage::

    from smartcardfyi.api import SmartCardFYI

    with SmartCardFYI() as api:
        results = api.search("emv")
        print(results)
"""

__version__ = "0.1.0"
