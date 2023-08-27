from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐀𝐃𝐃 𝐌𝐄 𝐌𝐎𝐋 𝐋𝐎𝐕𝐄ʕ˖͜͡˖ʔ",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐎𝐖𝐍𝐄𝐑ʕ˖͜͡˖ʔ",
                url=f"https://t.me/N_O_B_I_T_A_007",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐇𝐄𝐋𝐏ʕ˖͜͡˖ʔ",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐒𝐄𝐓𝐓𝐈𝐍𝐆𝐒ʕ˖͜͡˖ʔ", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="•ʕ˖͜͡˖ʔ𝐀𝐃𝐃 𝐌𝐄 𝐓𝐎 𝐘𝐎𝐔𝐑 𝐆𝐑𝐎𝐔𝐏ʕ˖͜͡˖ʔ•",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐂𝐎𝐌𝐌𝐀𝐍𝐃𝐒ʕ˖͜͡˖ʔ", callback_data="settings_back_helper"
            ),
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐅𝐎𝐔𝐍𝐃𝐄𝐑ʕ˖͜͡˖ʔ", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐆𝐑𝐎𝐔𝐏", url=config.SUPPORT_GROUP
            ),
            InlineKeyboardButton(
                text="ʕ˖͜͡˖ʔ𝐔𝐏𝐃𝐀𝐓𝐄𝐒ʕ˖͜͡˖ʔ", url=f"https://t.me/about_skshivam"
            )
        ],
     ]
    return buttons
