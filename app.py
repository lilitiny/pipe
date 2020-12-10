#!/usr/bin/env python3

from aws_cdk import core

from piplines_webiner.piplines_webiner_stack import PiplinesWebinerStack


app = core.App()
PiplinesWebinerStack(app, "piplines-webiner")

app.synth()
