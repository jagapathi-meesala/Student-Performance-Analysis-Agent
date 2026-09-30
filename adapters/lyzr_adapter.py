from adapters.portable_adapter import PortableAdapter


class lyzr_Adapter(PortableAdapter):
    """Compatibility boundary for lyzr; does not require the vendor SDK."""

    framework = "lyzr"
