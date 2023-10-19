# Not really sure what I am doing with this app; might get deleted
from icecream import ic

class Application():
    def run(self) -> int:
      ic("Placeholder for future setup")
      return 0


def main() -> int:
    app = Application()
    exit_code: int = app.run()
    return exit_code


if __name__ == "__main__":
    main()
