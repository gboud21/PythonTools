import logging.config

logger = logging.getLogger("reqLog")

logging_config = {
    "version" : 1,
    "disable_existing_loggers" : False,
    "formatters" : {
        "simple" : {
            "format" : "%(levelname)s: %(message)s",
        }
    },
    "handlers" : {
        "stdout" : {
            "class" : "logging.StreamHandler",
            "formatter" : "simple",
            "stream" : "ext//sys.stdout",
        }
    },
    "loggers" : {
        "root" : {"level" : "DEBUG", "handlers" : ["stdout"]}
    },
}

def main():
    logging.config.dictConfig(config=logging_config)
    logger.addHandler(logging.StreamHandler())
    logger.debug("debug message")
    logger.info("info message")
    logger.warning("warning message")
    logger.error("error message")
    logger.critical("critical message")
    try:
        1 / 0
    except ZeroDivisionError:
        logger.exception("exception message")

if __name__ == "__main__":
    main()