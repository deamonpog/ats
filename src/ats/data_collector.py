import bfrac


class DataCollector:

    def __init__(self, in_riot_api_caller):
        self.riot_api_caller = in_riot_api_caller
        self.data = []

    def run_snowball(self, in_summoner_name, in_region_server, in_max_matches=10000):
        qc = bfrac.QueryContext(self.riot_api_caller)
        qc.set_region_server(in_region_server)
        qc.get_summoner_by_name(in_summoner_name)
        ml = qc.get_matches_list(100, "ranked", 420, in_start_time=0, in_start=0)

        qc.get_match_info(ml[0])
