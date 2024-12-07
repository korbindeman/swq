import router
import validation


def greet():
    name = validation.input(
        "Name: ",
        str,
        lambda name: name.strip() != "",
        "Name must be 1 character or longer",
    )
    age = validation.input(
        "Age: ", int, lambda age: 0 < int(age) < 200, "Age must be between 0 and 200"
    )
    if age is not None and name is not None:
        print(f"Hello {name}, next year you will be {age+1} years old!")


def main():
    r = router.Router()

    r.add_route("hello", lambda: print("Hello world!"))
    r.add_route("greet", greet)

    while True:
        route = input("Route to: ")
        if route != "":
            r.route_to(route)
        r.get_active_route_callback()()


if __name__ == "__main__":
    main()
