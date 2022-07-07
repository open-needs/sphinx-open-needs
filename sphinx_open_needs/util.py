import logging
import operator
from functools import reduce  # forward compatibility for Python 3
from typing import Dict

from jinja2 import Template

log = logging.getLogger(__name__)


def dict_get(root, items, default=None):
    """
    Access a nested object in root by item sequence.

    Usage::
       data = {"nested": {"a_list": [{"finally": "target_data"}]}}
       value = dict_get(["nested", "a_list", 0, "finally"], "Not_found")

    """
    try:
        value = reduce(operator.getitem, items, root)
    except (KeyError, IndexError, TypeError) as e:
        log.debug(e)
        return default
    return value


def dict_undefined_set(dict_obj, key, value):
    if key not in dict_obj:
        dict_obj[key] = value


def jinja_parse(context: Dict, jinja_string: str) -> str:
    """
    Function to parse mapping options set to a string containing jinja template format.

    :param context: Data to be used as context in rendering jinja template
    :type: dict
    :param jinja_string: A jinja template string
    :type: str
    :return: A rendered jinja template as string
    :rtype: str

    """
    try:
        content_template = Template(jinja_string, autoescape=True)
    except Exception as e:
        raise ReferenceError(f'There was an error in the jinja statement: "{jinja_string}". ' f"Error Msg: {e}")

    content = content_template.render(**context)
    return content
