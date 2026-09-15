class ValidationError(ValueError):
    """Erreur de validation exposable au client et à Sentry."""

    def __init__(self, code: str, *, field: str):
        self.code = code
        self.field = field
        super().__init__(code)
