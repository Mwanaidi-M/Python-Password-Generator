import secrets
import string
import pyperclip


def random_password(pwd_length=8):
    """
    This is a function that generates a random password of variable length based on the user input but
    default length is 8.
    The random password will have:
    - At least 1 uppercase letter.
    - At least 1 lowercase letter.
    - At least 1 numerical digit.
    - At least 1 special character.

    :param pwd_length: <int>
    :return: new_pwd: <str>
    """

    # display a welcome message
    welcome = " M's RANDOM PASSWORD GENERATOR "
    print(f"{welcome:-^100}")

    # create variables for the letters, numbers & special characters
    all_letters = string.ascii_letters
    all_digits = string.digits
    all_special = string.punctuation

    # combine the variables into one string
    all_xters = all_letters + all_digits + all_special

    # using a while loop to check if the password has at least 1 uppercase, lowecase letter, number & special character
    while True:
        new_pwd = ''.join(secrets.choice(all_xters) for xter in range(pwd_length))

        if (any(xter.islower() for xter in new_pwd)) and (any(xter.isdigit() for xter in new_pwd)) and (
                any(xter.isupper() for xter in new_pwd)) and (any(xter for xter in all_special)):
            break

    print(f"Generated Password is: {new_pwd}")
    print(f"Password has been copied to your clipboard so you can paste it as well.\U0001F973\U0001F973\U0001F973")

    pyperclip.copy(new_pwd)


# calling the main function
random_password()
