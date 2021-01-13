#!/usr/bin/python
import sys
sys.path.append('../../')
from discord_webhook import DiscordWebhook, DiscordEmbed
sys.path.insert(0, '../.usage/Current')
with open('../.usage/Current') as fp:
	usage=int(fp.read())
from datetime import datetime

if usage>10000:
	webhook=DiscordWebhook(url='https://discord.com/api/webhooks/798835302595952690/6Vhn2xUHh4YXrI-8H1u37ybl-P3bcRmFDqsp-RjM_AcDjcKCG3Tvb29BfTEjVxA9reMe', username="Spidey")
	embed = DiscordEmbed(title='Peringatan', description='Penggunaan melebihi batas!!!', color=242424)
	embed.set_footer(text='Astaga kok bisa kelewat')
	embed.set_timestamp()
	embed.add_embed_field(name='Saran', value='Kurangi penggunaan')
	embed.add_embed_field(name='Cek', value='Buka OS ubuntu buat cek!')

	webhook.add_embed(embed)
	response = webhook.execute()

else:
	pass

