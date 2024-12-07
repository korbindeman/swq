import router


def main():
    r = router.Router()

    r.add_route("hello", lambda: print("Hello world!"))
    r.add_route("pablo", lambda: print("Hello Pablo!"))

    while True:
        route = input("Route to: ")
        if route != "":
            r.route_to(route)
        r.get_active_route_callback()()


if __name__ == "__main__":
    main()
