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
        return self.nutrient_factor * min(self.capacity , self.volume) > other.nutrient_factor * min(other.capacity , other.volume)

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

    def __init__(self, max_beehives: int) -> None:
        self.my_beehive : MaxHeap[Beehive] = MaxHeap(max_size = max_beehives)

    def set_all_beehives(self, hive_list: list[Beehive]) -> None:
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
        self.my_beehive.length = 0
        for i in range (len(hive_list)):
            self.my_beehive.add(hive_list[i])
    
    def add_beehive(self, hive: Beehive) -> None:
        """
            Add beehive in BeehiveSelector.

            Args:
            - hive : Beehive

            Complexity:
            - Best & Worst case : O(log N), N : the number of beehives.
        """
        self.my_beehive.add(element = hive)
    
    def harvest_best_beehive(self) -> float:
        """
            Harvest with finding minimum between honey capacity and honey volume.

            Returns:
            - it will return the number of emeralds, 
              which is calculated with nutrient_factor * minimum value between capacity and volume.

            Complexity:
            - Best case & Worst case : O(log N), N : the number of beehives.
        """
        max_behive = self.my_beehive.get_max()
        if max_behive.capacity > max_behive.volume:
            new_volume = 0
        else:
            new_volume = max_behive.volume - max_behive.capacity

        new_behive : Beehive = Beehive(x = max_behive.x , y = max_behive.y , z = max_behive.z , capacity = max_behive.capacity, nutrient_factor = max_behive.nutrient_factor , volume = new_volume)

        self.add_beehive(hive = new_behive)

        return max_behive.nutrient_factor * min(max_behive.capacity , max_behive.volume)
    
  
