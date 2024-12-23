import re
from pyrogram import Client, filters
import requests
import json
import random
import time

class GenCard:
    extra = ""
    mm = 0
    yy = 0
    cvv = ""

    def gen(cls, extra, mm='', yy='', cvv='', amo=10):
        cls.extra = extra
        cls.mm = int(mm) if mm else 0
        cls.yy = int(str(yy)[-2:]) if yy else 0
        cls.cvv = ''.join(filter(str.isdigit, cvv))

        if amo < 1 or amo > 100:
            amo = 10

        cards = []
        gcards = []

        for _ in range(amo):
            card = cls._gen_card()
            if card[0] in gcards:
                continue
            gcards.append(card[0])
            cards.append('|'.join(card))

        return cards

    def _gen_card(cls):
        return [cls._gen_cc(), cls._gen_mm(), cls._gen_yy(), cls._gen_cvv()]

    def _gen_cc(cls):
        num = 16
        if cls.extra.startswith("37"):
            num = 15
        
        ccbin = ''.join(filter(str.isdigit, cls.extra[:num]))

        # Replace 'x' with a random digit
        for i in range(len(ccbin)):
            if ccbin[i] == 'x':
                ccbin = ccbin[:i] + str(random.randint(0, 9)) + ccbin[i+1:]

        num += 1
        return cls._gen_num(ccbin, num)

    def _gen_num(cls, prefix, length):
        ccnumber = prefix

        while len(ccnumber) < (length - 1):
            ccnumber += str(random.randint(0, 9))

        sum_ = 0
        pos = 0
        reversed_ccnumber = ccnumber[::-1]

        while pos < length - 1:
            odd = int(reversed_ccnumber[pos]) * 2
            if odd > 9:
                odd -= 9

            sum_ += odd

            if pos != (length - 2):
                sum_ += int(reversed_ccnumber[pos + 1])

            pos += 2

        checkdigit = (10 - (sum_ % 10)) % 10
        ccnumber += str(checkdigit)

        return ccnumber

    def _gen_mm(cls):
        return str(cls.mm if 1 <= cls.mm <= 12 else random.randint(1, 12)).zfill(2)

    def _gen_yy(cls):
        now_yy = datetime.datetime.now().year % 100
        future_yy = now_yy + 10
        year = cls.yy if (cls.yy >= now_yy and cls.yy <= future_yy) else random.randint(now_yy, future_yy)
        return str(year).zfill(4)

    def _gen_cvv(cls):
        if cls.extra.startswith("37"):
            return str(random.randint(112, 998)).zfill(3)
        else:
            return str(random.randint(1102, 9998)).zfill(4) if not cls.cvv else cls.cvv.zfill(4)


# Example of how to use the GenCard class

# Parameters: extra, mm, yy, cvv, amount

class Bot:
    def __init__(self, proxy=None):
        self.proxy = proxy  # Store proxy settings if needed

    def bin_look_up(self, bin):
        bin = bin[:8]  # Truncate to 8 digits

        try:
            # Use the requests library to mimic the cURL call in PHP
            response = requests.get(f"https://lookup.binlist.net/{bin}", proxies=self.proxy)
            response.raise_for_status()  # raise an exception for HTTP errors
            decode_api = response.json()
            success = True
        except (requests.RequestException, json.JSONDecodeError) as e:
            success = False
            decode_api = {}

        return {
            "success": success,
            "scheme": decode_api.get("scheme", "N/A").upper(),
            "type": decode_api.get("type", "N/A").upper(),
            "brand": decode_api.get("brand", "N/A").upper(),
            "bank": decode_api.get("bank", {}).get("name", "N/A"),
            "country": decode_api.get("country", {}).get("name", "N/A"),
            "emoji": decode_api.get("country", {}).get("emoji", "🏳")
        }


    def is_banned_bin(self, bin):
        if not isinstance(bin, str):
            return False

        bin = bin[:6]  # Truncate to 6 digits

        # Read banned bins from a text file
        try:
            with open('banned_bins.txt', 'r') as file:
                banned_bins = file.read().splitlines()
            return bin in banned_bins
        except FileNotFoundError:
            return False  # If the file does not exist, return False
            
bot = Bot(proxy={"http": "http://101.51.54.236:8080", "https": "https://143.198.206.72:8888"})

from plugins.func.users_sql import *
@Client.on_message(filters.command ('gen'))
async def generate_card(Client, message):
    # Assume message.text contains the relevant data from the user
    data = message.text.split(maxsplit=1)
    command_data = data[1] if len(data) > 1 else ""

    if not command_data:
        await message.reply("Error: Enter data for card generation.")
        return

    # Sanitize and normalize input data
    data = re.sub(r'[^\dx ]', '\n', command_data.lower())
    data = re.sub(r'\n+', '\n', data)
    split = data.split()

    # Initialize variables
    extra, mm, yy, cvv, amo = None, None, None, None, 10
    digits = re.findall(r'[\dx]+', data)

    if not digits:  # No digits found
        await message.reply("Error: Invalid input data.")
        return

    extra_found = False

    for digit in digits:
        if re.match(r'^[3456]\d{4}[\dx]+', digit):
            extra = digit[:16]
            extra_found = True
            mm, yy, cvv = None, None, None # Reset values for new card
        elif extra_found:
            if not mm and re.match(r'^([1-9]|0[1-9]|1[012])$', digit):
                mm = digit
            elif not yy and re.match(r'^(20(2[2-9]|3[0-5])|(2[2-9]|3[0-5]))$', digit):
                yy = digit
            elif not mm and not yy:
                match = re.match(r'(\d{1,2})(20(2[2-9]|3[0-5])|(2[2-9]|3[0-5]))$', digit)
                if match:
                    mm = match.group(1)
                    yy = match.group(2)
            elif not cvv and re.match(r'^\d{3,4}$', digit):
                cvv = digit
            else:
                amo = digit  # Last number assumed to be amount

        # Stop searching once we got all necessary data
        if extra_found and mm and yy and cvv:
            break

    if not extra or len(extra) < 6:
        await message.reply("Error: Enter at least six digits for the Bin or extra number.")
        return

    # Check for length based on BIN
    card_length = 16 if extra.startswith("37") else 15
    if len(extra) != card_length:
        await message.reply("Error: Invalid card number length. Try another Bin or extra.")
        return

    # Default values for optional parameters
    mm = mm if mm is not None else 'rnd'
    yy = yy if yy is not None else 'rnd'
    cvv = cvv if cvv is not None else 'rnd'
    amo = int(amo) if amo > 10 else 10
    
    gcc = GenCard()
    cards = gcc.gen(extra, mm, yy, cvv, amo)  # Assuming this method exists in your generator object

    # Prepare response message
    msg = f"[⚙] <b>Format</b> → <code>{extra}|{mm}|{yy}|{cvv} {amo}</code>\n"
    msg += f"[🎰] <b>Amount</b> → <code>{len(cards)}</code>\n\n"

    for card in cards:
        msg += f"<code>{card}</code>\n"

    # BIN Lookup
    bin_info = await bot.binLookUp(extra[:6])  # Assuming this is an async method
    banned = "True ❌" if await bot.isBannedBin(extra[:6]) else "False ✅"

    msg += (f"\n[📟] <b>Bin</b> ↯ (<code>{extra[:6]}</code>) <code>{bin_info['scheme']}</code> - "
            f"<code>{bin_info['type']}</code> - <code>{bin_info['brand']}</code>\n"
            f"[🏦] <b>Bank</b> ↯ <i>{bin_info['bank']}</i>\n"
            f"[🗺] <b>Country</b> ↯ <i>{bin_info['country']}</i> [<code>{bin_info['emoji']}</code>]\n"
            f"[⛔] <b>Banned</b> ↯ <i>{banned}</i>")

    await message.reply(msg)

if __name__ == "__main__":
    Client.run()