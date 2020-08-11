from model.instance import Instance
from utils import const


class InstanceVmware(Instance):
    def __init__(self, json_current_instance):
        super().__init__(json_current_instance)
        self.hostname = json_current_instance["V2V_INSTANCE_HOSTNAME"]
        self.username = json_current_instance["V2V_INSTANCE_USERNAME"]
        self.password = json_current_instance["V2V_INSTANCE_PASSWORD"]

    def get_str(self):
        return const.HOSTNAME + self.hostname + \
               const.USERNAME + self.username + \
               const.PASSWORD + self.password
