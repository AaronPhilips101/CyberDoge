#Die Module for CyberDoge
#Created By @itexpert120
#Modifyed By @AaronPhilips101

@client.on(events("coinflip ?(.*)"))
async def handler(event):
    if event.fwd_from:
        return
    x = random.randint(1, 6)
await event.edit("Rolling Dice")
time.sleep(1)

await event.edit(f"The Die is: {x}")


ENV.HELPER.update({
    "die": "\
.die``` [No Arguemts Present]\
\nUsage: Roll a Dice.\
"
})
