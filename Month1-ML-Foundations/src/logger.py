import logging

def get_logger(name: str) -> logging.Logger:

    logging.basicConfig(
        level=logging.INFO,
        filename='app.log',
        filemode='a',
        format="%(asctime)s - %(levelname)s - %(message)s"
    )

    return logging.getLogger(name)
