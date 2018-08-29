# Copyright 2018-present Kensho Technologies, LLC.
from collections import defaultdict

from graphql_compiler.compiler import blocks


class SqlQueryTree(object):
    def __init__(self, root, query_path_to_location_info, query_path_to_filter, query_path_to_output_fields):
        """Wrap a SqlNode root with additional location_info metadata."""
        self.root = root
        self.query_path_to_location_info = query_path_to_location_info
        self.query_path_to_filter = query_path_to_filter
        self.query_path_to_output_fields = query_path_to_output_fields


class SqlNode(object):
    """Representation of a SQL Query as a tree."""

    def __init__(self, block, query_path):
        """Create a new SqlNode wrapping a Traverse/Recurse/QueryRoot block at a query_path."""
        self.query_path = query_path
        self.block = block
        self.children_nodes = []
        self.recursions = []

    def add_child_node(self, child_node):
        """Add a child node reference to this SqlNode, either non-recursive or recursive."""
        if isinstance(child_node.block, blocks.Recurse):
            self.recursions.append(child_node)
        else:
            self.children_nodes.append(child_node)

    def __str__(self):
        """Return a string representation of a SqlNode."""
        return u'SqlNode({}, children={})'.format(self.query_path, self.children_nodes)

    def __repr__(self):
        """Return the repr of a SqlNode."""
        return self.__str__()
