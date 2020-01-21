#!/usr/bin/env python3

from jinjarg import Jinjarg


class Example(Jinjarg):
    def setup(self):
        self.parser.add_argument("--boolean", action='store_true', default=False)
        self.parser.add_argument("--number", type=str, required=True)
        self.parser.add_argument("--iterable", nargs='+', default=[])


if __name__ == '__main__':
    print(Example())
