import discord

with open("data.bot", "r") as dataFile:
    TOKEN = dataFile.read()


class Client(discord.Client):
    @staticmethod
    async def on_ready():
        print("Bot is logged in.")
        await client.get_channel(842001152068419584).send("Hi. I am gipsy. I am a bot developed for this server, " +
                                                          "type /info to learn more about me.")

    @staticmethod
    async def on_message(message):
        if message.author == client.user:
            return
        print(f"Got message: \"{message.content}\" on \"{message.channel}\"")
        with open("responses.bot", "r") as responsesF:
            responses = responsesF.read()
            responses = responses.replace("\n", "%")
            responses = responses.split("%")
        for index, x in enumerate(responses):
            if responses[index] == message.content.lower():
                if responses[index + 1][0:2] == "!p":
                    await message.channel.send(responses[index + 1][2:], reference=message)
                    return
                print("Sending: " + responses[index + 1])
                await message.channel.send(responses[index + 1])
                return


client = Client()
try:
    client.run(TOKEN)
except:
    pass
