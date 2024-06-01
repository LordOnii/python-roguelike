import numpy as np  # type: ignore
from tcod.console import Console

import data.tile_types as tile_types


class GameMap:
    def __init__(self, width: int, height: int):
        self.width, self.height = width, height

        # Initialize the tiles array with the wall tile
        self.tiles = np.full(
            (width, height),
            fill_value=tile_types.wall,
            order="F",
            dtype=tile_types.tile_dt
        )


    def in_bounds(self, x: int, y: int) -> bool:
        """Return True if x and y are inside of the bounds of this map."""
        return 0 <= x < self.width and 0 <= y < self.height

    def render(self, console: Console) -> None:
        console.rgb[0:self.width, 0:self.height] = self.tiles["dark"]