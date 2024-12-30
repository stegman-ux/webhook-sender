import requests
import colorama
from colorama import Fore
import clear
webhook = input(Fore.YELLOW+"[<]entrée l'url du webhook : ")
message = input(Fore.YELLOW+"[<]entrée le message a envoyer : ")
message_to_send = {
    "content":f"{message}"
}
webhook_url = f"{webhook}"
requests.post(webhook_url,json=message_to_send)
clear.clear()
input(Fore.YELLOW+f"[<]le message '{message}' à bien etais envoyer au webhook...")

# script nul a chier mais j'mets quand meme des crédits mwawawa
# créator : intrable
# serveur discord : .gg/freeforreal