from dataclasses import dataclass
from typing import Optional


@dataclass
class ApartmentData:
    id: int
    num: Optional[int]
    on_sale: bool
    type_id: Optional[int]
    floor_id: Optional[int]
    section_id: Optional[int]
    building_id: Optional[int]
    image_url: Optional[str]