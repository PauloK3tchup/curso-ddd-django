from dataclasses import dataclass
from uuid import UUID
from typing import List
from core.publisher.domain.interfaces import PublisherRepository

@dataclass
class ListPublisherOutput:
    id: UUID
    name: str
    description: str
    is_active: bool

class ListPublisherUseCase:
    def __init__(self, repository: PublisherRepository):
        self.prepository = repository

    def execute(self) -> List[ListPublisherOutput]:
        publishers = self.repository.list()
        return [ListPublisherOutput(
            id=publisher.id,
            name=publisher.name,
            description=publisher.description,
            is_active=publisher.is_active
        ) for publisher in publishers]