from abc import ABC, abstractmethod
from models.match import Match


class BaseProvider(ABC):

    @abstractmethod
    def get_live_matches(self) -> list[Match]:
        pass