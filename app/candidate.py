#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import json
import logging
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("candidate")

def post_candidate(event, context):
    """
    POST candidate to DynamoDB
    """

    msg = "Hello World"
    logger.warning(f"message: {msg}")

    logger.info("start sleeping...")
    time.sleep(1)
    logger.warning("stop sleeping...")

    resp = {
        "statusCode": 200,
        "body": json.dumps(msg)
    }

    logger.warning(f"resp: {resp}")

    return resp

def get_candidate(event, context):
    """
    Get candidates from DynamoDB
    """

    resp = {
        "statusCode": 200,
        "body": json.dumps({})
    }
    logger.warning(f"resp: {resp}")

    return resp


if __name__ == "__main__":
    post_candidate(None, None)
    get_candidate(None, None)
