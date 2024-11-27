from dataclasses import dataclass
from typing import Optional


@dataclass
class FloorData:
    id: int
    floor_number: Optional[int]
    section_id: Optional[int]