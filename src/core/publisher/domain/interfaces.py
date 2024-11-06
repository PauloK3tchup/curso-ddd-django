from abc import ABC, abstractmethod
from core.publisher.domain.entities import Publisher
from typing import List

class PublisherRepository(ABC):
    @abstractmethod
    def create(self, publisher: Publisher) -> Publisher:
        raise NotImplementedError
    
    @abstractmethod
    def list(self) -> List[Publisher]:
        raise NotImplementedError