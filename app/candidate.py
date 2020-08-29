#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import json
import logging
import time

logging.basicConfig(level="INFO")
logger = logging.getLogger("candidate")

def submit(event, context):
    """
    First Lambda function. Triggered manually.
    :param event: AWS event data
    :param context: AWS function's context
    :return: ''
    """

    msg = "Hello World"
    logger.warning(f"message: {msg}")

    logger.warning("start sleeping...")
    time.sleep(1)
    logger.warning("stop sleeping...")

    resp = {
        "statusCode": 200,
        "body": json.dumps(msg)
    }

    logger.warning(f"resp: {resp}")

    return resp

if __name__ == "__main__":
    submit(None, None)
