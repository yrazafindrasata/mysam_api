#! /usr/bin/env python
# -*- coding: utf-8 -*-

from api import create_app


if __name__ == '__main__':
    app = create_app()
    app.run("0.0.0.0", 10006)
