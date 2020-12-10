#!/usr/bin/env python3

from aws_cdk import core

from piplines_webiner.piplines_webiner_stack import PipelinesWebinarStack
from piplines_webiner.pipeline_stack import PipelineStack


app = core.App()
PipelinesWebinarStack(app, "pipelines-webinar")
PipelineStack(app, 'PipelineStack', env={
    'account': '900985145045',
    'region': 'us-east-1'
})
app.synth()
