# bot.py
import json
import os
import random
import asyncio
from datetime import datetime, timedelta, time, timezone
import math
import pymongo
from pymongo import MongoClient
from pprint import pprint
import requests

import nextcord
from nextcord import SelectOption, ButtonStyle
from nextcord.ext import tasks, commands
from nextcord.interactions import Interaction, InteractionResponse
from nextcord.ui import button, View, Button, Select, TextInput, Modal

from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
USER = os.getenv('USER')
PWD = os.getenv('PWD')

STOCKS_API_KEY = os.getenv("YAHOO_API_KEY")

# pping:
PP_START = time(20, 00, 00)
PP_END = time(22, 00, 00)

# currency symbols:
token_symbol = "<:ethanger:763411726741143572>"
coin_symbol = "<:ethoggers:868201785301561394>"

guild = None
intents = nextcord.Intents.all()
intents.members = True
prefix = "eb!"

client = MongoClient(f"mongodb+srv://{USER}:{PWD}@ethanbotdb.jiyrt.mongodb.net/EthanBotDB")
db=client.bot_data

ethan_tokens = db.ethan_tokens
user_stocks = db.user_stocks
general_info = db.general_info
stock_info = db.stock_info

# rant toggles
# REMEMBER THIS IS ON U TURN IT OFF WHEN IT RESETS
VIRAJ = False
SAM = False

class Listeners(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        for guild in bot.guilds:
            if guild.name == GUILD:
                break
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name} (id: {guild.id})\n'
        )
    
    @commands.Cog.listener()
    async def on_message(self, message):
        global SAM
        global VIRAJ

        num = random.randint(1, 200)
        if num == 69:
            guild = message.author.guild
            role = guild.get_role(829155593322364959)
            role_members = role.members
            if message.author not in role_members and message.author.id == 501505695091392527:
                await message.channel.send(f"{message.author.mention} YOU SHOULD PLAY OSU")
        if (message.content[:5].strip() == prefix):
            return
        if (bot.user.id != message.author.id):                
            msg = message.content.strip().lower()
            choices_all = ["runfunc", "no sex", "ethan!", "ethan lee!", "my king!", "love ethan lee", "ETHAN LEE!!!!!", ":hot_face:", "STAN ETHAN LEE!", "vote ethan gang", "ethan lee best boy", "ETHAN sdo[f-dsfpasfkhsalduhfluashdf uaudfsa", "wouhaoguhaeg"]
            choices_ngan = ["sex", "sex??", "sex!"]
            if 'ethan' in msg and message.channel.id != 765710257753948190:
                if message.author.id == 597628340203028485:
                    await message.channel.send(random.choice(choices_ngan))
                else:
                    choice = random.choice(choices_all)
                    if (choice == "runfunc"):
                        string = "ethan"
                        for x in string:
                            await message.channel.send(f"GIVE ME A {x.capitalize()},")
                            await asyncio.sleep(0.7)
                        await message.channel.send(f"ETHAN LEE, ETHAN LEE!")
                        return
                    x = random.randint(1, 200)
                    if (x == 69):
                        for x in range(24):        
                            choice = random.choice(choices_all)            
                            if (choice == "runfunc"):
                                string = "ethan"
                                for x in string:
                                    await message.channel.send(f"GIVE ME A {x.capitalize()},")
                                    await asyncio.sleep(0.7)
                                await message.channel.send(f"ETHAN LEE, ETHAN LEE!")
                                continue
                            await message.channel.send(choice)
                    await message.channel.send(choice)
            if 'connor' in msg:
                await message.channel.send("ethan sex")
            if 'edge' in msg and 'play' in msg:
                await message.channel.send("ethedge ethplay ethgasm")
            if 'higgy' in msg:
                await message.channel.send("ethan be gettin' real jiggy")
            if 'sam' in msg and ('sister' in msg or 'your mom' in msg):
                await message.channel.send("<:sexualrelations:803707185963991081>")
                await message.channel.send("https://imgur.com/a/WsImVVj")
            if msg == 'ethan\'s insane announcement' and (message.channel.id == 765710257753948190):
                await message.channel.send("ethan's insane announcement")
            if 'china' in msg:
                await message.channel.send("荣耀归于中国")
            if 'egg' in msg:
                await message.channel.send("egg")
            if 'penis' in msg:
                await message.channel.send("lol penis")
            if 'sex' in msg:
                await message.channel.send("sex ( ͡° ͜ʖ ͡°)")
            if ':say_that_again:' in msg:
                await message.channel.send("me and daniel when we see that ethan is naked")
            if 'cock' in msg:
                await message.channel.send("https://imgur.com/d7X724S")
            if 'knowledge' in msg:
                await message.channel.send("https://www.youtube.com/watch?v=Cv1RJTHf5fk")
            if 'boris' in msg:
                await message.channel.send("BORIS JOHNSON")
            if 'johnson' in msg:
                await message.channel.send("JOHNSON? BORIS JOHNSON???")
            if 'putin' in message.content.lower():
                await message.channel.send("Putin.")
                await asyncio.sleep(1)
                await message.channel.send("Putin....")
                await asyncio.sleep(1)
                await message.channel.send("PUTIN DEEZ NUTS IN YOUR MOUTH")
            if 'kenneth' in msg:
                await message.channel.send("shit")
            if "nou" in message.content.lower().replace(" ", "") and "enough" not in message.content.lower().replace(" ", "") and message.channel.id != 765710257753948190:
                await message.channel.send("https://i.pinimg.com/originals/d5/8b/67/d58b67b83ffff03e8fd15583c91017fb.png")
                await message.channel.send("**NO U LMAO**")
            if "equality" in msg:
                await message.channel.send("Kenny Calls Commie-nism")
            if "communism works" in msg:
                await message.channel.send("Communism works, just ignore the concen....")
                await asyncio.sleep(2)
                await message.channel.send("Wait... who is that?")
                await asyncio.sleep(2)
                await message.channel.send("OH FUCK LUKE NO GET AWAY FROM ME")
                await asyncio.sleep(1)
                await message.channel.send("no what are you doing with that knife")
                await asyncio.sleep(3)
                await message.channel.send("OKAY COMMUNISM WORKS COMMUNISM WORKS ITS THE BEST GOVERNMENT SYSTEM THAT HAS EVER BEEN INVENTED")
            if "died" in msg:
                await asyncio.sleep(10)
                times = random.randint(1, 500)
                await message.channel.send("EGG " * times)
            if "issue" in msg:
                await message.channel.send("lmao skill issue")
            if "second amendment" in msg:
                await message.channel.send("Own a musket for home defense, since that's what the founding fathers intended. Four ruffians break into my house. \"What the devil?\" As I grab my powdered wig and Kentucky rifle. Blow a golf ball sized hole through the first man, he's dead on the spot. Draw my pistol on the second man, miss him entirely because it's smoothbore and nails the neighbors dog. I have to resort to the cannon mounted at the top of the stairs loaded with grape shot, \"Tally ho lads\" the grape shot shreds two men in the blast, the sound and extra shrapnel set off car alarms. Fix bayonet and charge the last terrified rapscallion.He Bleeds out waiting on the police to arrive since triangular bayonet wounds are impossible to stitch up, Just as the founding fathers intended")
            if "fail" in msg:
                await message.channel.send("https://imgur.com/315P6Fs")
            if "based" in msg:
                await message.channel.send("**BASED AF**")
                await message.channel.send("https://imgur.com/a/NvSoP4P")
            if "slave" in msg or "incest" in msg or "secession" in msg:
                await message.channel.send("https://imgur.com/a/jHxef46")
        if (message.author.id == 292448459909365760):
            if 'sad' in message.content.strip().lower():
                await message.channel.send("<:zzwhoops_cries:813585484441714698>")
        if (message.author.id == 390601966423900162):
            if 'scribbles notes' in message.content.lower():
                await message.channel.send("https://tenor.com/bi7Db.gif")
            msg = message.content.lower().replace(" ", "")
            if ("invisible hand" in msg):
                await message.channel.send("Aw fuck you ethan you're not the invisible hand you're a bitch")
            if ("whim" in msg):
                await message.channel.send("I'll invert your asshole on a whim dipshit")
            # viraj is about to start ranting and ethan would like to stop him
            if "radical" in msg:
                VIRAJ = not VIRAJimage.png
                print(f"VIRAJ: {VIRAJ}")
            # sam is about to start saying something stupid and ethan would like to stop him
            if "boner" in msg:
                SAM = not SAM
                print(f"SAM: {SAM}")
        if (message.author.id == 501505695091392527):
            if (SAM):
                chance = random.randint(1, 100)
                if (chance <= 15):
                    await message.channel.send("https://tenor.com/view/who-asked-gif-21634393")
            if 'sister' in message.content:
                await message.channel.send("<:sexualrelations:803707185963991081>")
            if (message.channel.id == 537757338300317739):
                if 'parsfuk' in message.content.lower().replace(" ", ""):
                    for x in range(7):
                        await message.channel.send("https://tenor.com/bMkPz.gif")
                    embed = nextcord.Embed(title="No, Sam, #parsfuk **WILL NOT** be ***FUCKING LIBERATED***", description="__***DENIED***__")
                    await message.channel.send(embed=embed)
            if "fight" in message.content.lower().replace(" ", "") and "continue" in message.content.lower().replace(" ", ""):
                embed = nextcord.Embed(title="*Not after I'm done with you*...")
                await message.channel.send(embed=embed)
                await asyncio.sleep(2)
                await message.channel.send(f"**Acquiring location of user {message.author.mention}...**")
                await asyncio.sleep(5)
                await message.channel.send("**Location found!**")
                await asyncio.sleep(1)
                await message.channel.send("https://www.google.com/maps/place/56+Leigh+Ave,+Princeton,+NJ+08540/")
            if "xd" in message.content.lower().replace(" ", "") or "haha" in message.content.lower().replace(" ", ""):
                embed = nextcord.Embed(title="Aw fuck you sam go suck a lemon", description="STFU or im taking away your ethan tokens")
                await message.channel.send(embed=embed)
        if (message.author.id == 712420717685112863):
            if (VIRAJ):
                chance = random.randint(1, 100)
                if (chance <= 15):
                    await message.channel.send("https://tenor.com/view/who-asked-gif-21634393")

class Ethan(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ethelp")
    async def ethan_help(self, ctx):
        if (ctx.author.id != 390601966423900162 and ctx.author.id != 292448459909365760):
            await ctx.channel.send("Only Ethan can use this dumbass")
            return

        embed = nextcord.Embed(title="**Fun:**", description=f"**Viraj**: {VIRAJ}\n**Sam**: {SAM}")
        await ctx.author.send(embed=embed)

    @commands.command(name="set")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def set_balance(self, ctx, currency, member: nextcord.Member, amount):
        economy = self.bot.get_cog('Economy')
        amount = round(float(str(amount).replace(",","")), 2)
        symbol = await economy.get_symbol(currency)
        types = ["tokens", "coins"]

        if (ctx.author.id != 390601966423900162):
            await ctx.channel.send("Only Ethan can use this dumbass")
            self.set_balance.reset_cooldown(ctx)
            return
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try! Type 'coins' or 'tokens'.")
            self.set_balance.reset_cooldown(ctx)
            return

        id = member.id
        existing = ethan_tokens.find_one({"id": id})
        if existing == None:
            await economy.create_token_account(ctx, member)
            if (currency == "tokens"):
                data["tokens"] = amount
            if (currency == "coins"):
                data["coins"] = amount
            ethan_tokens.insert_one(data)        
            await ctx.channel.send(f"Okay, {member.mention} now has **{amount:,.2f}** {symbol}.")
        else:
            query = {
                "id": id
            }
            if (currency == "tokens"):
                new_balance = amount
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "tokens": new_balance
                    }
                }
                ethan_tokens.update_one(query, data)
            if (currency == "coins"):
                new_balance = amount
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "coins": new_balance
                    }
                }
                ethan_tokens.update_one(query, data)

            await ctx.channel.send(f"Okay, {member.mention} now has **{amount:,.2f}** {symbol}.")

    @commands.command(name="edit", aliases=["add"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def edit_balance(self, ctx, currency, member: nextcord.Member, amount):
        economy = self.bot.get_cog('Economy')
        amount = round(float(str(amount).replace(",","")), 2)
        symbol = await economy.get_symbol(currency)
        types = ["tokens", "coins"]

        if (ctx.author.id != 390601966423900162):
            await ctx.channel.send("Only Ethan can use this dumbass")
            self.edit_balance.reset_cooldown(ctx)
            return
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try! Type 'coins' or 'tokens'.")
            self.edit_balance.reset_cooldown(ctx)
            return

        id = member.id
        existing = ethan_tokens.find_one({"id": id})
        if existing == None:
            await economy.create_token_account(ctx, member)
            if (currency == "tokens"):
                data["tokens"] = amount
            if (currency == "coins"):
                data["coins"] = amount
            ethan_tokens.insert_one(data)        
            await ctx.channel.send(f"Okay, {member.mention} now has **{amount:,.2f}** {symbol}")
        else:
            query = {
                "id": id
            }
            if (currency == "tokens"):
                cur_balance = existing["tokens"]
                new_balance = cur_balance + amount
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "tokens": new_balance
                    }
                }
                ethan_tokens.update_one(query, data)
            if (currency == "coins"):
                cur_balance = existing["coins"]
                new_balance = cur_balance + amount
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "coins": new_balance
                    }
                }
                ethan_tokens.update_one(query, data)

            if (amount < 0):
                await ctx.channel.send(f"Okay, I've taken **{amount:,.2f}** {symbol} from {member.mention}.\nThey now have **{new_balance:,.2f}** {symbol}.")
            else:
                await ctx.channel.send(f"Okay, I've added **{amount:,.2f}** {symbol} to {member.mention}.\nThey now have **{new_balance:,.2f}** {symbol}.")

    @commands.command(name="editall", aliases=["addall"])
    @commands.cooldown(1, 5)
    async def edit_all_balances(self, ctx, currency, amount):
        economy = self.bot.get_cog('Economy')
        amount = round(float(str(amount).replace(",","")), 2)
        types = ["tokens", "coins"]
        symbol = await economy.get_symbol(currency)

        if (ctx.author.id != 390601966423900162):
            await ctx.channel.send("Stop trying to be Ethan")
            self.edit_all_balances.reset_cooldown(ctx)
            return
        if (currency == ""):
            await ctx.channel.send("Well pick a currency to add to.")
            self.edit_all_balances.reset_cooldown(ctx)
            return
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try!")
            self.edit_all_balances.reset_cooldown(ctx)
            return
        if (amount == 0.0):
            await ctx.channel.send("You're a dumb dumb, dumb dumb")
            self.edit_all_balances.reset_cooldown(ctx)
            return
            
        # increment all currency values by amount
        data = {
            "$inc":
            {
                currency: amount
            }
        }
        ethan_tokens.update_many(filter={}, update=data)
        count = ethan_tokens.count_documents(filter={})

        await ctx.channel.send(f"Okay, I've added **{amount}**{symbol} to **{count}** users. Please be careful Ethan")

    @commands.command(name="HYPERINFLATION", aliases=["inflate"])
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def hyperinflation(self, ctx, currency = "", multi = 0.0):
        economy = self.bot.get_cog('Economy')
        types = ["tokens", "coins"]
        symbol = await economy.get_symbol(currency)

        if (ctx.author.id != 390601966423900162):
            await ctx.channel.send("Only Ethan can cause hyperinflation!")
            self.hyperinflation.reset_cooldown(ctx)
            return
        if (currency == ""):
            await ctx.channel.send("Well pick a currency to inflate, idiot")
            self.hyperinflation.reset_cooldown(ctx)
            return
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try!")
            self.hyperinflation.reset_cooldown(ctx)
            return
        if (multi <= 0.0):
            await ctx.channel.send("Canceling EthanCurrency, are you? Enter a number above 0 dumbass")
            self.hyperinflation.reset_cooldown(ctx)
            return
        elif (multi == 1.0):
            await ctx.channel.send("I mean, okay, sure, but you do realize this changes jackshit right")
            self.hyperinflation.reset_cooldown(ctx)
            return
        """
        elif (multi > 1.1):
            await ctx.channel.send("I have removed the limit!")
            await asyncio.sleep(20)
            await ctx.channel.send("AND REPLACED IT WITH 1.1X LMAO GET FUCKED")
            self.hyperinflation.reset_cooldown(ctx)
            return
        """

        data = {
            "$mul":
            {
                currency: multi
            }
        }
        ethan_tokens.update_many(filter={currency:{"$not":{"$eq":0}}}, update=data)

        query = {
            "type": "currency"
        }
        cur_rate = general_info.find_one(query)[f"{currency}_rate"]
        new_rate = cur_rate * multi
        # using f-string to select either "coins_rate" or "tokens_rate"
        data = {
            "$set": {
                f"{currency}_rate": new_rate
            }
        }
        general_info.update_one(query, data)

        await ctx.channel.send(f"Okay, I've inflated {symbol} by {multi}.\nYour inflation rate is now **{new_rate:,.3f}**x.\nI hope you know what you're doing...")

    @commands.command(name="MURDERINFLATIONWITHARUSTYFUCKINGKNIFE")
    @commands.has_permissions(administrator=True)
    async def murder(self, ctx):
        murder = 0.001
        image="https://cms.qz.com/wp-content/uploads/2016/12/demon.jpg?quality=75&strip=all&w=1600&h=900&crop=1"
        data = {
            "$mul":
            {
                "tokens": murder
            }
        }
        ethan_tokens.update_many(filter={"tokens":{"$not":{"$eq":0}}}, update=data)
        query = {
            "type": "currency"
        }
        cur_rate = general_info.find_one(query)["tokens_rate"]
        new_rate = cur_rate * murder
        data = {
            "$set": {
                "tokens_rate": new_rate
            }
        }
        general_info.update_one(query, data)
        await ctx.channel.send(image)

class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def create_token_account(self, ctx, member=None):
        if (member == None):
            member = ctx.author
        tokens = 0.00
        coins = 0.00
        await ctx.channel.send(f"Records not found... creating account for {member.mention}.")
        data = {
            "id": member.id,
            "name": f"{member.name}#{member.discriminator}",
            "tokens": tokens,
            "coins": coins
        }
        print(data)
        await asyncio.sleep(1)
        await ctx.channel.send(f"Account created!")
        ethan_tokens.insert_one(data)

    async def get_symbol(self, currency):
        if currency == "tokens":
            return("<:ethanger:763411726741143572>")
        elif currency == "coins":
            return("<:ethoggers:868201785301561394>")

    @commands.command(name="balance", aliases=["bal"])
    async def view_balance(self, ctx, member: nextcord.Member = None):
        if member is None:
            member = ctx.author
        
        id = member.id
        existing = ethan_tokens.find_one({"id": id})
        tokens = 0.00
        coins = 0.00
        if existing == None:
            await self.create_token_account(ctx)
        else:
            tokens = f"{existing['tokens']:,.2f}"
            coins = f"{existing['coins']:,.2f}"

        embed = nextcord.Embed(title=f"{member.name}'s EthanBalance:tm:")
        embed.add_field(name="<:ethanger:763411726741143572> (ET)", value=tokens, inline=True)        
        embed.add_field(name="<:ethoggers:868201785301561394> (EC)", value=coins, inline=True)
        await ctx.channel.send(embed=embed)

    @commands.command(name="pay", aliases=["donate", "give"])
    async def pay(self, ctx, currency, receiver: nextcord.Member = None, amount = ""):
        giver = ctx.author
        types = ["tokens", "coins"]
        symbol = await self.get_symbol(currency)

        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try! Type 'coins' or 'tokens'.")
            return
        if (receiver == None):
            await ctx.channel.send("Who you payin', yourself? That ain't how it works.")
            return

        giver_existing = ethan_tokens.find_one({"id": giver.id})
        giver_balance = giver_existing[currency]
        try:
            amount = float(amount)
        except ValueError:
            if (amount == "all"):
                amount = giver_balance
            else:
                await ctx.channel.send(f"How the fuck am I supposed to give {receiver.display_name} {amount}{symbol}?")
                return
        if (float(amount) <= 0.0):
            await ctx.channel.send("Hey you gotta *pay* the person a positive number that isn't 0 bitch")
            return
            
        receiver_existing = ethan_tokens.find_one({"id": receiver.id})
        if (giver_existing == None):
            await ctx.channel.send(f"You need an account and to like... not be broke to pay someone lmao. Try {prefix}bal to create one.")
            return
        if (receiver_existing == None):
            await self.create_token_account(ctx, receiver)
            receiver_existing = ethan_tokens.find_one({"id": receiver.id})
        
        if (amount == "all"):
            amount = giver_balance
        receiver_balance = receiver_existing[currency]
        new_giver_balance = giver_balance - amount
        new_receiver_balance = receiver_balance + amount

        if (new_giver_balance < 0):
            await ctx.channel.send(f"You can't give that much, ha poor")
            return

        give_data = {
            "$set": {
                currency: new_giver_balance
            }
        }
        receive_data = {
            "$set": {
                currency: new_receiver_balance
            }
        }
        ethan_tokens.update_one({"id": giver.id}, give_data)
        ethan_tokens.update_one({"id": receiver.id}, receive_data)

        # maybe replace with another database call to make sure everything is consistent?
        await ctx.channel.send(f"You gave **{amount:,.2f}**{symbol} to {receiver.mention}.\nYour balance: **{new_giver_balance:,.2f}**{symbol}\nTheir balance: **{new_receiver_balance:,.2f}{symbol}**")

    @commands.command(name="circulation", aliases=['circ', 'total', 'all'])
    async def total_wealth(self, ctx):
        agg = ethan_tokens.aggregate([{
            "$group": {
                "_id": 1,
                "tokens": {"$sum": "$tokens"},
                "coins": {"$sum": "$coins"},
                "count": {"$sum": 1}
            }
        }])

        total_value = list(agg)[0]
        db_count = total_value['count']
        tokens = total_value['tokens']
        coins = total_value['coins']
        avg_tokens = tokens / db_count
        avg_coins = coins / db_count

        description = f"**Members in database: __{db_count}__**\n\n**Tokens:** `{tokens:,.2f}`{token_symbol}\n**Average:** `{avg_tokens:,.2f}`{token_symbol}\n\n**Coins:** `{coins:,.2f}`{coin_symbol}\n**Average:** `{avg_coins:,.2f}`{coin_symbol}"
        embed = nextcord.Embed(title=f"__{ctx.guild.name}'s Server Worth__", description=description)
        await ctx.channel.send(embed=embed)
        
    @commands.command(name="leaderboard", aliases=["top", "rich"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def leaderboard(self, ctx, currency = ""):
        member = ctx.author
        types = ["tokens", "coins"]
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try! Type 'coins' or 'tokens'.")
            self.leaderboard.reset_cooldown(ctx)
            return
        
        description = ""
        count = 0
        if currency == "tokens":
            accounts = ethan_tokens.find().sort("tokens", pymongo.DESCENDING).limit(7)
            for account in accounts:
                if (account['name'] == f"{member.name}#{member.discriminator}"):
                    is_user = "***"
                else:
                    is_user = ""
                if (account['tokens'] == 0):
                    break
                count += 1
                description += f"**#{count}**: `{account['tokens']:,.2f}`<:ethanger:763411726741143572> - {is_user}{account['name']}{is_user}\n"
        elif currency == "coins":
            accounts = ethan_tokens.find().sort("coins", pymongo.DESCENDING).limit(7)
            for account in accounts:
                if (account['name'] == f"{member.name}#{member.discriminator}"):
                    is_user = "***"
                else:
                    is_user = ""
                if (account['coins'] == 0):
                    break
                count += 1
                description += f"**#{count}**: `{account['coins']:,.2f}`<:ethoggers:868201785301561394> - {is_user}{account['name']}{is_user}\n"

        embed = nextcord.Embed(title=f"{ctx.guild.name}'s {currency.capitalize()} Leaderboard", description=description)
        await ctx.channel.send(embed=embed)

    @commands.command(name="inflation", aliases=["rates"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def get_rate(self, ctx):
        query = {
            "type": "currency"
        }
        rates = general_info.find_one(query)
        coins_rate = rates["coins_rate"]
        tokens_rate = rates["tokens_rate"]
        coins_symbol = await self.get_symbol("coins")
        tokens_symbol = await self.get_symbol("tokens")
        embed = nextcord.Embed(title=f"__{ctx.guild}'s Inflation Rates:__", description=f"{tokens_symbol}: **{tokens_rate:,.3f}x**\n{coins_symbol}: **{coins_rate:,.3f}x**")
        await ctx.channel.send(embed=embed)

    @commands.command(name="ETHANEDGEPLAY", aliases=["ELEP", "EEP", "EDGEPLAY"])
    @commands.cooldown(1, 45, commands.BucketType.guild)
    async def eth_edge(self, ctx, success="100"):
        try:
            success = int(success)
        except ValueError:
            await ctx.channel.send("Bro you gotta give me an integer")
            return
        time = 30
        rates = general_info.find_one({"type": "currency"})
        tokens_rate = rates["tokens_rate"]
        coins_rate = rates["coins_rate"]

        limit = 1000
        if (success <= 0):
            await ctx.channel.send(f"Enter a number between 1 and {limit}, dumbass. Victory doesn't come *that* easy.")
            self.eth_edge.reset_cooldown(ctx)
            return
        elif (success >= limit):
            await ctx.channel.send(f"I will leak my OnlyFans if you somehow get over {limit}. Pick another number!")
            self.eth_edge.reset_cooldown(ctx)
            return

        async def calculate_tokens(users, messages, target, inflation):
            user_score = math.pow(users * 15, 1.2)
            message_score = math.pow(messages, 1.3) / 2
            bonus = random.randint(0, messages)
            multiplier = math.pow(target / 50, 0.4)
            total = (user_score + message_score + bonus) * multiplier
            inflation_total = total * inflation
            data = {
                "user_score": user_score,
                "message_score": message_score,
                "multiplier": multiplier,
                "bonus": bonus,
                "total": total,
                "inflation_total": round(inflation_total, 2)
            }
            return data

        async def calculate_coins(users, messages, target, inflation):
            msg_rate_user = (messages / users) / time

            rate_score = math.pow(msg_rate_user * 75, 0.9)
            multiplier = math.pow(target / 50, 0.4)
            total = rate_score * multiplier
            inflation_total = total * inflation
            data = {
                "msg_rate_user": msg_rate_user,
                "rate_score": rate_score,
                "multiplier": multiplier,
                "total": total,
                "inflation_total": round(inflation_total, 2)
            }
            return data

        async def counter(ctx):
            count = 0
            users = 0
            per_user_stats = {}

            first = datetime.now(timezone.utc)
            await asyncio.sleep(time)

            embed = nextcord.Embed(title="__**STOP**__", description="Tallying love for edge play...")
            await ctx.channel.send(embed=embed)
            await asyncio.sleep(1.5)

            now = datetime.now(timezone.utc)
            messages = await ctx.channel.history(limit=None, before=now, after=first).flatten()

            for msg in messages:
                if (msg.content != "ELEP"):
                    continue
                id = msg.author.id
                count += 1
                if (id not in per_user_stats):
                    per_user_stats[id] = 1
                elif (id in per_user_stats):
                    per_user_stats[id] = per_user_stats.get(id) + 1

            users = len(per_user_stats)
            user_earnings = ""
            if (int(count) >= int(success)):
                tokens = await calculate_tokens(users, count, success, tokens_rate)
                coins = await calculate_coins(users, count, success, coins_rate)
                for key, value in per_user_stats.items():
                    msg_percent = value / count
                    earned_tokens = msg_percent * tokens['inflation_total']
                    earned_coins = msg_percent * coins['inflation_total']
                    user = bot.get_user(key).name
                    query = {
                        "id": int(key)
                    }
                    data = {
                        "$inc":
                        {
                            "coins": earned_coins,
                            "tokens": earned_tokens
                        }
                    }
                    ethan_tokens.update_one(query, data)
                    user_earnings += f"**{user}**: **{value}** msgs (**{msg_percent * 100:.2f}**%) = **{earned_tokens:,.2f}**{token_symbol} + **{earned_coins:,.2f}**{coin_symbol}\n"
                description = f"Token Payout: **{tokens['inflation_total']:,.2f}**{token_symbol}\nCoin Payout: **{coins['inflation_total']:,.2f}**{coin_symbol}\n\n__**Breakdown:**__\nMessages: **{count}**/**{success}**\nUsers Participated: **{users}**\n\n__**User Earnings:**__\n{user_earnings}"
            else:
                tokens = 0
                coins = 0            
                for key, value in per_user_stats.items():
                    user = bot.get_user(key).name
                    msg_percent = value / count
                    user_earnings += f"**{user}**: **{value}** msgs (**{msg_percent * 100:.2f}**%)"
                description = f"Token Payout: **{tokens}**{token_symbol}\nCoin Payout: **{coins}**{coin_symbol}\n\n__**Breakdown:**__\nMessages: **{count}**/**{success}**\nUsers Participated: **{users}**\n\n__**User Earnings**__\n{user_earnings}"

            embed = nextcord.Embed(title="__**Results:**__", description=description)
            await ctx.channel.send(embed=embed)
            await asyncio.sleep(2)

            if (int(count) >= int(success)):
                await ctx.channel.send("https://ih1.redbubble.net/image.724682828.9041/flat,1000x1000,075,f.jpg")
            else:
                await ctx.channel.send("you tried lmao you suck\n**YOU SUCK SKILL ISSUE LMAO**")
                await ctx.channel.send("https://imgur.com/a/vlkjkxv")

            return ([count, users])

        async def record_check(ctx, stats):
            query = {
                "type": "records"
            }
            records = general_info.find_one(query)["EEP"]
            msgs = records["msgs"]
            users = records["users"]

            if (stats[0] > msgs):
                description = f"Original: **{msgs}** msgs, **{users}** users\nNew: **{stats[0]}** msgs, **{stats[1]}** users"
                embed = nextcord.Embed(title="**New Record!**", description=description)
                await ctx.channel.send(embed=embed)
            else:
                return

            data = {
                "$set":
                {
                    "EEP": {
                        "msgs": stats[0],
                        "users": stats[1]
                    }
                }
            }
            general_info.update_one(query, data)
            

        embed=nextcord.Embed(title="I LOVE EDGE PLAY. PREPARE TO SEND 'ELEP' FOR 30 SECONDS", description=f"Goal: {success}\n")
        await ctx.channel.send(embed=embed)
        
        delay = 3
        first = await ctx.channel.send(f"**READY**")
        for x in range(delay):
            await asyncio.sleep(1)
            await first.edit(f"**{str(delay - x)}**")

        await asyncio.sleep(1)
        await ctx.channel.send("**-=-=- GO -=-=-**")

        stats = await counter(ctx)
        await record_check(ctx, stats)

class BuyStocks(Select):
    options = []
    stocks = stock_info.find()
    tokens_rate = 0.0

    def __init__(self, tokens_rate):
        self.tokens_rate = tokens_rate

        for stock in self.stocks:
            name = stock['name']
            converted_price = stock['price'] * self.tokens_rate
            currency = stock['currency']
            if (currency == 'USX'):
                converted_price /= 100
            description = f"{converted_price:,.2f}/unit\n"
            self.options.append(SelectOption
                (
                    label = name,
                    description = description,
                    emoji = token_symbol
                )
            )
        super().__init__(
            placeholder = "Select a stock option!",
            options = self.options,
            row = 1
        )

    async def callback(self, interaction: Interaction):
        view: BuyStocksView = self.view
        view.continue_prompt = True
        view.stop()
        view.name = self.values[0]
        view.stock = stock_info.find_one({'name': view.name})
        view.symbol = view.stock['symbol']
        view.converted_price = view.stock['price'] * self.tokens_rate
        if (view.stock['currency'] == 'USX'):
            view.converted_price /= 100
        embed = nextcord.Embed(title = f"Buying **{view.name}**:", description = f"How many units would you like to purchase? (Type 'max' for basically your entire balance)\n(`{view.converted_price:,.2f}`{token_symbol}/unit)")
        await interaction.response.send_message(embed=embed)

class BuyStocksView(View):    
    name = ""
    stock = {}
    symbol = ""
    converted_price = 0.0
    continue_prompt = False

    def __init__(self, tokens_rate, timeout=30):
        self.tokens_rate = tokens_rate
        super().__init__(timeout=timeout)

        self.add_item(BuyStocks(tokens_rate))

    async def on_timeout(self):
        self.stop()

    async def on_error(self, interaction, select):
        await interaction.channel.send_message("lmao u suck")

class Stocks(commands.Cog):
    good_names = ["Crude Oil", "Gold", "Wheat", "Corn", "Ethanol"]
    symbols = "CL=F,GC=F,ZW=F,ZC=F,CU=F"
    base_rate = 12
    tokens_rate = base_rate

    def __init__(self, bot):
        self.bot = bot
        self.refresh_stocks.start()

    async def create_stock_account(self, ctx, member = None):
        if (member == None):
            member = ctx.author
        await ctx.channel.send(f"No stock account found for {member.mention}. Creating...")
        data = {
            "id": member.id,
            "name": f"{member.name}#{member.discriminator}",
            "stock_data": {}
        }
        print(data)
        await asyncio.sleep(1)
        await ctx.channel.send(f"Account created!")
        user_stocks.insert_one(data)        

    @commands.command(name="stocks", aliases=["stock", "stonk", "stonks"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def stocks(self, ctx, choice=""):
        async def update_rate():
            self.tokens_rate = self.base_rate * general_info.find_one({"type": "currency"})["tokens_rate"]

        async def view_stocks(ctx):
            await update_rate()

            stocks = stock_info.find()

            description = f"**Conversion Rate**: `{self.tokens_rate:,.2f}`{token_symbol}/USD\n\n"
            for stock in stocks:
                symbol = stock['symbol'].replace('=F', '')
                name = stock['name']
                price = stock['price']
                converted_price = price * self.tokens_rate
                currency = stock['currency']
                if (currency == 'USX'):
                    price /= 100
                description += f"({symbol}) **{name}**: `{converted_price:,.2f}`{token_symbol}/unit - ($`{price:,.2f}`)\n"

            query = {"type": "stocks"}
            last_update = general_info.find_one(query)['update_time']
            date_time = last_update.strftime("%m/%d/%Y %I:%M:%S %p")
            description += f"\n**Data last updated at:** {date_time}"
            
            embed = nextcord.Embed(title="Stonks", description=description)
            await ctx.channel.send(embed=embed)

        async def buy_stocks(ctx):
            economy = self.bot.get_cog('Economy')
            member = ctx.author

            query = {"id": ctx.author.id}
            user = ethan_tokens.find_one(query)
            if user == None:
                await economy.create_token_account(ctx, ctx.author)
            bal = user['tokens']

            view = BuyStocksView(self.tokens_rate)
            await ctx.channel.send("**BUYING STOCKS**", view=view)
            await view.wait()
            if (not view.continue_prompt):
                return

            def check(m):
                return (
                    m.author == member
                    and m.channel == ctx.channel
                )
            try:
                msg = await self.bot.wait_for (
                    "message",
                    timeout=15,
                    check=check
                )
                if msg:
                    # take floor to nearest millionth or whatever precision is set to
                    precision = 0.000001
                    if (msg.content.lower() == "max"):
                        amount = (bal / view.converted_price) // precision * precision
                    else:
                        try:
                            amount = float(msg.content)
                        except ValueError:
                            await ctx.channel.send(f"Hey dumbass you can't buy {msg.content} units of {view.name}")
                            return
            except asyncio.TimeoutError:
                await ctx.channel.send("Well give me a number, don't just stare at me like that you creep", delete_after=10)
                return

            total_price = amount * view.converted_price
            # return if the user doesn't have enough money.
            if (bal < total_price):
                await ctx.channel.send(f"lmao you don't have enough money fool, you need **{total_price:,.2f}**{token_symbol} to buy **{amount:,.3f}** units of {view.name}")
                return
            
            embed = nextcord.Embed(title=f"Buying **{view.name}** ({view.stock['symbol']})", description=f"**Total**: `{amount:,.3f}`u for **`{total_price:,.2f}`**{token_symbol} (`{view.converted_price:,.2f}`{token_symbol}/unit)")
            await ctx.channel.send(embed=embed)
            # create user stocks collection if it doesn't exist, populate with data
            query = {"id": member.id}
            cur_stocks = user_stocks.find_one(query)
            if (cur_stocks == None):
                await self.create_stock_account(ctx)
            data = {
"""
                "$set": {
                    "name": f"{member.name}#{member.discriminator}",
                    "stock_data": {
                        "name": view.name,
                        "symbol": view.stock['symbol'],
                        "amount":
                        "buy_price":
                        "buy_worth":
                    }
                }
"""
            }
            user_stocks.update_one(query, data)

        if (choice == ""):
            await ctx.channel.send("Bro you gotta tell me what you want to do,\nimagine if you went up to your teacher and\nasked hey, how do you stonks?\nDo you want to 'view', 'buy' or 'sell' your stocks?")
        if (choice == "view"):
            await view_stocks(ctx)
        if (choice == "buy"):
            await buy_stocks(ctx)

    @tasks.loop(hours=8)
    async def refresh_stocks(self):
        now = datetime.now()
        print("Refreshing stocks at " + str(now))
        query = {"type": "stocks"}
        data = {
            "$set": {
                "update_time": now
            }
        }
        general_info.find_one_and_update(query, data, upsert=True)

        url = "https://yfapi.net/v6/finance/quote"
        querystring = {"symbols": self.symbols}
        headers = {
            'x-api-key': STOCKS_API_KEY
            }
        response = requests.request("GET", url, headers=headers, params=querystring)

        try:
            formatted = response.json()['quoteResponse']['result']
            for good in formatted:
                symbol = good['symbol']
                name = good['shortName']
                currency = good['currency']
                price = round(good['regularMarketPrice'], 2)
                
                for good_name in self.good_names:
                    if (good_name in name):
                        name = good_name
                        break

                query = {
                    "symbol": symbol
                }
                data = {
                    "symbol": symbol,
                    "name": name,
                    "currency": currency,
                    "price": price
                }
                stock_info.find_one_and_replace(query, data, upsert=True)
        except KeyError as e:
            print(f"Thingy happened with stonks: {e.message}")
            return


    @refresh_stocks.before_loop
    async def before_refresh(self):
        # wait until X:00:00
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        start = datetime.combine((now + timedelta(hours=1)).date(), time((now + timedelta(hours=1)).time().hour, 0, 0)).replace(tzinfo=timezone.utc)
        wait_seconds = (start - now).total_seconds()
        print("Waiting " + str(wait_seconds) + " before starting refresh.")
        
        await asyncio.sleep(wait_seconds)

class Gambling(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="luckynumbers", aliases=["lnums", "ln", "luckynums"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lucky_numbers(self, ctx, currency = "", amount = ""):
        economy = self.bot.get_cog('Economy')
        types = ["tokens", "coins"]
        symbol = await economy.get_symbol(currency)
        
        if (currency not in types):
            await ctx.channel.send(f"Ethan{currency.capitalize()}:tm: doesn't exist. Nice try! Type 'coins' or 'tokens'.")
            self.lucky_numbers.reset_cooldown(ctx)
            return
        balance = ethan_tokens.find_one({"id": ctx.author.id})[currency]
        try:
            amount = float(amount)
        except ValueError:
            if (amount == "all"):
                amount = balance
            else:
                await ctx.channel.send(f"tf is {amount}{symbol}?")
                return
        if (amount <= 0.0):
            await ctx.channel.send(f"You have to gamble some amount of tokens or coins.\nBroke ass lil shit lmao")
            return
        
        if (balance < amount):
            await ctx.channel.send(f"You don't have that much money idiot")
            return
        await ctx.channel.send(f"Gambling **{amount:,.2f}**{symbol}. Choose a number from **1-10**! Type 'e' to exit.")

        def check(m):
            return (
                m.channel.id == ctx.channel.id
                and m.author.id == ctx.author.id
            )
        try:
            guess = await bot.wait_for("message", check=check, timeout=30.0)
            guess = guess.content
            if (guess.strip().lower() == "e"):
                await ctx.channel.send(f"lmao pussy :chicken:")
                return
            if not (int(guess) <= 10 and int(guess) >= 0):
                await ctx.channel.send(f"Enter a number between 1 and 10.")
                return

            number = random.randint(1, 10)
            difference = abs(int(number) - int(guess))

            await ctx.channel.send(f"The number was **{number}**. Your guess, **{guess}** was **{difference}** off.")

            if (difference == 0):
                percent = random.randint(175, 300)
                change = amount * (percent / 100)
                await ctx.channel.send("https://ih1.redbubble.net/image.724682828.9041/flat,1000x1000,075,f.jpg")
                await ctx.channel.send(f"Spot on! Congratulations, you've won **{(change - amount):,.2f}**{symbol} (**{amount:,.2f}** --> **{change:,.2f}**) *({(percent / 100):.2f}x)*.")
            elif (difference == 1):
                percent = random.randint(125, 165)
                change = amount * (percent / 100)
                await ctx.channel.send(f"I mean, you were pretty close. You get... a lil bit: **{(change - amount):,.2f}**{symbol} (**{amount:,.2f}** --> **{change:,.2f}**) *({(percent / 100):.2f}x)*.")
            elif (difference == 2 or difference == 3):
                percent = random.randint(30, 99)
                change = amount * (percent / 100)
                await ctx.channel.send(f"You weren't that close, so I'll just give you some of your money back: **{(change - amount):,.2f}**{symbol} (**{amount:,.2f}** --> **{change:,.2f}**) *({(percent / 100):.2f}x)*.")
            else:
                change = 0
                await ctx.channel.send("https://imgur.com/a/vlkjkxv")
                await ctx.channel.send(f"lmao you suck, I'll be taking **{amount:,.2f}**{symbol}")

            member = ctx.author
            new_balance = balance + (change - amount)
            if (currency == "tokens"):
                query = {
                    "id": member.id
                }
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "tokens": new_balance
                    }
                }
            elif (currency == "coins"):
                query = {
                    "id": member.id
                }
                data = {
                    "$set":
                    {
                        "name": f"{member.name}#{member.discriminator}",
                        "coins": new_balance
                    }
                }
            ethan_tokens.update_one(query, data)
                
            await asyncio.sleep(1)
            await ctx.channel.send(f"You now have **{new_balance:,.2f}**{symbol}")
        except asyncio.TimeoutError:
            await ctx.channel.send("Type at most **TWO NUMBERS** in *30* seconds **ITS NOT THAT HARD**.\nI should just take your money but... that would be a scam. EthanBot does not scam.")    

class Froligarch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        await self.pping()

    @commands.command(name="manualtally")
    @commands.has_permissions(administrator=True)
    async def manual_pp(self, ctx, days=0):
        await bot.wait_until_ready()
        
        guild = bot.get_guild(423583970328838154)
        channel = guild.get_channel(866168036770578432)
        
        now = datetime.now(timezone.utc)
        after = datetime.combine(now.date(), PP_START).replace(tzinfo=timezone.utc) - timedelta(days=days)
        before = datetime.combine(now.date(), PP_END).replace(tzinfo=timezone.utc) - timedelta(days=days)

        await channel.send("**-=-=- Tallying manually because Zach fucked up -=-=-**")

        messages = await channel.history(limit=None, before=before, after=after).flatten()
        pps = {}
        for msg in messages:
            if (msg.author.id != bot.user.id):
                continue
            embeds = msg.embeds
            if embeds == []:
                continue
            for embed in embeds:
                footer = str(embed.footer.text)
                if (embed.title != "peepee size machine"):
                    continue
                if (footer not in pps) or len(pps) == 0:
                    cur = embed.description.split("\n")
                    pps[footer] = str(cur[1]).count("=")
        pps = dict(sorted(pps.items(), key=lambda item: item[1], reverse=True))
        print(pps)
        description = ""
        if len(pps.items()) == 0:
            description = f"xd yall suck, not even a single pp. Disgracing the Glorious Froligarchy."
        else:
            count = 0
            units = random.choice(["cm", "mm", "m", "in", "ft", "yd"])
            for key, value in pps.items():
                count += 1
                text = f"**({count}).** "
                if (count <= 2):
                    text += "<:poggies:826811320073453598> **FROLIGARCH** "
                if (value <= 1):
                    text += ":pinching_hand: L BOZO "
                member = guild.get_member(int(key))
                text += f"**{member.name}**: {value} {units}\n"
                description += text

        embed = nextcord.Embed(title="LEADERBOARD FOR TODAY", url="https://www.youtube.com/watch?v=iik25wqIuFo", description=description)
        await channel.send(embed=embed)
        await self.remove_froligarchs(guild)
        await self.add_froligarchs(guild, list(pps.items())[:2])

    async def activate_pp(self, announce=False):
        await bot.wait_until_ready()
        
        guild = bot.get_guild(423583970328838154)
        channel = guild.get_channel(866168036770578432)
        
        now = datetime.now(timezone.utc)
        after = datetime.combine(now.date(), PP_START).replace(tzinfo=timezone.utc)
        before = datetime.combine(now.date(), PP_END).replace(tzinfo=timezone.utc)
        duration = (before - after).total_seconds()
        total_seconds = (before - now).total_seconds()

        if (announce == True):
            await channel.send(f"<@&652326925800570880> {prefix}pp")
        if (total_seconds > 0 and total_seconds <= duration):
            print(f"Frogging: {total_seconds}sec remaining")
            await asyncio.sleep(total_seconds)
        elif (total_seconds > duration):
            return
        await channel.send("**-=-=- FROLIGARCHY FOR THE DAY HAS CLOSED. -=-=-**")

        messages = await channel.history(limit=None, before=before, after=after).flatten()
        pps = {}
        for msg in messages:
            if (msg.author.id != bot.user.id):
                continue
            embeds = msg.embeds
            if embeds == []:
                continue
            for embed in embeds:
                footer = str(embed.footer.text)
                if (embed.title != "peepee size machine"):
                    continue
                if (footer not in pps) or len(pps) == 0:
                    cur = embed.description.split("\n")
                    pps[footer] = str(cur[1]).count("=")
        pps = dict(sorted(pps.items(), key=lambda item: item[1], reverse=True))
        print(pps)
        description = ""
        if len(pps.items()) == 0:
            description = f"xd yall suck, not even a single pp. Disgracing the Glorious Froligarchy."
        else:
            count = 0
            units = random.choice(["cm", "mm", "m", "in", "ft", "yd"])
            for key, value in pps.items():
                count += 1
                text = f"**({count}).** "
                if (count <= 2):
                    text += "<:poggies:826811320073453598> **FROLIGARCH** "
                if (value <= 1):
                    text += "<:pinching_hand:> L BOZO "
                member = guild.get_member(int(key))
                text += f"**{member.name}**: {value} {units}\n"
                description += text

        embed = nextcord.Embed(title="LEADERBOARD FOR TODAY", url="https://www.youtube.com/watch?v=iik25wqIuFo", description=description)
        await channel.send(embed=embed)
        await self.remove_froligarchs(guild)
        await self.add_froligarchs(guild, list(pps.items())[:2])

    async def pping(self):
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        target = datetime.combine(now.date(), PP_START).replace(tzinfo=timezone.utc)
        seconds_until_target = math.ceil((target - now).total_seconds())
        print(f"Seconds until target 1: {seconds_until_target}")

        if (seconds_until_target < 0):
            if (seconds_until_target >= -7200):
                await self.activate_pp()
            target = datetime.combine(now.date() + timedelta(days=1), PP_START).replace(tzinfo=timezone.utc)
            seconds_until_target = math.ceil((target - now).total_seconds())
            print(f"Seconds until target 2: {seconds_until_target}")
        # maybe replace 7200 with the difference b/w PP_START and PP_END
        await asyncio.sleep(seconds_until_target)
        await self.activate_pp(announce=True)
        while True:
            now = datetime.utcnow().replace(tzinfo=timezone.utc)
            target = datetime.combine(now.date() + timedelta(days=1), PP_START).replace(tzinfo=timezone.utc)
            seconds_until_target = math.ceil((target - now).total_seconds())
            print(f"Seconds until target 3: {seconds_until_target}")
            await asyncio.sleep(seconds_until_target)
            await self.activate_pp(announce=True)

    async def add_froligarchs(self, guild, members):
        role = guild.get_role(841482931255115816)
        for member in members:
            frog = guild.get_member(int(member[0]))
            await frog.add_roles(role)

    async def remove_froligarchs(self, guild):
        role = guild.get_role(841482931255115816)
        role_members = role.members
        for member in role_members:
            await member.remove_roles(role)

    @commands.command(name='pp')
    async def pp(self, ctx):
        def peepee():
            length = random.randint(0, 15)
            x = random.randint(1, 250)
            if (x == 69):
                length = random.randint(15, 3500)
            return length

        title = "peepee size machine"
        count = peepee()
        if (ctx.author.id == 372841965198376963):
            count = random.randint(0, random.randint(1, 30))
            if (count > 14):
                await asyncio.sleep(3)
                await ctx.channel.send("congor moment")
        if (ctx.author.id == 501505695091392527):
            count = random.randint(0, 20)
            pass
        if (ctx.author.id == 597628340203028485):
            count = -(random.randint(11, 15))
            await ctx.send("some australia type shit")
            description = f"{ctx.message.author.name}'s penis\nᗡ{('=' * abs(count))}8 ({count})"
            embed=nextcord.Embed(title=title, url="https://www.youtube.com/watch?v=iik25wqIuFo", description=description)
            embed.set_footer(text=f"{ctx.message.author.id}")
            await ctx.send(embed=embed)
            return
        description = f"{ctx.message.author.name}'s penis\n8{('=' * count)}D ({count})"
        embed=nextcord.Embed(title=title, url="https://www.youtube.com/watch?v=iik25wqIuFo", description=description)
        embed.set_footer(text=f"{ctx.message.author.id}")
        await ctx.send(embed=embed)

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="roll", aliases=['dice', 'r'])
    async def roll(self, ctx, number=str(100)):
        try:
            if (str(float(number)) == number):
                await ctx.channel.send(f"You ever find a {number} sided die? Well, no, so give me an integer idiot")
                return
        except ValueError:
            await ctx.channel.send(f"You like... what... <:are_you_high:847849655990485002> I can't roll letters nincompoop")
            return

        roll = random.randint(0, int(number))
        await ctx.channel.send(f"Rolling **d{number}**...")
        await ctx.channel.send(f"You rolled **{roll:,}**.")

    @commands.command(name="rollbetween", aliases=['rb', 'dicebetween', 'db'])
    async def roll(self, ctx, start_number=str(0), end_number=str(100)):
        try:
            if (str(float(start_number)) == start_number):
                await ctx.channel.send(f"You ever find a {start_number} sided die? Well, no, so give me an integer idiot")
                return
            if (str(float(end_number)) == end_number):
                await ctx.channel.send(f"I can't roll {end_number}, give me an integer dumb dumb")
                return
            if (int(start_number) > int(end_number)):
                await ctx.channel.send(f"Your second number has to be lower than the first bozo. If you don't specify a second number, it defaults to 100.")
        except ValueError:
            await ctx.channel.send(f"You like... what... <:are_you_high:847849655990485002> I can't roll letters nincompoop")
            return

        roll = random.randint(int(start_number), int(end_number))
        await ctx.channel.send(f"Rolling between **{start_number}** and **{end_number}**...")
        await ctx.channel.send(f"You rolled **{roll:,}**.")

    @commands.command(name="eliminate", aliases=["elim"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def eliminate(self, ctx, member: nextcord.Member = None):
        if (member == None):
            await ctx.channel.send("Hey you little shit I can't eliminate no one")
            return
        if (member.guild_permissions.administrator):
            await ctx.channel.send("https://i.pinimg.com/originals/0f/fd/29/0ffd29da68cc8176440779fcdb5b87bb.jpg")
            self.eliminate.reset_cooldown(ctx)
            return
        nick = member.display_name
        await ctx.channel.send(f'{member.mention} is a lil shit')
        await asyncio.sleep(1)
        await ctx.channel.send('lmao L get eliminated')
        await member.edit(nick="Eliminated")
        await asyncio.sleep(9)
        await ctx.channel.send('oh wait nvm, zzwhoops told me odro days are over.')
        await asyncio.sleep(3)
        await ctx.channel.send('sorry!')
        await asyncio.sleep(1)
        await member.edit(nick=nick)

        await ctx.message.delete()

    @commands.command(name="randomword", aliases=["random", "rword"])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def random_word(self, ctx):
        req = requests.get("https://random-word-api.herokuapp.com/word?number=1")
        words = json.loads(req.text)
        word = random.choice(words)
        await ctx.channel.send(f"Your word is: {word}")

    @commands.command(name="wtf")
    @commands.cooldown(1, 25, commands.BucketType.user)
    async def navy_seal(self, ctx):
        text = "What the fuck did you just fucking say about me, you little bitch? I'll have you know I graduated top of my class in the Navy Seals, and I've been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills. I am trained in gorilla warfare and I'm the top sniper in the entire US armed forces. You are nothing to me but just another target. I will wipe you the fuck out with precision the likes of which has never been seen before on this Earth, mark my fucking words. You think you can get away with saying that shit to me over the Internet? Think again, fucker. As we speak I am contacting my secret network of spies across the USA and your IP is being traced right now so you better prepare for the storm, maggot. The storm that wipes out the pathetic little thing you call your life. You're fucking dead, kid. I can be anywhere, anytime, and I can kill you in over seven hundred ways, and that's just with my bare hands. Not only am I extensively trained in unarmed combat, but I have access to the entire arsenal of the United States Marine Corps and I will use it to its full extent to wipe your miserable ass off the face of the continent, you little shit. If only you could have known what unholy retribution your little \"clever\" comment was about to bring down upon you, maybe you would have held your fucking tongue. But you couldn't, you didn't, and now you're paying the price, you goddamn idiot. I will shit fury all over you and you will drown in it. You're fucking dead, kiddo."
        await ctx.channel.send(text)

class Zach(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="exportchannels")
    async def export_channels(self, ctx):
        guild = bot.get_guild(423583970328838154)
        channels = {}

        for x in guild.text_channels:
            channels[x.name] = x.category

        for x in guild.voice_channels:
            channels[x.name] = x.category

        with open("channels.txt", "wb") as f:
            for key, value in channels.items(): 
                f.write(('%s:%s\n' % (key, value)).encode('utf8'))


"""
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.channel.send(f"Stop spamming me you dolt: try again in {round(error.retry_after, 2)}sec.", delete_after=4)
    if isinstance(error, commands.errors.CommandInvokeError):
        await ctx.channel.send(f"Your input was invalid. Unfortunately, EthanBot does not have a snarky response for you! So, you suck!")
    else:
        print(error)
"""
class EthanBot(commands.Bot):
    def __init__(self, case_insensitive, command_prefix, intents):
        super().__init__(case_insensitive=case_insensitive, command_prefix=command_prefix, intents=intents)

bot = EthanBot(True, prefix, intents)

def setup(bot):
    bot.add_cog(Listeners(bot))
    bot.add_cog(Ethan(bot))
    bot.add_cog(Economy(bot))
    bot.add_cog(Stocks(bot))
    bot.add_cog(Gambling(bot))
    bot.add_cog(Fun(bot))
    bot.add_cog(Froligarch(bot))
    bot.add_cog(Zach(bot))

setup(bot)
bot.run(TOKEN)