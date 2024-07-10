class SiteMaprException(Exception):
    ...


class InvalidSiteMapPriority(SiteMaprException):
    def __init__(self, priority: str) -> None:
        super().__init__(
            f"Invalid priority value: {priority}. Priority must be between 0.0 and 1.0."
        )
