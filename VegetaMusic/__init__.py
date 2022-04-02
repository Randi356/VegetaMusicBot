# Credits @TeamYukki 
# by @rencprx 

from VegetaMusic.core.bot import YukkiBot
from VegetaMusic.core.dir import dirr
from VegetaMusic.core.git import git
from VegetaMusic.core.userbot import Userbot
from VegetaMusic.misc import dbb, heroku, sudo

from .logging import LOGGER

# Directories
dirr()

# Check Git Updates
git()

# Initialize Memory DB
dbb()

# Heroku APP
heroku()

# Load Sudo Users from DB
sudo()

# Bot Client
app = VegetaBot()

# Assistant Client
userbot = Userbot()

from .platforms import *

YouTube = YouTubeAPI()
Telegram = TeleAPI()
