from mycroft import MycroftSkill, intent_file_handler


class RemoteController(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('controller.remote.intent')
    def handle_controller_remote(self, message):
        self.speak_dialog('controller.remote')


def create_skill():
    return RemoteController()

