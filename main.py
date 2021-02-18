import os
from app import app
from apscheduler.schedulers.background import BackgroundScheduler
from tasks import mass_update

if __name__ == '__main__':
    scheduler = BackgroundScheduler(timezone='UTC')
    scheduler.start()
    scheduler.add_job(func=mass_update,
                      trigger='cron',
                      minute=0,
                      id='hourly_mass_update')
    app.run(host=os.environ.get('STOCKMAILER_HOST'), port=int(os.environ.get('STOCKMAILER_PORT')))
