# -*- coding:utf-8 -*-
import os
from lib import pycgminer as cgtools

from argparse import ArgumentParser
import json


class CCLi(ArgumentParser):
    def __init__(self):
        super().__init__()
        self.hosts_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_hosts")
        self.hosts = []
        if os.path.exists(self.hosts_path):
            with open(self.hosts_path, "r") as f:
                self.hosts = f.readline().replace(" ", "").strip().split(",")
                f.close()
        else:
            with open(self.hosts_path, "w"):
                pass
        self.add_argument('-at', '--asic_type', action='store_true')
        self.add_argument('-ac', '--asic_chains', action='store')
        self.add_argument('-t', '--temperature', action='store')
        self.add_argument('-af', '--asic_fan', nargs=2, action='store')
        self.add_argument('-temp', '--asic_temperature', action='store')
        self.add_argument('-hr', '--hashrate', action='store')
        self.add_argument('--fan-d', '--asic_fan_discovery', action='store')
        self.add_argument('--add_host', action='store')
        self._cli(self.parse_args())

    def _cli(self, parse_args_object):
        work_list = parse_args_object._get_kwargs()
        if len(work_list) != 0:
            for m in work_list:
                if type(m[1]) is list:
                    print(getattr(self, "%s" % m[0])(*m[1]))
                    break
                elif type(m[1]) is bool:
                    if m[1] is not False:
                        print(getattr(self, "%s" % m[0])())
                        break
                elif type(m[1]) is str or type(m[1]) is int:
                    print(getattr(self, "%s" % m[0])(m[1]))
                    break

    def hashrate(self, ip):
        stats = self._get_stats(ip)
        if stats:
            return stats[1]["GHS 5s"]
        else:
            return 0

    def temperature(self, ip):
        stats = self._get_stats(ip)
        if stats:
            return stats[1]["temp_max"]
        else:
            return 0

    def asic_type(self):
        data = []
        for i, ip in enumerate(self.hosts):
            stats_object = self._get_stats(ip)
            data_ip = ip.split(":")
            if len(data_ip) == 1:
                data_ip.append("4028")
            if stats_object is not None:
                chains = 0
                for chain in filter(lambda x: "chain_acn" in x, [*stats_object[1].keys()]):
                    if stats_object[1][chain] != 0:
                        chains += stats_object[1][chain]
                data.append({
                    "{#ASICINDEX}": i,
                    "{#ASICTYPE}": "%s" % stats_object[0]["Type"].replace("+", "plus"),
                    "{#ASICIP}": ip,
                    "{#TRUEASICIP}": data_ip[0],
                    "{#ASICPORT}": data_ip[1],
                    "{#ASICCHAINS}": chains

                })
            else:
                data.append({
                    "{#ASICTYPE}": "Error", "{#ASICIP}": ip, "{#TRUEASICIP}": data_ip[0], "{#ASICPORT}": data_ip[1]
                })
        return json.dumps({"data": data})

    def asic_fan(self, ip, fan):
        stats_object = self._get_stats(ip)
        if stats_object is not None:
            return stats_object[1]["fan{}".format(fan)]
        else:
            return 0

    def add_host(self, ip):
        with open(self.hosts_path, "a") as f:
            f.write(",%s" % str(ip))

    def asic_chains(self, ip):
        stats_object = self._get_stats(ip)
        if stats_object is not None:
            chains = 0
            for chain in filter(lambda x: "chain_acs" in x, [*stats_object[1].keys()]):
                if stats_object[1][chain] != "":
                    chains += stats_object[1][chain].strip().replace(" ", "").count("o")
            return chains
        else:
            return 0

    def _get_stats(self, ip):
        body = cgtools.get_stats(ip)
        if body["STATUS"][0]["STATUS"] != "error":
            return body["STATS"]
        else:
            return None


if __name__ == "__main__":
    CCLi()
