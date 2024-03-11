
LEXICON: dict[str, str] = {
    '/start': '<b>Привет!</b>\n\nЭто бот, в котором '
              'ты можешь учиться используя "флэш-карточки".'
              '\n\nЧтобы посмотреть список доступных '
              'команд - набери /help',
    '/help': '<b>Это Анки бот</b>\n\nДоступные команды:\n\n/sets - '
              'Навигация по колодам карточек.\n/cards - показать все '
              'карточки колоды.\n/addcard - добавить карточку в колоду. '
              '\n/help - справка по работе бота.',
    '/cancel': 'Отмена произошла успешно',
    'echo_response': 'Извините, не могу распознать данную команду.\n'
                      '/help - справка по работе бота.',
    'cancel': 'Отменить',
    'keyboard_sets': 'Все ваши колоды:',
    'front_side': 'Пожалуйста, введите лицевую сторону карты:',
    'back_side': 'Пожалуйста, введите обратную сторону карты:',
    'enter_set_name': 'Пожалуйста, введите название колоды:',
    'invalid_name': 'То, что вы отправили не похоже на текст\n\n'
             'Пожалуйста, введите текст\n\n'
             'Если вы хотите прервать ввод названия - '
             'отправьте команду /cancel',
    'no_sets': 'Вы еще не создали ни одной колоды карточек. \n'
               '/help - справка по работе бота.',
    'no_cards': 'В данной колоде нету карт\n'
               '/help - справка по работе бота.',
    'choose_del_set_card': 'Выбирите что вы хотите сделать: ',
    'answer': 'Перевернуть',
    'hint': 'Подсказка',
    'not_valid_set_name': 'Введенный вами текст слишком длиный. Повторите еще раз:',
    'next': 'Далее',
    'choose_set': 'Выберите колоду:',
    'edit_sets': 'Редактировать',
    'button_sets': 'Мои колоды',
    'button_study': 'Учить карточки',
    'button_cards': 'Мои карты',
    'button_add_set': 'Добавить колоду',
    'button_add_card': 'Добавить карту',
    'success': 'Операция была совершена успешно!',
    'del_choosen_card': 'Выберите карту которую хотите удалить:',
    'del_set': 'Выберите колоду который хотите удалить: ',
    'del_smbl': '❌',

}

LEXICON_COMMANDS: dict[str, str] = {
    '/start': 'Начало работы',
    '/help': 'Справка по работе бота',
    '/sets': 'Показывает все доступные вам колоды',
    '/addset': 'Показывает все карточки выбранной колоды',
    '/addcard': 'Добавить карточку в выбранную колоду',
    '/cancel': 'Отмена'
}