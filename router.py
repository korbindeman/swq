from typing import Callable


class Router:
    active_route = ""
    routes = {}

    def add_route(self, routeKey: str, routeCallback: Callable) -> None:
        self.routes[routeKey] = routeCallback

    def route_to(self, routeKey: str) -> None:
        self.active_route = routeKey

    def get_active_route_callback(self) -> Callable:
        return self.routes[self.active_route]
