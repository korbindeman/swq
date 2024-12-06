from typing import Callable


class Router:
    activeRoute = ""
    routes = {}

    def addRoute(self, routeKey: str, routeCallback: Callable) -> None:
        self.routes[routeKey] = routeCallback

    def routeTo(self, routeKey: str) -> None:
        self.activeRoute = routeKey

    def getActiveRouteCallback(self) -> Callable:
        return self.routes[self.activeRoute]
