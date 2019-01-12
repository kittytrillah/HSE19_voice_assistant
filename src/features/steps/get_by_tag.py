from behave import given, when, then
import speech_recognition as sr
import asyncio
import re
import sqlite3
from os import path
get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "/materials/" + f.lower() + ".wav")
test_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "speech_test.wav")
test_record = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "record.wav")
tag_books = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "books.wav")
quotes = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "show_me_the_quotes.wav")
ttime = False


currentst = '' #this is a global string constantly updating variable containing recorded speech
dirpath = path.dirname(path.realpath(__file__))


########## BEHAVE PART ###########


@given("service activated")
def record_competed(context):
    context.recognizer = sr.Recognizer()


@when("user pronounces {text}")
def when_user_pronounced_tag(context, text): #tag_name
    #audio_file = get_file(text) #Use this for non-test purposes
    audio_file = quotes(text)
    context.audio_file = audio_file


@when("program recognizes input")
def recognize_command(context):
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_command = context.recognizer.recognize_sphinx(audio)
    print('recognized? : ' + context.recognized_command)
    #if record state -> coroutine
    if context.recognized_command == "show me the quotes":
        print('recognized show')
    elif context.recognized_command == "save the quotes":
        print('recognized save')
    elif context.recognized_command == "save the quotes in cloud":
        print('recognized save')


@when('program shows label "pronounce a tag"')
def show_label(context):
    print("Pronounce a tag")


@when("user says {text}")
def user_tag(context, text): #tag_name
    startcoroutine()
    #audio_file = get_file(text) #Use this for non-test purposes
    audio_file = tag_books(text)
    context.audio_file = audio_file
    pass


@then("program searches for the quotes with that tag above")
def lookfor_quotes(context):
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_command = context.recognizer.recognize_sphinx(audio)
    if ttime:
        print('recognized? : ' + context.recognized_command)
    #scroll through database and output


@then("program shows all of the tagged quotes")
def show_result(context):
    print("All quotes") #mock


@then("program saves all of the tagged quotes")
def save_result(context):
    print("All quotes saved") #mock


@then("program saves all of the tagged quotes in cloud")
def save_result(context):
    print("All quotes saved") #mock


########## ADDITIONAL STUFF #############


def startcoroutine():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    task = asyncio.ensure_future(state_control())
    loop.run_until_complete(task)
    print('Coroutine done')
    return 'Completed'


async def state_control():
    ttime = True
    await asyncio.sleep(5)
    ttime = False
    return ttime
