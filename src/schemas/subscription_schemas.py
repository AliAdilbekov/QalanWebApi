from pydantic import RootModel

class SubscriptionResponseSchema(RootModel[str]):
    def is_success(self) -> bool:
        return self.root.lower() == "ok"
