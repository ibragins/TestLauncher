from model.instance import Instance
from utils import const


class InstanceVmware(Instance):
    def __init__(self, json_current_instance):
        super().__init__(json_current_instance)
        self.hostname = json_current_instance["V2V_VMWARE_INSTANCE_API_URL"]
        self.username = json_current_instance["V2V_VMWARE_INSTANCE_USERNAME"]
        self.password = json_current_instance["V2V_VMWARE_INSTANCE_PASSWORD"]

    def get_str(self):
        return const.VMWARE_HOSTNAME + self.hostname + \
               const.VMWARE_USERNAME + self.username + \
               const.VMWARE_PASSWORD + self.password
