from adapters.portable_adapter import PortableAdapter


class openai_Adapter(PortableAdapter):
    """Compatibility boundary for openai; does not require the vendor SDK."""

    framework = "openai"
