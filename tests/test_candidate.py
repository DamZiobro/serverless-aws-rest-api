#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import unittest
from unittest.mock import patch, MagicMock

from app import candidate

class TestHelloModule(unittest.TestCase):

    @patch("boto3.client")
    @patch("time.sleep")
    def test_postCandidate_returns_success(self, sleep_mock, sqs_mock):
        result = candidate.postCandidate("test", None)
        sleep_mock.assert_called_once()

    @patch("boto3.client")
    @patch("json.dumps")
    def test_getCandidate_returns_success(self, json_dumps_mock, sqs_mock):
        result = candidate.getCandidate("test", None)
        json_dumps_mock.assert_called_once_with({})
