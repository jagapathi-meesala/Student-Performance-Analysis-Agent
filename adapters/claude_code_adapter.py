from adapters.portable_adapter import PortableAdapter


class claude_code_Adapter(PortableAdapter):
    """Compatibility boundary for claude_code; does not require the vendor SDK."""

    framework = "claude_code"
