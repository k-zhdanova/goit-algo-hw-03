from copy_files_app.main import main as run_copy_files_app
from koch_snowflake_app.main import main as run_koch_snowflake_app


def main():
    try:
        print(
            "Which app do you want to run? \n (1) Copy files \n (2) Koch snowflake \n (q) Quit \n"
        )
        action = input()

        if action == "1":
            run_copy_files_app()

        elif action == "2":
            run_koch_snowflake_app()

        elif action == "q":
            print("\nGood bye!")
            return
        else:
            print("\033[91mI don't understand that command\033[0m")

    except KeyboardInterrupt:
        print("\nGood bye!")
        return


if __name__ == "__main__":
    main()
