import bfrac

from ats.data_collector import DataCollector

appconfig = bfrac.AppConfig("D:/PROJECTS/BFRAC/cj_config.ini")

rac = bfrac.RiotAPICaller(appconfig)

dc = DataCollector(rac)

dc.run_snowball("RowdyDrk", "na1")

