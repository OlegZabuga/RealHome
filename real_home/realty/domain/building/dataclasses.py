from dataclasses import dataclass
from typing import Optional


@dataclass
class BuildingData:
    id: int
    num: Optional[int]
    on_street: Optional[str]
    project_id: Optional[int]
    image_url: Optional[str]