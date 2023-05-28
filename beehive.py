from __future__ import annotations
from dataclasses import dataclass
from heap import MaxHeap

@dataclass
class Beehive:
    """A beehive has a position in 3d space, and some stats."""

    x: int
    y: int
    z: int

    capacity: int
    nutrient_factor: int
    volume: int = 0

    def __gt__(self , other : Beehive) -> bool:
        return self.nutrient_factor * min(self.capacity , self.volume) > other.nutrient_factor * min(other.capacity , other.volume)

    def __le__(self , other : Beehive) -> bool:
        return self.nutrient_factor * min(self.capacity , self.volume) <= other.nutrient_factor * min(other.capacity , other.volume)

class BeehiveSelector:

    def __init__(self, max_beehives: int) -> None:
        self.my_beehive : MaxHeap[Beehive] = MaxHeap(max_size = max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]) -> None:
        self.my_beehive.length = 0
        for i in range (len(hive_list)):
            self.my_beehive.add(hive_list[i])
    
    def add_beehive(self, hive: Beehive) -> None:
        self.my_beehive.add(element = hive)
    
    def harvest_best_beehive(self) -> float:
        max_behive = self.my_beehive.get_max()
        if max_behive.capacity > max_behive.volume:
            new_volume = 0
        else:
            new_volume = max_behive.volume - max_behive.capacity

        new_behive : Beehive = Beehive(x = max_behive.x , y = max_behive.y , z = max_behive.z , capacity = max_behive.capacity, nutrient_factor = max_behive.nutrient_factor , volume = new_volume)

        self.add_beehive(hive = new_behive)

        return max_behive.nutrient_factor * min(max_behive.capacity , max_behive.volume)
    
  
