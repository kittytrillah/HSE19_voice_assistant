from behave import given, when, then
import speech_recognition as sr


@given("record of quote completed")
def record_competed(context):

    context.record_completed = ["Record completed"]


@when("user pronounce {tag_name}")
def when_user_pronounced_tag(tag_name): #tag_name
    #tag_name.user_pronounced_tag = sr.Recognizer()
    pass


@when("time interval since last record < 4 sec")
def when_time_interval_satisfied(context):
    context.time_interval_satisfied = True


@then("tag recorded")
def tag_recorded(context, tag_name):
    #assert context.reply == "Tag Recorded" // leave it for representation
    context.tag_added = [tag_name]


@then("succeed code in status bar")
def succeed_code_in_status_bar(context, tag_name):
    assert context.reply == "Tag recorded: " + tag_name
