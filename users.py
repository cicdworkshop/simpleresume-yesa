"""This file is the module to get users data from database. But, for the purpose of the workshop, it reads the users
data from the dummy file.
"""
import yaml


class User:
    def __init__(self):
        self.user_id: str           = ""
        self.name: str              = ""
        self.address: str           = ""
        self.phone: str             = ""
        self.email: str             = ""
        self.description: str       = ""
        self.linkedin_url: str      = ""
        self.github_url: str        = ""
        self.experiences: list      = []
        self.education: list        = []
        self.certifications: list   = []


    def sort_user_experience(self):
        """Sort users experience based on chronological order. The most recent experience should be first.
        """
        self.experiences = sorted(self.experiences, key=lambda x: x["title"])

    # (FOR WORKSHOP)
    # Implement the function to sort user certifications based on the chronological order.
    # Copy the above function, paste it below, and modify it to sort user certifications.


def load_dummy_users() -> list:
    """This function loads dummy user data. In the real-world, this should get users data from database.
    For the workshop, this read users from a file.

    Returns:
        dummy_users: List of user object.
    """
    filename = "dummy_users.yaml"
    dummy_users = yaml.load(open(filename), Loader=yaml.FullLoader)
    users = []
    for user_id, user_data in dummy_users.items():
        user = User()
        user.user_id        = user_id
        user.name           = user_data["name"]
        user.address        = user_data["address"]
        user.phone          = user_data["phone"]
        user.email          = user_data["email"]
        user.description    = user_data["description"]
        user.linkedin_url   = user_data["linkedin_url"]
        user.github_url     = user_data["github_url"]
        user.experiences    = user_data["experiences"]
        user.education      = user_data['education']
        user.certifications = user_data["certifications"]
        user.sort_user_experience()
        # (FOR WORKSHOP)
        # Call the function to sort user certifications.
        users.append(user)
    return users
