import sc2
from sc2 import run_game, Maps, Race, Difficulty
from sc2.player import Bot, Computer


class SentdeBot(sc2.BotAI):
	async def on_step(self, iteration):
		#distributing the workers
		await self.distribute_workers()

run_game()