from dataclasses import dataclass
from typing import Optional


@dataclass
class ProjectData:
    id: int
    name: str
    description: str
    amount_floors: int
    rating: str
    image_url: Optional[str]