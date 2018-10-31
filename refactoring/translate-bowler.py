#!/usr/bin/env bowler
# Copyright 2018 John Reese
# Licensed under the MIT License

import re
from bowler.helpers import print_tree, find_first
from bowler.query import Query
from bowler.types import TOKEN, SYMBOL, Node
from fissix.fixer_util import Call, Dot, Name, LParen, RParen, String, FromImport, Newline

def add_import(ln, cap, fn):
    while ln.parent is not None:
        ln = ln.parent

    first_node = ln.children[0]
    new_import = Node(
        SYMBOL.simple_stmt,
        [
            FromImport("asyncio", [Name("run", prefix=" ")]),
            Newline(),
        ],
        prefix=first_node.prefix,
    )

    first_node.prefix = ""
    ln.insert_child(0, new_import)

(
    Query("source.py")
    .select_function("runner")
    .is_call()
    .modify(add_import)
    .rename("run")
    .select_function("runner")
    .is_def()
    .modify(lambda ln, cap, fn: ln.remove())
    # .diff()
)

(
    Query()
    .select_function("anxiety")
    .rename("consider")
    .modify_argument(
        name="count", default_value="5",
    )
    # .diff()
)

(
    Query()
    .select_function("anxiety")
    .rename("consider")
    .modify_argument(
        name="count", default_value="5",
    )
    .select_function("despair")
    .rename("take_action")
    .add_argument(
        name="action", value='"vote"',
        positional=True, type_annotation="str",
    )
    # .diff()
)

def fix_despair(ln, cap, fn):
    stmt = find_first(ln, SYMBOL.simple_stmt, recursive=True)
    if stmt:
        new_call = Call(
            Name("print"),
            args=[
                String('f"Go {action}!!!"')
            ],
        )
        stmt.replace(
            Node(
                SYMBOL.simple_stmt,
                children=[new_call],
            )
        )


(
    Query()
    .select_function("anxiety")
    .rename("consider")
    .modify_argument(
        name="count", default_value="5",
    )
    .select_function("despair")
    .rename("take_action")
    .add_argument(
        name="action", value='"vote"',
        positional=True, type_annotation="str",
    )
    .modify(fix_despair)
    .diff()
)
