#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8

import unittest
from unittest.mock import patch, MagicMock

from app import candidate

class TestHelloModule(unittest.TestCase):

    @patch("boto3.client")
    @patch("time.sleep")
    def test_candidate_returns_success(self, sleep_mock, sqs_mock):
        result = candidate.submit("test", None)
        sleep_mock.assert_called_once()
