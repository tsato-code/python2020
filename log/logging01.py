from logging import getLogger, StreamHandler, DEBUG, Formatter, FileHandler
import os


logger = getLogger(None)


def main():
    logger.info("start")
    logger.info("process 1")
    # process 1
    logger.info("process 2")
    # process 2


if __name__ == "__main__":
    fmt_text = (
        "%(asctime)s %(name)s %(lineno)d"
        " [%(levelname)s][%(funcName)s] %(message)s"
    )
    log_fmt = Formatter(fmt_text)

    handler = StreamHandler()
    handler.setLevel("INFO")
    handler.setFormatter(log_fmt)
    logger.setLevel("INFO")
    logger.addHandler(handler)

    handler = FileHandler(
        os.path.basename(os.path.abspath(__file__)) + ".log", "a"
    )
    handler.setLevel(DEBUG)
    handler.setFormatter(log_fmt)
    logger.setLevel(DEBUG)
    logger.addHandler(handler)

    main()
