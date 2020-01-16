from flask_script import Manager
from flask_migrate import Migrate,MigrateCommand
from app import app,db
manager =Manager(app)
Migrate(app,db)

manager.add_command("heyangyang",MigrateCommand)


#python manage.py heyangyang

if __name__ == "__main__":
    manager.run()