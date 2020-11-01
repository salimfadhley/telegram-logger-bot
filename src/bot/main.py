import logging
from bot.bot import main as bot_main

log = logging.getLogger(__name__)

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    bot_main()

if __name__ == "__main__":
    log.info("Starting the bot!")
    main()
