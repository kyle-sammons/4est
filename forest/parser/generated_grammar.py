#!/usr/bin/env python
# -*- coding: utf-8 -*-

# CAVEAT UTILITOR
#
# This file was automatically generated by Grako.
#
#    https://pypi.python.org/pypi/grako/
#
# Any changes you make to it will be overwritten the next time
# the file is generated.


from __future__ import print_function, division, absolute_import, unicode_literals

from grako.buffering import Buffer
from grako.parsing import graken, Parser
from grako.util import re, RE_FLAGS, generic_main  # noqa


KEYWORDS = {}


class ForestBuffer(Buffer):
    def __init__(
        self,
        text,
        whitespace=None,
        nameguard=False,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        namechars='',
        **kwargs
    ):
        super(ForestBuffer, self).__init__(
            text,
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            namechars=namechars,
            **kwargs
        )


class ForestParser(Parser):
    def __init__(
        self,
        whitespace=None,
        nameguard=False,
        comments_re=None,
        eol_comments_re=None,
        ignorecase=None,
        left_recursion=False,
        parseinfo=True,
        keywords=None,
        namechars='',
        buffer_class=ForestBuffer,
        **kwargs
    ):
        if keywords is None:
            keywords = KEYWORDS
        super(ForestParser, self).__init__(
            whitespace=whitespace,
            nameguard=nameguard,
            comments_re=comments_re,
            eol_comments_re=eol_comments_re,
            ignorecase=ignorecase,
            left_recursion=left_recursion,
            parseinfo=parseinfo,
            keywords=keywords,
            namechars=namechars,
            buffer_class=buffer_class,
            **kwargs
        )

    @graken()
    def _start_(self):

        def block0():
            self._statement_()
        self._positive_closure(block0)

    @graken()
    def _statement_(self):
        with self._choice():
            with self._option():
                self._print_()
            with self._option():
                self._input_()
            with self._option():
                self._pop_()
            with self._option():
                self._value_()
            with self._option():
                self._dup_()
            with self._option():
                self._swap_()
            with self._option():
                self._add_()
            with self._option():
                self._sub_()
            with self._option():
                self._mul_()
            with self._option():
                self._mod_()
            with self._option():
                self._pow_()
            with self._option():
                self._div_()
            with self._option():
                self._if_()
            with self._option():
                self._equality_()
            with self._option():
                self._iterate_()
            self._error('no available options')

    @graken()
    def _input_(self):
        self._token(',')

    @graken()
    def _if_(self):
        self._token('?')
        self._statement_()
        self._else_()

    @graken()
    def _else_(self):
        self._token('#')
        self._statement_()

    @graken()
    def _equality_(self):
        self._token('=')

    @graken()
    def _iterate_(self):
        self._token('I')

        def block0():
            self._statement_()
        self._positive_closure(block0)
        self._token('E')

    @graken()
    def _pow_(self):
        self._token('^')

    @graken()
    def _mod_(self):
        self._token('%')

    @graken()
    def _add_(self):
        self._token('+')

    @graken()
    def _sub_(self):
        self._token('-')

    @graken()
    def _mul_(self):
        self._token('*')

    @graken()
    def _div_(self):
        self._token('/')

    @graken()
    def _dup_(self):
        self._token('U')

    @graken()
    def _swap_(self):
        self._token('S')

    @graken()
    def _print_(self):
        self._token('.')

    @graken()
    def _pop_(self):
        self._token('O')

    @graken()
    def _value_(self):
        with self._choice():
            with self._option():
                self._number_()
            with self._option():
                self._string_()
            with self._option():
                self._boolean_()
            self._error('no available options')

    @graken()
    def _boolean_(self):
        with self._choice():
            with self._option():
                self._token('T')
            with self._option():
                self._token('F')
            self._error('expecting one of: F T')

    @graken()
    def _string_(self):
        self._token('"')
        self._letters_()
        self._token('"')

    @graken()
    def _number_(self):
        self._token('D')
        self._digits_()

    @graken()
    def _digits_(self):
        self._pattern(r'[0-9]+')

    @graken()
    def _letters_(self):
        self._pattern(r'[a-zA-Z ]+')


class ForestSemantics(object):
    def start(self, ast):
        return ast

    def statement(self, ast):
        return ast

    def input(self, ast):
        return ast

    def if_(self, ast):
        return ast

    def else_(self, ast):
        return ast

    def equality(self, ast):
        return ast

    def iterate(self, ast):
        return ast

    def pow(self, ast):
        return ast

    def mod(self, ast):
        return ast

    def add(self, ast):
        return ast

    def sub(self, ast):
        return ast

    def mul(self, ast):
        return ast

    def div(self, ast):
        return ast

    def dup(self, ast):
        return ast

    def swap(self, ast):
        return ast

    def print(self, ast):
        return ast

    def pop(self, ast):
        return ast

    def value(self, ast):
        return ast

    def boolean(self, ast):
        return ast

    def string(self, ast):
        return ast

    def number(self, ast):
        return ast

    def digits(self, ast):
        return ast

    def letters(self, ast):
        return ast


def main(filename, startrule, **kwargs):
    with open(filename) as f:
        text = f.read()
    parser = ForestParser()
    return parser.parse(text, startrule, filename=filename, **kwargs)


if __name__ == '__main__':
    import json
    from grako.util import asjson

    ast = generic_main(main, ForestParser, name='Forest')
    print('AST:')
    print(ast)
    print()
    print('JSON:')
    print(json.dumps(asjson(ast), indent=2))
    print()
