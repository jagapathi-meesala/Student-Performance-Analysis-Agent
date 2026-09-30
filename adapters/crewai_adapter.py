from adapters.portable_adapter import PortableAdapter


class crewai_Adapter(PortableAdapter):
    """Compatibility boundary for crewai; does not require the vendor SDK."""

    framework = "crewai"
