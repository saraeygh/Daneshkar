import getpass
from users import User


def main():
    """Th main body of code where user sends commands."""
    while True:
        print("🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠🏠")
        user_command = input(
            "[0] exit.\n"
            "[1] sign up.\n"
            "[2] sign in.\n"
            "Insert your command: "
        )

        match user_command:
            case "0":  # Exit
                break

            case "1":  # Sign up
                username = input("Username 👤: ")
                password = getpass.getpass(prompt="Password 🔒: ")
                phone_number = input("Phone number ☎️: ")
                if username in User.users_dict:
                    print("Username not available 😔")
                elif len(password) < 4:
                    print("Minimum password length is 4 😬")
                else:
                    User.sign_up(username, password, phone_number)

            case "2":  # Sign in
                username = input("Username👤: ")
                password = getpass.getpass(prompt="Password🔒: ")
                if User.sign_in(username, password):
                    sign_in_cmd = input(
                        "You signed in 😊\n"
                        "[1] show user info.\n"
                        "[2] edit user info.\n"
                        "[3] change password.\n"
                        "[4] main menu.\n"
                        "Insert your command: "
                    )
                    match sign_in_cmd:
                        case "1":  # Show user info
                            signined_user = User(
                                username,
                                password,
                                User.users_dict[username]["id"],
                                User.users_dict[username]["phone_number"],
                            )
                            print(signined_user)

                        case "2":  # Edit user info
                            new_user_name = input("Username👤: ")
                            new_phone_number = input("New phone☎️: ")
                            User.users_dict[new_user_name] = User.users_dict[username]
                            del User.users_dict[username]
                            User.users_dict[new_user_name][
                                "phone_number"
                            ] = new_phone_number

                        case "3":  # change password
                            old_password = getpass.getpass(prompt="Old pass🔒: ")
                            new_password = getpass.getpass(prompt="New pass🔒: ")
                            new_password_r = getpass.getpass(
                                prompt="New password again🔒: "
                            )
                            if User.change_pass(
                                username,
                                old_password,
                                new_password,
                                new_password_r
                            ):
                                print(
                                    "Old password or new password match error 😯"
                                )

                        case "4":  # Exit to main menu
                            print("Going back to main menu.")

                        case other:
                            print("Invalid command, sign in again 😯")
                else:
                    print("Invlaid username or password 😯")

            case other:
                print("Undefined command 😯")


if __name__ == "__main__":
    main()