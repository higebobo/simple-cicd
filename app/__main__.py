# -*- mode: python -*- -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

load_dotenv()


def greetings(name=None):
    if not name:
        name = os.getenv('NAME', 'John')
    return f'Hello {name}'


if __name__ == "__main__":
    print(greetings())
