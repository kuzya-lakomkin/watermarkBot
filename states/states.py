from aiogram.utils.helper import Helper, HelperMode, ListItem


class PreprocessingStates(Helper):
    mode = HelperMode.snake_case

    START = ListItem()
    LINKS_INPUT = ListItem()
    POSITION_CHOICE = ListItem()
    GRABBING = ListItem()

