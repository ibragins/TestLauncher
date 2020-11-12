from model.instance import Instance
from utils import const


class InstanceRhv(Instance):
    def __init__(self, json_current_instance):
        super().__init__(json_current_instance)
        self.urlApi = json_current_instance["V2V_RHV_INSTANCE_API_URL"]
        self.port = json_current_instance["V2V_RHV_INSTANCE_PORT"]
        self.urlSuffix = "/ovirt-engine/api"
        self.username = json_current_instance["V2V_RHV_INSTANCE_USERNAME"]
        self.password = json_current_instance["V2V_RHV_INSTANCE_PASSWORD"]
        self.caCertPath = json_current_instance["V2V_RHV_INSTANCE_CA_CERT"]
        self.caCert = "$(cat " + self.caCertPath + ")"
        self.cluster = json_current_instance["V2V_RHV_INSTANCE_CLUSTER"]
        self.urlFull = self.urlApi + ":" + self.port + self.urlSuffix

    def get_str(self):
        return const.RHV_URL + self.urlFull + \
               const.RHV_USERNAME + self.username + \
               const.RHV_PASSWORD + self.password + \
               const.RHV_CERT + self.caCert + \
               const.RHV_CLUSTER + self.cluster
