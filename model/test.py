from model.instance_rhv import InstanceRhv
from model.instance_vmware import InstanceVmware
from utils import const
from utils.const import *
from utils.utils import exit_method


class Test(object):
    def __init__(self, json_current_test):
        self.name = json_current_test['Testname']
        self.description = json_current_test['Description']
        self.storage_class = json_current_test['STORAGE_CLASS']
        self.volume_mode = json_current_test['VOLUME_MODE']
        self.no_headless = json_current_test['NO_HEADLESS']
        self.test = json_current_test['Test']
        self.params_openshift = json_current_test['params.openshift']
        self.instance = self.init_instance(json_current_test["Instance"])
        self.instance_str = self.instance.get_str()

    def get_str(self):
        cli_str = self.description + "\n" + \
                  self.instance_str + \
                  const.STORAGE + self.storage_class + \
                  const.VOLUME + self.volume_mode + \
                  const.NO_HEADLESS + self.no_headless + \
                  const.YARN + self.test + \
                  const.PARAM_OCP + " " + self.params_openshift
        return cli_str

    @staticmethod
    def init_instance(json_current_inst):
        # print(json_current_inst)
        instance_type = str(json_current_inst["TYPE"]).upper()
        if instance_type == INST_RHV.upper():
            return InstanceRhv(json_current_inst)
        elif instance_type == INST_VMWARE.upper():
            return InstanceVmware(json_current_inst)
        else:
            exit_method(-1, "Wrong instance type!")
