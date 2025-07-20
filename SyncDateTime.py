import requests
import subprocess

x = requests.get('https://www.timeapi.io/api/time/current/zone?timeZone=Australia%2FBrisbane')

data = x.json()

formatted = f"{data['year']}-{data['month']}-{data['day']} {data['hour']}:{data['minute']}:{data['seconds']}"

cmd = f'date -s "{formatted}"'
print(cmd)
subprocess.run(['sudo', 'bash', '-c', cmd])
