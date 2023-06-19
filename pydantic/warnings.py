__all__ = ('PydanticDeprecationWarning',)


class PydanticDeprecationWarning(DeprecationWarning):
    message: str
    since: tuple[int, int]

    def __init__(self, message: str, *args: object, since: tuple[int, int]) -> None:
        super().__init__(message, *args)
        self.message = message.rstrip('.')
        self.since = since

    def __str__(self) -> str:
        message = f'{self.message}. Deprecated in Pydantic V{self.since[0]}.{self.since[1]}.'
        if self.since == (2, 0):
            message += ' See Pydantic V2 Migration Guide at https://docs.pydantic.dev/v2/migration/'
        return message
