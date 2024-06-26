from aiogram import F, Router
from aiogram.filters import  StateFilter, Command
from aiogram.types import Message
from sqlalchemy.orm import sessionmaker

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state, State, StatesGroup
from keyboards.reply_menu import sets_cards_kb
from lexicon.lexicon_ru import LEXICON
from services.services import validate_set_name
from database.db_commands import add_set
router = Router()


# Creating state machine to keep track of a name of the set
# as well as valid name was given into handler or not
class FSMAddSet(StatesGroup):

    name = State()



# This handler is triggered when user enters command "/cancel"
@router.message(Command(commands='cancel'), StateFilter(FSMAddSet.name))
async def process_cancel_command(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(LEXICON[message.text], reply_markup=sets_cards_kb)


# This handler triggers when creating new set and asks for
# the name of a new set
@router.message(F.text == LEXICON['button_add_set'], StateFilter(default_state))
async def process_enter_name(message: Message, state: FSMContext):

    await message.answer(text=LEXICON['enter_set_name'])
    # setting a state for user to enter a name of the new set
    await state.set_state(FSMAddSet.name)


# This handler recieves the new name of the set, adds it to
# state as 'name', gets data from state, creates a new set in
# the 'data base' and clears the state afterwards
@router.message(StateFilter(FSMAddSet.name), F.text)
async def process_name_sent(message: Message, state: FSMContext, session_maker: sessionmaker):

    if not validate_set_name(message.text):
        await message.answer(text=LEXICON['not_valid_set_name'])
        await state.set_state(FSMAddSet.name)
        return

    # updating the name state
    await state.update_data(name=message.text)

    # getting data from the state
    current_state = await state.get_data()
    if current_state is None:
        return

    #creating a new set in 'data base'
    await add_set(user_id=message.from_user.id, set_name=current_state['name'], session_maker=session_maker)

    # clearing state
    await state.clear()
    await message.answer(text=f'Отлично! Колода с именем {message.text} был успешно создан', reply_markup=sets_cards_kb)


# This handler operates if user sent any data that is not text
@router.message(StateFilter(FSMAddSet.name))
async def warning_invalid_name(message: Message, state: FSMContext):
    await message.answer(
        text=LEXICON['invalid_name']
    )
