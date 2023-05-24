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
        return self.nutrient_factor * min(self.capacity , self.volume) >  other.nutrient_factor * min(other.capacity , other.volume)

    def __le__(self , other : Beehive) -> bool:
        return self.nutrient_factor * min(self.capacity , self.volume) <= other.nutrient_factor * min(other.capacity , other.volume)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.cur_hive : MaxHeap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        self.cur_hive.length = 0
        for i in range (len(hive_list)):
            self.cur_hive.add(hive_list[i])
    
    def add_beehive(self, hive: Beehive):
        self.cur_hive.add(element = hive)
    
    def harvest_best_beehive(self):
        gt_hive = self.cur_hive.get_max()
        if gt_hive.capacity > gt_hive.volume:
            new_volume = 0
        else:
            new_volume = gt_hive.volume - gt_hive.capacity

        self.add_beehive(Beehive(x= gt_hive.x, y=gt_hive.y, z=gt_hive.z, capacity = gt_hive.capacity, nutrient_factor = gt_hive.nutrient_factor ,volume = new_volume))

        return gt_hive.nutrient_factor * min(gt_hive.capacity,gt_hive.volume)