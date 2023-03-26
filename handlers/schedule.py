from aiogram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger

async def new_year(bot: Bot):
    await bot.send_message(ADMINS[0], "Happy New Year!")

async def set_scheduler:
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        new_year,
        trigger=CronTrigger(minute=0, hour=0, day='1', month='1', day_of_week='*'),
        kwargs={"bot": bot},
    )

scheduler.start()