import redis
import os
import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def redis_url_key():
    return 'REDIS_URL'


def trigger_time_key():
    return 'TRIGGER_TIME'


triggerTime = os.environ[trigger_time_key()]

redisUrl = os.environ[redis_url_key()]

r = redis.Redis.from_url(redisUrl)


scheduler = BlockingScheduler()


@scheduler.scheduled_job('cron', day_of_week='mon-sun', hour=int(triggerTime))
def send_subscription():
    print('SUB DID TRIGGERED')
    r.publish('SUB', 'FIRE')

#
# @scheduler.scheduled_job('interval', seconds=int(triggerTime))
# def timed_job():
#     print('This job is run every three minutes.')
#     r.publish('SUB', 'FIRE')


print("START SCHEDULER")
scheduler.start()
