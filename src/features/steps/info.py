from behave import given, when, then
import speech_recognition as sr
import wikipedia
import asyncio
import re
import sqlite3
from os import path


########TEST RECORDED SPEECH###########
get_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "/materials/" + f.lower() + ".wav")
test_file = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "speech_test.wav")
test_record = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "record.wav")
tag_books = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "books.wav")
quotes = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "show_me_the_quotes.wav")
source = lambda f: path.join(path.dirname(path.realpath(__file__)), "materials/" + "source.wav")
########################################

ttime = False


currentst = '' #this is a global string constantly updating variable containing recorded speech
dirpath = path.dirname(path.realpath(__file__))


########## BEHAVE PART ###########


@given("service is enabled")
def record_competed(context):
    context.recognizer = sr.Recognizer()


@when("user chooses a quote")
def when_user_pronounced_tag(context): #tag_name
    #mock
    return 'Quote has been chosen'


@when("user pronounce: {text}")
def when_user_pronounced_source(context, text): #tag_name
    #audio_file = get_file(text) #Use this for non-test purposes
    audio_file = source(text)
    context.audio_file = audio_file


@when("program recognizes operation")
def recognize_command(context):
    with sr.AudioFile(context.audio_file) as source:
        audio = context.recognizer.record(source)
    context.recognized_command = context.recognizer.recognize_sphinx(audio)
    print('recognized? : ' + context.recognized_command)
    if context.recognized_command == "source":
        print('recognized show')
    if "find author" in context.recognized_command:
        context.auname = context.recognized_command.replace("find author", "")
        print('recognized save')

@then("program reads meta")
def read_result(context):
    print("Reading meta") #mock


@then("program shows meta info")
def show_meta_result(context):
    print("Showing meta") #mock


@then("looks for author info using Wikipedia API")
def wiki_look(context):
    author = wikipedia.page(context.auname)
    author.sections
    print("looks for author info using Wikipedia API") #mock


@then("program shows info")
def show_result(context):
    print("Author Info") #mock