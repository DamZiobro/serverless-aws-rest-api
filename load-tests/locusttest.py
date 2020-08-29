#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2020 damian <damian@damian-desktop>
#
# Distributed under terms of the MIT license.

from locust import HttpUser, task, between

class SubmitBehavior(HttpUser):

    @task(1)
    def test_submit(self):
        self.client.post("/develop/candidates", name="Test /submit endpoint")

    wait_time = between(5, 15)
