#### Add this UserParameter in end your zabbix_agent.conf file

`UserParameter=gpu.number,"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" -L | find /c /v ""`

`UserParameter=gpu.discovery,C:\scripts\get_gpus_info.bat`

`UserParameter=gpu.fanspeed[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=fan.speed --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.power[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=power.draw --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.temp[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=temperature.gpu --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.utilization[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=utilization.gpu --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.memfree[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=memory.free --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.memused[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=memory.used --format=csv,noheader,nounits -i $1`

`UserParameter=gpu.memtotal[*],"C:\Program Files\NVIDIA Corporation\NVSMI\nvidia-smi.exe" --query-gpu=memory.total --format=csv,noheader,nounits -i $1`