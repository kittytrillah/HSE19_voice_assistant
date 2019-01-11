from behave import given, when, then
import speech_recognition as sr
import asyncio
from os import path
get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "/materials/" + f.lower() + ".wav")
test_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "speech_test.wav")
test_record = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "record.wav")
ttime = False


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



#@when("time interval since last record < 3 sec")
async def state_control(context):
    ttime = True
    await asyncio.sleep(3)
    ttime = False
    return ttime


# @when("user pronounce {tag_name}")
# def when_user_pronounced_tag(context, tag_name): #tag_name
#     #tag_name.user_pronounced_tag = sr.Recognizer()
#     pass


# @when("time interval since last record < 3 sec")
# def when_time_interval_satisfied(context):
#     context.time_interval_satisfied = True


@then("record state is activated")
def tag_recorded(context):
    #assert context.reply == "Tag Recorded" // leave it for representation
    #context.tag_added = [tag_name]
    pass


@then("user pronounces what has to be recorded")
def succeed_code_in_status_bar(context):
    #assert context.reply == "Tag recorded: " + tag_name
    pass


########## ADDITIONAL STUFF #############


def startcoroutine():
    loop = asyncio.get_event_loop()
    future = asyncio.Future()
    task = asyncio.ensure_future(state_control(""))
    loop.run_until_complete(task)
    print('Coroutine done')
    return 'Completed'
