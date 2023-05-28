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
        """
            Check which nutrient_factor is greater between self and other.

            Args:
            - other : other beehive for compare.

            Returns:
            - it returns greater nutrient_factor.

            Complexity:
            - Best & Worst case : O(1)
        """
        return self.nutrient_factor * min(self.capacity , self.volume) >  other.nutrient_factor * min(other.capacity , other.volume)

    def __le__(self , other : Beehive) -> bool:
        """
            Check which nutrient_factor is lesser or equal between self and other.

            Args:
            - other : other beehive for compare.

            Returns:
            - it returns smaller or equal nutrient_factor.

            Complexity:
            - Best & Worst case : O(1)
        """
        return self.nutrient_factor * min(self.capacity , self.volume) <= other.nutrient_factor * min(other.capacity , other.volume)

class BeehiveSelector:

    def __init__(self, max_beehives: int):
        self.cur_hive : MaxHeap = MaxHeap(max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]):
        """
            Replace all current (possibly none) beehives in the selector
             with the beehives in the list provided as an argument.

            Args:
            - other : other beehive for compare.

            Returns:
            - it returns smaller or equal nutrient_factor.

            Complexity:
            - Best case & Worst case : O(M log M), M is len(hive_list)
        """
        self.cur_hive.length = 0
        for i in range (len(hive_list)):
            self.cur_hive.add(hive_list[i])
    
    def add_beehive(self, hive: Beehive):
        """
            Add beehive in BeehiveSelector.

            Args:
            - hive : Beehive

            Complexity:
            - Best & Worst case : O(log N), N : the number of beehives.
        """
        self.cur_hive.add(element = hive)
    
    def harvest_best_beehive(self):
        """
            Harvest with finding minimum between honey capacity and honey volume.

            Returns:
            - it will return the number of emeralds, 
              which is calculated with nutrient_factor * minimum value between capacity and volume.

            Complexity:
            - Best case & Worst case : O(log N), N : the number of beehives.
        """
        gt_hive = self.cur_hive.get_max()
        if gt_hive.capacity > gt_hive.volume:
            new_volume = 0
        else:
            new_volume = gt_hive.volume - gt_hive.capacity

        self.add_beehive(Beehive(x= gt_hive.x, y=gt_hive.y, z=gt_hive.z, capacity = gt_hive.capacity, nutrient_factor = gt_hive.nutrient_factor ,volume = new_volume))

        return gt_hive.nutrient_factor * min(gt_hive.capacity,gt_hive.volume)