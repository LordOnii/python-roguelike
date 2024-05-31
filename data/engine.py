from typing import Set, Iterable, Any

from tcod.context import Context
from tcod.console import Console

from data.entity import Entity
from data.game_map import GameMap
from data.input_handlers import EventHandler


class Engine:
    def __init__(self, event_handler: EventHandler, game_map: GameMap, entities: Set[Entity], player: Entity):
        self.event_handler = event_handler
        self.game_map = game_map
        self.entities = entities
        self.player = player

    def handle_events(self, events: Iterable[Any]) -> None:
        for event in events:
            action = self.event_handler.dispatch(event)

            if action is None:
                continue

            action.perform(engine=self, entity=self.player)

    def render(self, console: Console, context: Context) -> None:
        self.game_map.render(console)

        for entity in self.entities:
            console.print(entity.x, entity.y, entity.char, fg=entity.color)

        context.present(console)

        console.clear()