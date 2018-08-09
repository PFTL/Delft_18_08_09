import sys
sys.path.append('/home/aquiles/Documents/ZZP/Delft')
from PythonForTheLab.Model.experiment.IV_measurement import Experiment

e = Experiment()
e.load_config('Config/experiment_dummy.yml')
e.load_daq()
e.do_scan()
e.save_scan_data('filename.txt')