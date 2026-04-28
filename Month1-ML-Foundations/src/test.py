from logger import get_logger
from config import APP_NAME, AUTHOR

logger = get_logger(__name__)

def main() -> None:

    logger.info(f'Starting the {APP_NAME}')
    logger.info(f'Author of this app is {AUTHOR}')
    logger.info(f'App is running smoothly.')

if __name__ == '__main__':
    main()