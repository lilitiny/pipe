from os import path


from aws_cdk import core
import aws_cdk.aws_lambda as lmb
import aws_cdk.aws_apigateway as apigw


class PipelinesWebinarStack(core.Stack):

    def init(self, scope: core.Construct, construct_id: str, kwargs) -> None:
        super().init(scope, construct_id, kwargs)



        # The code that defines your stack goes here
        this_dir = path.dirname(__file__)

        handler = lmb.Function(self, 'Handler',
            runtime=lmb.Runtime.PYTHON_3_7,
            handler='handler.handler',
            code=lmb.Code.from_asset(path.join(this_dir, 'lambda')))




        gw = apigw.LambdaRestApi(self, 'Gateway',
            description='Endpoint for a simple Lambda-powered web service',
            handler=handler.current_version)


        self.url_output = core.CfnOutput(self, 'Url',
            value=gw.url)