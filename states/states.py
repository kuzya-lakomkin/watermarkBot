from aiogram.utils.helper import Helper, HelperMode, ListItem


class PreprocessingState(Helper):
    mode = HelperMode.snake_case

    links_input = ListItem()
    position_choice = ListItem()
    grabbing = ListItem()
