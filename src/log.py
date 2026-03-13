



from loguru import logger


def logging_file(file):
    """C'est la fonction qui gére le fichier de log """
    logger.remove()
    logger.add(
        file,
        rotation="10 MB",
        retention="30 days",
        compression="zip",
        level="INFO",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} | {message}"
    )
