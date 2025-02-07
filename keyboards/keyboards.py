from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='ℹ️ О нас', callback_data='about')],
    [InlineKeyboardButton(text='🛒 Товары', callback_data='shop')],
    [InlineKeyboardButton(text='📞 Поддержка', callback_data='support')],
])

about_us_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='📈 Проценты', callback_data='interest')],
    [InlineKeyboardButton(text='🏠 Вернуться на главную', callback_data='back_to_main_menu')]
])

interest_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🔙 Вернуться назад', callback_data='back_to_about')],
    [InlineKeyboardButton(text='🏠 Вернуться на главную', callback_data='back_to_main_menu')]
])

shop_keyboard = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='🛒 Посмотреть товары', callback_data='show_items')],
    [InlineKeyboardButton(text='🏠 Вернуться на главную', callback_data='back_to_main_menu')]
])
