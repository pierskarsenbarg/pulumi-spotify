# coding=utf-8
# *** WARNING: this file was generated by pulumi. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from . import _utilities
import typing
# Export this package's modules as members:
from .provider import *
from .random import *
_utilities.register(
    resource_modules="""
[
 {
  "pkg": "spotify",
  "mod": "index",
  "fqn": "pulumi_spotify",
  "classes": {
   "spotify:index:Random": "Random"
  }
 }
]
""",
    resource_packages="""
[
 {
  "pkg": "spotify",
  "token": "pulumi:providers:spotify",
  "fqn": "pulumi_spotify",
  "class": "Provider"
 }
]
"""
)
