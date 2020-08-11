class Instance(object):
    def __init__(self, json_current_instance):
        self.username = json_current_instance["V2V_INSTANCE_USERNAME"]
        self.password = json_current_instance["V2V_INSTANCE_PASSWORD"]
