from utils import SCORES_FILE_NAME, MAX_DIFF


def user_points(user_diffivalty: int = MAX_DIFF):
    try:
        with open(SCORES_FILE_NAME, 'r+') as file:
            num = int(file.read()) + user_diffivalty * 3 + 5
            file.write(str(num))
    except:
        with open(SCORES_FILE_NAME, 'w') as file1:
            file1.write(str(user_diffivalty * 3 + 5))
