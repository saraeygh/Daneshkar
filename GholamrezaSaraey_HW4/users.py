import uuid
import hashlib


class User:
    users_dict = {}

    def __init__(self, username: str, password: str, id: str, phone_number: str = None):
        """User class initializer function:

        Args:
            username (str): Should be unique.
            password (str): Should be private and 4 character minimum length.
            id (str): unique identifier that automatically generated.
            phone_number (str, optional): User phone number. Defaults to None.
        """
        self.username = username
        self.phone_number = phone_number
        self.__password = password
        self.id = id

    @classmethod
    def sign_up(cls, username: str, password: str, phone_number: str = None):
        """Sign up function that stores user information.

        Args:
            username (str): Username
            password (str): Password
            phone_number (str, optional): User phone number. Defaults to None.
        """
        password = cls.password_hash(password)
        cls.users_dict.update(
            {
                username: {
                    "Password": password,
                    "phone_number": phone_number,
                    "id": uuid.uuid4(),
                }
            }
        )

    @classmethod
    def sign_in(cls, username: str, password: str) -> bool:
        """Verifies user sign in.

        Args:
            username (str): Input username
            password (str): Input password

        Returns:
            bool: True means success / False means failure.
        """
        verification = cls.verify(username, password)
        if verification:
            return True
        return False

    @staticmethod
    def change_pass(
        username: str, old_password: str, new_password: str, new_password_r: str
    ) -> bool | None:
        """Method to change user password.

        Args:
            username (str): username.
            old_password (str): previous password.
            new_password (str): New password
            new_password_r (str): New password repetition.

        Returns:
            True or None: True means failure / None means password changed.
        """
        old_password = User.password_hash(old_password)
        if (
            old_password == User.users_dict[username]["Password"]
            and new_password == new_password_r
        ):
            new_password = User.password_hash(new_password)
            User.users_dict[username]["Password"] = new_password
        else:
            return True

    @staticmethod
    def verify(username: str, password: str) -> bool:
        """User verification.

        Args:
            username (str): Input username.
            password (str): Input password.

        Returns:
            bool: True means success / False means failure. 
        """
        password = User.password_hash(password)
        
        if (
            username in User.users_dict
            and password == User.users_dict[username]["Password"]
        ):
            return True
        return False
    
    @staticmethod
    def password_hash(password: str) -> str:
        """Hash input string (Password)

        Args:
            password (str): Input password as plain text.

        Returns:
            str: Hashed password as string.
        """
        password = password.encode()
        password = hashlib.sha256(password).hexdigest()
        return password

    def __str__(self) -> str:
        """Override __str__ magic method.

        Returns:
            str: User information. 
        """
        return f"Username: {self.username}\nID: {self.id}\nPhone: {self.phone_number}"