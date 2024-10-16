from aws_cdk import (
    Stack,
    aws_apigateway as apigateway,
    aws_lambda as lambda_,
    aws_lambda as _lambda,
    aws_iam as iam, BundlingOptions, Duration,
    aws_s3 as s3, aws_lambda_event_sources, RemovalPolicy,
    aws_dynamodb as dynamodb,
)
from constructs import Construct

class CloudBackStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        bucket = s3.Bucket(
            self, "matijafesfsfesfes",
            bucket_name="matijadwadawdaw",

            cors=[
                s3.CorsRule(
                    allowed_methods=[
                        s3.HttpMethods.GET,
                        s3.HttpMethods.PUT,
                        s3.HttpMethods.POST,
                        s3.HttpMethods.DELETE,
                        s3.HttpMethods.HEAD
                    ],
                    allowed_origins=["*"],
                    allowed_headers=["*"]
                )
            ],
            removal_policy=RemovalPolicy.DESTROY
        )

        s3_role = iam.Role(
            self, "S3AccessRole",
            assumed_by=iam.ServicePrincipal("s3.amazonaws.com")
        )
        #
        # s3_role.add_to_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         effect=iam.Effect.ALLOW,
        #         actions=[
        #             "s3:GetObject",
        #             "s3:PutObject",
        #         ],
        #         resources=[
        #             "arn:aws:s3:::content-bucket-cloud-app-movie2/*"
        #
        #         ]
        #     )
        # )
        #
        table = dynamodb.Table(
            self, 'unique-initialtable-nameMP',
            table_name='unique-initialtable-nameMP',
            partition_key={'name': 'id', 'type': dynamodb.AttributeType.STRING},
            #sort_key={'name': 'title', 'type': dynamodb.AttributeType.STRING},
            stream=dynamodb.StreamViewType.NEW_IMAGE
        )
        #
        # lambda_role = iam.Role(
        #     self, "LambdaRole",
        #     assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        # )
        # lambda_role.add_managed_policy(
        #     iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        # )
        # lambda_role.add_to_policy(
        #     iam.PolicyStatement(
        #         effect=iam.Effect.ALLOW,
        #         actions=[
        #             "dynamodb:DescribeTable",
        #             "dynamodb:Query",
        #             "dynamodb:Scan",
        #             "dynamodb:GetItem",
        #             "dynamodb:PutItem",
        #             "dynamodb:UpdateItem",
        #             "dynamodb:DeleteItem",
        #             "s3:GetObject",
        #             "s3:PutObject",
        #             "s3:PutObjectACL",
        #             "cognito-idp:AdminCreateUser",
        #             "cognito-idp:AdminInitiateAuth",
        #             "cognito-idp:AdminRespondToAuthChallenge",
        #             "cognito-idp:AdminAddUserToGroup",
        #             "cognito-idp:AdminRemoveUserFromGroup",
        #             "cognito-idp:AdminGetUser",
        #             "cognito-idp:AdminUpdateUserAttributes",
        #             "sns:Publish",
        #             "states:StartExecution",
        #             "states:DescribeExecution",
        #             "sns:Subscribe"
        #         ],
        #         resources=[
        #             f"{bucket.bucket_arn}/*",
        #             table.table_arn
        #         ]
        #     )
        # )

        api_gateway_role = iam.Role(self, "ApiGatewayRole",
                                    assumed_by=iam.ServicePrincipal("apigateway.amazonaws.com"),
                                    description="Role for API Gateway to invoke lambda functions")

        api_gateway_role.add_to_policy(iam.PolicyStatement(
            actions=["lambda:InvokeFunction"],
            resources=["*"]
        ))

        self.api = apigateway.RestApi(self, "Internship",
                                      rest_api_name="Internship",
                                      description="",
                                      endpoint_types=[apigateway.EndpointType.REGIONAL],
                                      default_cors_preflight_options={
                                          "allow_origins": apigateway.Cors.ALL_ORIGINS,
                                          "allow_methods": apigateway.Cors.ALL_METHODS
                                      }
                                      )

        lambda_role = iam.Role(
            self, "LambdaRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com")
        )
        lambda_role.add_managed_policy(
            iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
        )
        lambda_role.add_to_policy(
            iam.PolicyStatement(
                effect=iam.Effect.ALLOW,
                actions=[
                    "dynamodb:DescribeTable",
                    "dynamodb:Query",
                    "dynamodb:Scan",
                    "dynamodb:GetItem",
                    "dynamodb:PutItem",
                    "dynamodb:UpdateItem",
                    "dynamodb:DeleteItem",
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:PutObjectACL",
                ],
                resources=[
                    f"{bucket.bucket_arn}/*",
                    table.table_arn,
                ]
            )
        )

        def create_lambda_function(id, name, handler, include_dir, method, layers, database_dynamo, database_s3):
            env = 'TABLE_NAME'
            if database_dynamo is not None:
                database = database_dynamo
            else:
                if database_dynamo is None and database_s3 is None:
                    database = ""
                else:
                    env = 'BUCKET_NAME'
                    database = database_s3
            function = _lambda.Function(
                self, id,
                function_name=name,
                runtime=_lambda.Runtime.PYTHON_3_9,
                layers=layers,
                handler=handler,
                code=_lambda.Code.from_asset(include_dir,
                                             ),
                memory_size=128,
                timeout=Duration.seconds(10),
                environment={
                    env: database,
                },
                role=lambda_role
            )

            return function

        hello_world_lambda = create_lambda_function(
            "helloWorldExample",
            "helloWorld",
            "helloWorld.lambda_handler",
            "helloWorld",
            "GET",
            [],
            None,
            None
        )

        hello_world_lambda.add_permission(
            "ApiGatewayInvokePermission",
            action="lambda:InvokeFunction",
            principal=iam.ServicePrincipal("apigateway.amazonaws.com"),
            source_arn=self.api.arn_for_execute_api("/*/*/*")
        )

        self.api.root.add_resource("helloWorld").add_method("GET", apigateway.LambdaIntegration(hello_world_lambda,
                                                                                              credentials_role=api_gateway_role,
                                                                                              proxy=True))
