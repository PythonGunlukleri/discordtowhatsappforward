from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from discord.ext import commands
from twilio.rest import Client
import discord

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
  print('Bot giriş yaptı')

@bot.command()
async def mesajgonder(ctx, numara , mesaj):
    account_sid = 'sid' 
    auth_token = 'token' 
    client = Client(account_sid, auth_token) 
    message = client.messages.create( 
                                  from_='whatsapp:+14155238886',  
                                  body=mesaj,      
                                  to='whatsapp:'+numara 
                              ) 
    print(message.sid)
    await ctx.send("Mesajınız gönderildi! Not:Eğer ki !mesajgonderyardım'daki adımları yapmadıysanız mesajınız gitmez! Bu sizi doğrulamamız için gereklidir." + " Developer için hata bakma message id : " + message.sid)
@bot.command()
async def yardım(ctx):
    embed=discord.Embed(title="Emrovsky Whatsapp", description="https://www.youtube.com/channel/UC_q6e2_Um5qiRZZTqY1JgbQ python günlükleri tarafından hazırlanan discord + whatsapp bot", color=0x00ff00)
    embed.add_field(name="!mesajgonder", value="!mesajgonder <numara> <mesaj>", inline=False)
    embed.add_field(name="!mesajgonderyardım", value="yardım menüsü", inline=False)
    await ctx.send(embed=embed)
@bot.command()
async def mesajgonderyardım(ctx):
    await ctx.send("İlk olarak whatsappdan mesaj atacağınız numaradan +14155238886'e join nation-example yazın.Whatsapp telefonunuzda indirili ise buraya basabilirsiniz : http://wa.me/+14155238886?text=join%20nation-example")

    


bot.run('Njk4ODk5Mjk1MTE3NTA4NjM5.XpMisA.wo0Bi-DL4SXKrhM8XstZEJkcNAc')