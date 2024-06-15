import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "27612834")  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "28d176c899b65da009467232171d60f9") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7190767292:AAGJ1pvLg1L3o7VNk_Lb3h1MryvtTSmlPSs") # ⚠️ Required
    FORCE_SUB = os.environ.get('FORCE_SUB', '5574593875 1119579816 1735152469 6427494689 6610700592') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None
   
    # database config
    DB_URL  = os.environ.get("DB_URL", "mongodb+srv://animebash32:animebash3222@cluster0.tcey822.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")  # ⚠️ Required
    DB_NAME  = os.environ.get("DB_NAME","epicdatabase") 

    # Other Configs 
    ADMIN = int(os.environ.get("ADMIN", "")) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get('LOG_CHANNEL', '-1002185866235')) # ⚠️ Required
    BOT_UPTIME = BOT_UPTIME  = time.time()
    START_PIC = os.environ.get("START_PIC", "https://graph.org/file/15e82d7e665eccc8bd9c5.jpg")

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))


    caption = """
**File Name**: {0}

**Original File Size:** {1}
**Encoded File Size:** {2}
**Compression Percentage:** {3}

__Downloaded in {4}__
__Encoded in {5}__
__Uploaded in {6}__
"""
