"Typed environment configuration for ChatJiXia."

from chatenv import BaseEnvConfig, EnvField


class ChatjixiaConfig(BaseEnvConfig):
    "ChatJiXia ChatEnv configuration."

    _title = "ChatJiXia Configuration"
    _aliases = ["chatjixia"]
    _storage_dir = "Chatjixia"

    @classmethod
    def test(cls) -> None:
        """Validate schema registration without external side effects."""

        print(f"Testing {cls._title}...")
        print("Schema loaded; no network test is required.")

    CHATJIXIA_API_KEY = EnvField(
        "CHATJIXIA_API_KEY",
        desc="API key",
        is_sensitive=True,
    )


__all__ = ["ChatjixiaConfig"]
