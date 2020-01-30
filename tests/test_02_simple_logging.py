import pytest
import logging


logger = logging.getLogger(__name__)


def test_one():
    logger.info("xxx")
    logger.info("xxx")
    logger.info("xxx")
    logger.info("xxx")
    logger.info("xxx")
    logger.info("xxx")
    print('hi')