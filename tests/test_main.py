# -*- mode: python -*- -*- coding: utf-8 -*-
import pytest

from app.__main__ import greetings

def test_app():
    name = 'Doe'
    result = greetings(name)

    assert name in result
