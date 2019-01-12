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
ttime = False


currentst = '' #this is a global string constantly updating variable containing recorded speech
dirpath = path.dirname(path.realpath(__file__))

########## BEHAVE PART ###########


@given("service is active")
def record_competed(context):
    context.recognizer = sr.Recognizer()
    # plus add some visualization to show user a change of state


@when("user pronounce {text}")
def when_user_pronounced_tag(context, text): #tag_name
    #audio_file = get_file(text) #Use this for non-test purposes
    audio_file = test_record(text)
    context.audio_file = audio_file
    pass


@when("program recognize input")
def recognize_command(context):
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_command = context.recognizer.recognize_sphinx(audio)
    print('recognized? : ' + context.recognized_command)
    #if record state -> coroutine
    if context.recognized_command == "record":
        print('recognized')
        startcoroutine()
    elif context.recognized_command == "precise record": #recognizer sucks sometimes ¯\_(ツ)_/¯
        print('recognized')
        startcoroutine()
        pass


@when("program recorded text {text}") #in future speech to text should be done in coroutine
def record_text(context, text):
    audio_file = test_file(text)
    context.audio_file = audio_file
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_text = context.recognizer.recognize_google(audio)
    currentst = context.recognized_text # sort of mock for the future updates
    print('recorded current: ' + currentst)
    print('recognized : ' + context.recognized_text)
    return 'Text recorded'


@when("program starts recording {text}")
def user_reads_text(context, text): #tag_name
    #audio_file = get_file(text) #Use this for non-test purposes
    audio_file = test_file(text)
    context.audio_file = audio_file
    pass


@when("piece of recorded part is finished")
def find_text(context):
    # here the coroutine with regex will be started in future, currently "hack" version below
    with open(dirpath + "/materials/" + "orwell_1984.txt", 'r') as myfile:
        data = myfile.read().replace('\n', '')
        find = context.recognized_text
        words = re.findall("\w+", data)
        result = [x for x in find if x in words]
        print('data: ' + data)
        print('currenst: ' + context.recognized_text)
        print(result) # in future, the pronounced part of text should be highlighted
    return 'Text found'


async def state_control():
    ttime = True
    await asyncio.sleep(3)
    ttime = False
    return ttime


async def checktextexistence(): #Mock for the future speech-to-text update
    await asyncio.sleep(0.1)
    return ttime


# @when("user pronounce {tag_name}")
# def when_user_pronounced_tag(context, tag_name): #tag_name
#     #tag_name.user_pronounced_tag = sr.Recognizer()
#     pass


# @when("time interval since last record < 3 sec")
# def when_time_interval_satisfied(context):
#     context.time_interval_satisfied = True


@then("note is recorded")
def tag_record(context):
    conn = sqlite3.connect(dirpath + "/notes_db.db")
    c = conn.cursor()
    c.execute(
        "Create TABLE if not exists notes (tag TEXT,content TEXT)")
    try:
        pass
        #c.execute() Execute our values not to lose note data
        #conn.commit()
    except Exception as err:
        print(err)
        pass
    context.reply = "Note Recorded. Tag?"
    startcoroutine()
    pass


@then("user pronounces {text}")
def when_user_pronounced_tag(context, text): #tag_name
    audio_file = tag_books(text)
    if ttime:
        context.audio_file = audio_file # Somewhat timer for operation recognition


@then("tag saved with a note")
def tag_save(context): #tag_name
    conn = sqlite3.connect(dirpath + "/notes_db.db")
    c = conn.cursor()
    c.execute(
        "Create TABLE if not exists notes (tag TEXT,content TEXT)")
    try:
        pass
        # c.execute() Execute our values not to lose note data
        # conn.commit()
    except Exception as err:
        print(err)
        pass
    context.reply = "Tag recorded"

########## ADDITIONAL STUFF #############


def startcoroutine():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    task = asyncio.ensure_future(state_control())
    loop.run_until_complete(task)
    print('Coroutine done')
    return 'Completed'


def refreshsearchcoroutine():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    task = asyncio.ensure_future(state_control())
    loop.run_until_complete(task)
    return 'Search part done'
