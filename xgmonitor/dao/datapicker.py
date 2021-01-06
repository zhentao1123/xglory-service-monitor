"""
data picker
"""
import json
from typing import Dict
from xgmonitor.dao.apporder import app_comm_ords, app_price_ords, app_sync_ords
from xgmonitor.dao.clopter import cl_run, cl_return


# base data picker
class BaseAppPicker:
    app_ords: Dict = None
    comm_ords: Dict = None
    log_path: str = None

    def __init__(self, app_ords: Dict, comm_ords: Dict):
        self.app_ords = app_ords
        self.comm_ords = comm_ords
        self.log_path = app_ords.get('log_path')

    # =======================================================

    def pick_time_count(self, keyword: str, time: str) -> str:
        command = self._reprocess_comm_command('time_count')\
                .replace('[keyword]', keyword)\
                .replace('[time]', time)
        return str(cl_return(command)[0]).replace(' ', '')

    def pick_time_count_hour(self, keyword: str, hour: str) -> str:
        command = self._reprocess_comm_command('time_count_hour')\
                .replace('[keyword]', keyword)\
                .replace('[hour]', hour)
        return str(cl_return(command)[0]).replace(' ', '')

    def pick_time_print(self, keyword: str, time: str) -> json:
        command = self._reprocess_comm_command('time_print') \
            .replace('[keyword]', keyword) \
            .replace('[time]', time)
        return json.dumps(cl_return(command))

    def pick_time_print_hour(self, keyword: str, hour: str) -> str:
        command = self._reprocess_comm_command('time_print_hour')\
                .replace('[keyword]', keyword)\
                .replace('[hour]', hour)
        return json.dumps(cl_return(command))

    # =======================================================

    # replace log path in command string
    def _replace_log_path(self, command: str) -> str:
        return command.replace('[log_path]', self.log_path)

    def _reprocess_comm_command(self, comm_ord_key: str):
        command = str(self.comm_ords.get(comm_ord_key))
        command = self._replace_log_path(command)
        return command


# sync data picker
class AppSyncPicker(BaseAppPicker):

    def pick_latest_queue_size(self) -> json:
        command = dict(self.app_ords.get('ords')).get('latest_queue_size')
        command = self._replace_log_path(command)
        return json.dumps(cl_return(command))


# price data picker
class AppPricePicker(BaseAppPicker):
    pass


# local test
syncPicker = AppSyncPicker(app_sync_ords, app_comm_ords)
# val = syncPicker.latest_queue_size()
# val = syncPicker.pick_time_count(keyword='queue.size', time='14:[0-9]{2}:[0-9]{2}')
# val = syncPicker.pick_time_count_hour(keyword='queue.size', hour='15')
# val = syncPicker.pick_time_print(keyword='queue.size', time='14:[0-9]{2}:[0-9]{2}')
val = syncPicker.pick_time_print_hour(keyword='queue.size', hour='14')
print(val)
