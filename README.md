# Zabbix Template for your BITMAIN ASIC

#### What needed?
Python 3+
#### How to start?

Import asic.xml into your zabbix

Copy source code in your server

Replace "/your/path/asic.py" with the path to file "asic.py"

Add this UserParameter in end your zabbix_agent.conf file
 
`UserParameter=asic.chains[*],python3 "/your/path/asic.py" -ac $1`

`UserParameter=asic.hashrate[*],python3 "/your/path/asic.py" -hr $1`

`UserParameter=asic.fan[*],python3 "/your/path/asic.py" -af $1 $2`

`UserParameter=asic.discovery,python3 "/your/path/asic.py" -at`

`UserParameter=asic.temp[*],python3 "/your/path/asic.py" -t $1`

Linking template to your zabbix host 
