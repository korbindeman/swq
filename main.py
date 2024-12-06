import router


def main():
    r = router.Router()

    r.addRoute("hello", lambda: print("Hello world!"))
    r.addRoute("pablo", lambda: print("Hello Pablo!"))

    while True:
        route = input("Route to: ")
        if route != "":
            r.routeTo(route)
        r.getActiveRouteCallback()()


if __name__ == "__main__":
    main()
