# Zabbix Template for your BITMAIN ASIC

#### Tested
We are testing our script on antminer L3+ and S9 with original frimware(L3) and vnish 3.8.6(S9)

#### What needed?
Python 3+
#### How to start?

Import asic.xml into your zabbix

Copy source code in your server

Replace "/your/path/asic.py" with the path to your source files

Add this UserParameter in end your zabbix_agent.conf file
 
`UserParameter=asic.chains[*],python3 "/your/path/asic.py" -ac $1`

`UserParameter=asic.hashrate[*],python3 "/your/path/asic.py" -hr $1`

`UserParameter=asic.fan[*],python3 "/your/path/asic.py" -af $1 $2`

`UserParameter=asic.discovery,python3 "/your/path/asic.py" -at`

`UserParameter=asic.temp[*],python3 "/your/path/asic.py" -t $1`

Add in file saved_hosts asic ip's. For example: 10.10.10.10,10.10.10.2,10.10.10.100:3000

Linking template to your zabbix host 

#### !!! Attention !!!
If you use forwarding port, you most be forward to port 4028
