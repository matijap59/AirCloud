'''
# AWS::InspectorV2 Construct Library

This module is part of the [AWS Cloud Development Kit](https://github.com/aws/aws-cdk) project.

```python
import aws_cdk.aws_inspectorv2 as inspector
```

<!--BEGIN CFNONLY DISCLAIMER-->

There are no official hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet. Here are some suggestions on how to proceed:

* Search [Construct Hub for InspectorV2 construct libraries](https://constructs.dev/search?q=inspectorv2)
* Use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, in the same way you would use [the CloudFormation AWS::InspectorV2 resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InspectorV2.html) directly.

<!--BEGIN CFNONLY DISCLAIMER-->

There are no hand-written ([L2](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_lib)) constructs for this service yet.
However, you can still use the automatically generated [L1](https://docs.aws.amazon.com/cdk/latest/guide/constructs.html#constructs_l1_using) constructs, and use this service exactly as you would using CloudFormation directly.

For more information on the resources and properties available for this service, see the [CloudFormation documentation for AWS::InspectorV2](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_InspectorV2.html).

(Read the [CDK Contributing Guide](https://github.com/aws/aws-cdk/blob/main/CONTRIBUTING.md) and submit an RFC if you are interested in contributing to this construct library.)

<!--END CFNONLY DISCLAIMER-->
'''
from pkgutil import extend_path
__path__ = extend_path(__path__, __name__)

import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import constructs as _constructs_77d1e7e8
from .. import (
    CfnResource as _CfnResource_9df397a6,
    IInspectable as _IInspectable_c2943556,
    IResolvable as _IResolvable_da3f097b,
    ITaggableV2 as _ITaggableV2_4e6798f8,
    TagManager as _TagManager_0a598cb3,
    TreeInspector as _TreeInspector_488e0dd5,
)


@jsii.implements(_IInspectable_c2943556, _ITaggableV2_4e6798f8)
class CfnCisScanConfiguration(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration",
):
    '''The CIS scan configuration.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html
    :cloudformationResource: AWS::InspectorV2::CisScanConfiguration
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        # one_time: Any
        
        cfn_cis_scan_configuration = inspectorv2.CfnCisScanConfiguration(self, "MyCfnCisScanConfiguration",
            scan_name="scanName",
            schedule=inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                ),
                monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                    day="day",
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                ),
                one_time=one_time,
                weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                    days=["days"],
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            ),
            security_level="securityLevel",
            tags={
                "tags_key": "tags"
            },
            targets=inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                account_ids=["accountIds"],
        
                # the properties below are optional
                target_resource_tags={
                    "target_resource_tags_key": ["targetResourceTags"]
                }
            )
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        scan_name: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.ScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        security_level: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.CisTargetsProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param scan_name: The name of the CIS scan configuration.
        :param schedule: The CIS scan configuration's schedule.
        :param security_level: The CIS scan configuration's CIS Benchmark level.
        :param tags: The CIS scan configuration's tags.
        :param targets: The CIS scan configuration's targets.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__ee74cd979e0690afc5238694387a2bb443783c172f8af7544b4b5c468df80b9c)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnCisScanConfigurationProps(
            scan_name=scan_name,
            schedule=schedule,
            security_level=security_level,
            tags=tags,
            targets=targets,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1c340cf5a8052b5b5d1021305af92e23dcb4f62645a1014b0a49bb031d376ee8)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daf01f89651352328420f5a52535d8376706a979b3cb022464732eddc33e94c8)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The CIS scan configuration's scan configuration ARN.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cdkTagManager")
    def cdk_tag_manager(self) -> _TagManager_0a598cb3:
        '''Tag Manager which manages the tags for this resource.'''
        return typing.cast(_TagManager_0a598cb3, jsii.get(self, "cdkTagManager"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="scanName")
    def scan_name(self) -> typing.Optional[builtins.str]:
        '''The name of the CIS scan configuration.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "scanName"))

    @scan_name.setter
    def scan_name(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8f6f074ec34751eb6d66964ee6738d096c1429db3564cba2005e530e659871bc)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scanName", value)

    @builtins.property
    @jsii.member(jsii_name="schedule")
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.ScheduleProperty"]]:
        '''The CIS scan configuration's schedule.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.ScheduleProperty"]], jsii.get(self, "schedule"))

    @schedule.setter
    def schedule(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.ScheduleProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__17c38c82086f8ffe9712e88585d2f980663e72bbb5b6ac70574594200cb759c2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schedule", value)

    @builtins.property
    @jsii.member(jsii_name="securityLevel")
    def security_level(self) -> typing.Optional[builtins.str]:
        '''The CIS scan configuration's CIS Benchmark level.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "securityLevel"))

    @security_level.setter
    def security_level(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__53a976b81d95f07052322a80e8b1ff546ae083bdb3cb3d358b91e5b7e50b0909)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "securityLevel", value)

    @builtins.property
    @jsii.member(jsii_name="tags")
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The CIS scan configuration's tags.'''
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "tags"))

    @tags.setter
    def tags(
        self,
        value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__5b4e1fac23c27cbc692267473e4cf9258b43062b9aea2a43b116dcfb105adb0d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tags", value)

    @builtins.property
    @jsii.member(jsii_name="targets")
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.CisTargetsProperty"]]:
        '''The CIS scan configuration's targets.'''
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.CisTargetsProperty"]], jsii.get(self, "targets"))

    @targets.setter
    def targets(
        self,
        value: typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.CisTargetsProperty"]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__8afffccf2a9a470f423d247abd4a6dfe735dc39c53a2abe26c8cdb1844ec12a2)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "targets", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.CisTargetsProperty",
        jsii_struct_bases=[],
        name_mapping={
            "account_ids": "accountIds",
            "target_resource_tags": "targetResourceTags",
        },
    )
    class CisTargetsProperty:
        def __init__(
            self,
            *,
            account_ids: typing.Sequence[builtins.str],
            target_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
        ) -> None:
            '''The CIS targets.

            :param account_ids: The CIS target account ids.
            :param target_resource_tags: The CIS target resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                cis_targets_property = inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                    account_ids=["accountIds"],
                
                    # the properties below are optional
                    target_resource_tags={
                        "target_resource_tags_key": ["targetResourceTags"]
                    }
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__48b07d123221faefb49073a28736f1aec9dc2a488247f39ec213274809cd3b6a)
                check_type(argname="argument account_ids", value=account_ids, expected_type=type_hints["account_ids"])
                check_type(argname="argument target_resource_tags", value=target_resource_tags, expected_type=type_hints["target_resource_tags"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "account_ids": account_ids,
            }
            if target_resource_tags is not None:
                self._values["target_resource_tags"] = target_resource_tags

        @builtins.property
        def account_ids(self) -> typing.List[builtins.str]:
            '''The CIS target account ids.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html#cfn-inspectorv2-cisscanconfiguration-cistargets-accountids
            '''
            result = self._values.get("account_ids")
            assert result is not None, "Required property 'account_ids' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def target_resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]]:
            '''The CIS target resource tags.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-cistargets.html#cfn-inspectorv2-cisscanconfiguration-cistargets-targetresourcetags
            '''
            result = self._values.get("target_resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.List[builtins.str]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "CisTargetsProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"start_time": "startTime"},
    )
    class DailyScheduleProperty:
        def __init__(
            self,
            *,
            start_time: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A daily schedule.

            :param start_time: The schedule start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                daily_schedule_property = inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__bd3a6a48de82a0a7da55bb17cc5099cc069382b4a48c7b97e3ef62fa2f60aa59)
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "start_time": start_time,
            }

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"]:
            '''The schedule start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-dailyschedule.html#cfn-inspectorv2-cisscanconfiguration-dailyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DailyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"day": "day", "start_time": "startTime"},
    )
    class MonthlyScheduleProperty:
        def __init__(
            self,
            *,
            day: builtins.str,
            start_time: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A monthly schedule.

            :param day: The monthly schedule's day.
            :param start_time: The monthly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                monthly_schedule_property = inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                    day="day",
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__100314319c9ea946d9251b6fcc3341b05bf63331e32e3a7f7aa894b6b8421861)
                check_type(argname="argument day", value=day, expected_type=type_hints["day"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "day": day,
                "start_time": start_time,
            }

        @builtins.property
        def day(self) -> builtins.str:
            '''The monthly schedule's day.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-day
            '''
            result = self._values.get("day")
            assert result is not None, "Required property 'day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"]:
            '''The monthly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-monthlyschedule.html#cfn-inspectorv2-cisscanconfiguration-monthlyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MonthlyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.ScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={
            "daily": "daily",
            "monthly": "monthly",
            "one_time": "oneTime",
            "weekly": "weekly",
        },
    )
    class ScheduleProperty:
        def __init__(
            self,
            *,
            daily: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.DailyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            monthly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.MonthlyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            one_time: typing.Any = None,
            weekly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.WeeklyScheduleProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''The schedule the CIS scan configuration runs on.

            Each CIS scan configuration has exactly one type of schedule.

            :param daily: A daily schedule.
            :param monthly: A monthly schedule.
            :param one_time: A one time schedule.
            :param weekly: A weekly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                # one_time: Any
                
                schedule_property = inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                    daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                        day="day",
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    one_time=one_time,
                    weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                        days=["days"],
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__db99f3a188203b64b30f42f8814cca36f1b859733833ecc2b25042b4eb91d395)
                check_type(argname="argument daily", value=daily, expected_type=type_hints["daily"])
                check_type(argname="argument monthly", value=monthly, expected_type=type_hints["monthly"])
                check_type(argname="argument one_time", value=one_time, expected_type=type_hints["one_time"])
                check_type(argname="argument weekly", value=weekly, expected_type=type_hints["weekly"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if daily is not None:
                self._values["daily"] = daily
            if monthly is not None:
                self._values["monthly"] = monthly
            if one_time is not None:
                self._values["one_time"] = one_time
            if weekly is not None:
                self._values["weekly"] = weekly

        @builtins.property
        def daily(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.DailyScheduleProperty"]]:
            '''A daily schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-daily
            '''
            result = self._values.get("daily")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.DailyScheduleProperty"]], result)

        @builtins.property
        def monthly(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.MonthlyScheduleProperty"]]:
            '''A monthly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-monthly
            '''
            result = self._values.get("monthly")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.MonthlyScheduleProperty"]], result)

        @builtins.property
        def one_time(self) -> typing.Any:
            '''A one time schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-onetime
            '''
            result = self._values.get("one_time")
            return typing.cast(typing.Any, result)

        @builtins.property
        def weekly(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.WeeklyScheduleProperty"]]:
            '''A weekly schedule.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-schedule.html#cfn-inspectorv2-cisscanconfiguration-schedule-weekly
            '''
            result = self._values.get("weekly")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.WeeklyScheduleProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "ScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.TimeProperty",
        jsii_struct_bases=[],
        name_mapping={"time_of_day": "timeOfDay", "time_zone": "timeZone"},
    )
    class TimeProperty:
        def __init__(
            self,
            *,
            time_of_day: builtins.str,
            time_zone: builtins.str,
        ) -> None:
            '''The time.

            :param time_of_day: The time of day in 24-hour format (00:00).
            :param time_zone: The timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                time_property = inspectorv2.CfnCisScanConfiguration.TimeProperty(
                    time_of_day="timeOfDay",
                    time_zone="timeZone"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__f2452dd795ce037d8e45e12f3b1e33517e2f22095c208d70f01cce9d97cc7f45)
                check_type(argname="argument time_of_day", value=time_of_day, expected_type=type_hints["time_of_day"])
                check_type(argname="argument time_zone", value=time_zone, expected_type=type_hints["time_zone"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "time_of_day": time_of_day,
                "time_zone": time_zone,
            }

        @builtins.property
        def time_of_day(self) -> builtins.str:
            '''The time of day in 24-hour format (00:00).

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html#cfn-inspectorv2-cisscanconfiguration-time-timeofday
            '''
            result = self._values.get("time_of_day")
            assert result is not None, "Required property 'time_of_day' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def time_zone(self) -> builtins.str:
            '''The timezone.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-time.html#cfn-inspectorv2-cisscanconfiguration-time-timezone
            '''
            result = self._values.get("time_zone")
            assert result is not None, "Required property 'time_zone' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "TimeProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty",
        jsii_struct_bases=[],
        name_mapping={"days": "days", "start_time": "startTime"},
    )
    class WeeklyScheduleProperty:
        def __init__(
            self,
            *,
            days: typing.Sequence[builtins.str],
            start_time: typing.Union[_IResolvable_da3f097b, typing.Union["CfnCisScanConfiguration.TimeProperty", typing.Dict[builtins.str, typing.Any]]],
        ) -> None:
            '''A weekly schedule.

            :param days: The weekly schedule's days.
            :param start_time: The weekly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                weekly_schedule_property = inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                    days=["days"],
                    start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                        time_of_day="timeOfDay",
                        time_zone="timeZone"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d30b6b9756e498926a5cf63c7bbf5e7f937d68b176005d1670779697c6b3abb4)
                check_type(argname="argument days", value=days, expected_type=type_hints["days"])
                check_type(argname="argument start_time", value=start_time, expected_type=type_hints["start_time"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "days": days,
                "start_time": start_time,
            }

        @builtins.property
        def days(self) -> typing.List[builtins.str]:
            '''The weekly schedule's days.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-days
            '''
            result = self._values.get("days")
            assert result is not None, "Required property 'days' is missing"
            return typing.cast(typing.List[builtins.str], result)

        @builtins.property
        def start_time(
            self,
        ) -> typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"]:
            '''The weekly schedule's start time.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-cisscanconfiguration-weeklyschedule.html#cfn-inspectorv2-cisscanconfiguration-weeklyschedule-starttime
            '''
            result = self._values.get("start_time")
            assert result is not None, "Required property 'start_time' is missing"
            return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnCisScanConfiguration.TimeProperty"], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "WeeklyScheduleProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnCisScanConfigurationProps",
    jsii_struct_bases=[],
    name_mapping={
        "scan_name": "scanName",
        "schedule": "schedule",
        "security_level": "securityLevel",
        "tags": "tags",
        "targets": "targets",
    },
)
class CfnCisScanConfigurationProps:
    def __init__(
        self,
        *,
        scan_name: typing.Optional[builtins.str] = None,
        schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
        security_level: typing.Optional[builtins.str] = None,
        tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.CisTargetsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    ) -> None:
        '''Properties for defining a ``CfnCisScanConfiguration``.

        :param scan_name: The name of the CIS scan configuration.
        :param schedule: The CIS scan configuration's schedule.
        :param security_level: The CIS scan configuration's CIS Benchmark level.
        :param tags: The CIS scan configuration's tags.
        :param targets: The CIS scan configuration's targets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            # one_time: Any
            
            cfn_cis_scan_configuration_props = inspectorv2.CfnCisScanConfigurationProps(
                scan_name="scanName",
                schedule=inspectorv2.CfnCisScanConfiguration.ScheduleProperty(
                    daily=inspectorv2.CfnCisScanConfiguration.DailyScheduleProperty(
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    monthly=inspectorv2.CfnCisScanConfiguration.MonthlyScheduleProperty(
                        day="day",
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    ),
                    one_time=one_time,
                    weekly=inspectorv2.CfnCisScanConfiguration.WeeklyScheduleProperty(
                        days=["days"],
                        start_time=inspectorv2.CfnCisScanConfiguration.TimeProperty(
                            time_of_day="timeOfDay",
                            time_zone="timeZone"
                        )
                    )
                ),
                security_level="securityLevel",
                tags={
                    "tags_key": "tags"
                },
                targets=inspectorv2.CfnCisScanConfiguration.CisTargetsProperty(
                    account_ids=["accountIds"],
            
                    # the properties below are optional
                    target_resource_tags={
                        "target_resource_tags_key": ["targetResourceTags"]
                    }
                )
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__e3f0430cb9cf97c73c0c85526ac298bc695a6c9d3bf5e578a6d9b5c85d5623dc)
            check_type(argname="argument scan_name", value=scan_name, expected_type=type_hints["scan_name"])
            check_type(argname="argument schedule", value=schedule, expected_type=type_hints["schedule"])
            check_type(argname="argument security_level", value=security_level, expected_type=type_hints["security_level"])
            check_type(argname="argument tags", value=tags, expected_type=type_hints["tags"])
            check_type(argname="argument targets", value=targets, expected_type=type_hints["targets"])
        self._values: typing.Dict[builtins.str, typing.Any] = {}
        if scan_name is not None:
            self._values["scan_name"] = scan_name
        if schedule is not None:
            self._values["schedule"] = schedule
        if security_level is not None:
            self._values["security_level"] = security_level
        if tags is not None:
            self._values["tags"] = tags
        if targets is not None:
            self._values["targets"] = targets

    @builtins.property
    def scan_name(self) -> typing.Optional[builtins.str]:
        '''The name of the CIS scan configuration.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-scanname
        '''
        result = self._values.get("scan_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schedule(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.ScheduleProperty]]:
        '''The CIS scan configuration's schedule.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-schedule
        '''
        result = self._values.get("schedule")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.ScheduleProperty]], result)

    @builtins.property
    def security_level(self) -> typing.Optional[builtins.str]:
        '''The CIS scan configuration's CIS Benchmark level.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-securitylevel
        '''
        result = self._values.get("security_level")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def tags(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The CIS scan configuration's tags.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-tags
        '''
        result = self._values.get("tags")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def targets(
        self,
    ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.CisTargetsProperty]]:
        '''The CIS scan configuration's targets.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-cisscanconfiguration.html#cfn-inspectorv2-cisscanconfiguration-targets
        '''
        result = self._values.get("targets")
        return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.CisTargetsProperty]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnCisScanConfigurationProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.implements(_IInspectable_c2943556)
class CfnFilter(
    _CfnResource_9df397a6,
    metaclass=jsii.JSIIMeta,
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter",
):
    '''Details about a filter.

    :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html
    :cloudformationResource: AWS::InspectorV2::Filter
    :exampleMetadata: fixture=_generated

    Example::

        # The code below shows an example of how to instantiate this type.
        # The values are placeholders you should change.
        from aws_cdk import aws_inspectorv2 as inspectorv2
        
        cfn_filter = inspectorv2.CfnFilter(self, "MyCfnFilter",
            filter_action="filterAction",
            filter_criteria=inspectorv2.CfnFilter.FilterCriteriaProperty(
                aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                    lower_inclusive=123,
                    upper_inclusive=123
                )],
                last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                    begin_inclusive=123,
                    end_inclusive=123
                )],
                related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                    comparison="comparison",
        
                    # the properties below are optional
                    key="key",
                    value="value"
                )],
                resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                severity=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                title=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )],
                vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )],
                vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                    architecture=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    ),
                    name=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    release=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    version=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )
                )]
            ),
            name="name",
        
            # the properties below are optional
            description="description"
        )
    '''

    def __init__(
        self,
        scope: _constructs_77d1e7e8.Construct,
        id: builtins.str,
        *,
        filter_action: builtins.str,
        filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.FilterCriteriaProperty", typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param scope: Scope in which this resource is defined.
        :param id: Construct identifier for this resource (unique in its scope).
        :param filter_action: The action that is to be applied to the findings that match the filter.
        :param filter_criteria: Details on the filter criteria associated with this filter.
        :param name: The name of the filter.
        :param description: A description of the filter.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__76aaac8f8d755716225a5dd2d4902f3e7ec007381fa82a2d163553362c975c9d)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
        props = CfnFilterProps(
            filter_action=filter_action,
            filter_criteria=filter_criteria,
            name=name,
            description=description,
        )

        jsii.create(self.__class__, self, [scope, id, props])

    @jsii.member(jsii_name="inspect")
    def inspect(self, inspector: _TreeInspector_488e0dd5) -> None:
        '''Examines the CloudFormation resource and discloses attributes.

        :param inspector: tree inspector to collect and process attributes.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__daeca541bed43f62727b37c4048db034533d9b1614725f3cf4c361b77df5323e)
            check_type(argname="argument inspector", value=inspector, expected_type=type_hints["inspector"])
        return typing.cast(None, jsii.invoke(self, "inspect", [inspector]))

    @jsii.member(jsii_name="renderProperties")
    def _render_properties(
        self,
        props: typing.Mapping[builtins.str, typing.Any],
    ) -> typing.Mapping[builtins.str, typing.Any]:
        '''
        :param props: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__02055b54b230012a61c4a22e04d2fc0ffa08a47a06385a880a1db32a3f55f237)
            check_type(argname="argument props", value=props, expected_type=type_hints["props"])
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "renderProperties", [props]))

    @jsii.python.classproperty
    @jsii.member(jsii_name="CFN_RESOURCE_TYPE_NAME")
    def CFN_RESOURCE_TYPE_NAME(cls) -> builtins.str:
        '''The CloudFormation resource type name for this resource class.'''
        return typing.cast(builtins.str, jsii.sget(cls, "CFN_RESOURCE_TYPE_NAME"))

    @builtins.property
    @jsii.member(jsii_name="attrArn")
    def attr_arn(self) -> builtins.str:
        '''The Amazon Resource Number (ARN) associated with this filter.

        :cloudformationAttribute: Arn
        '''
        return typing.cast(builtins.str, jsii.get(self, "attrArn"))

    @builtins.property
    @jsii.member(jsii_name="cfnProperties")
    def _cfn_properties(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.get(self, "cfnProperties"))

    @builtins.property
    @jsii.member(jsii_name="filterAction")
    def filter_action(self) -> builtins.str:
        '''The action that is to be applied to the findings that match the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "filterAction"))

    @filter_action.setter
    def filter_action(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__a72dbbaedc7eb8a3b6da0867d3f429993d1cdfe3b095a514d2cb82730c01b31d)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterAction", value)

    @builtins.property
    @jsii.member(jsii_name="filterCriteria")
    def filter_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, "CfnFilter.FilterCriteriaProperty"]:
        '''Details on the filter criteria associated with this filter.'''
        return typing.cast(typing.Union[_IResolvable_da3f097b, "CfnFilter.FilterCriteriaProperty"], jsii.get(self, "filterCriteria"))

    @filter_criteria.setter
    def filter_criteria(
        self,
        value: typing.Union[_IResolvable_da3f097b, "CfnFilter.FilterCriteriaProperty"],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__b566081cfe458076187f61e1afab9cbbb5fb2cdd114aad2fa6e38280867325e5)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "filterCriteria", value)

    @builtins.property
    @jsii.member(jsii_name="name")
    def name(self) -> builtins.str:
        '''The name of the filter.'''
        return typing.cast(builtins.str, jsii.get(self, "name"))

    @name.setter
    def name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__1b0548c4926be9ebf2a0675883b51af78c4f6a9c034f4d0fb7a9ebfd7ad038ee)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "name", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the filter.'''
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "description"))

    @description.setter
    def description(self, value: typing.Optional[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__29a0d69128962a2d8d478ff9197ec92d930e2284a9cbff6337d95fb1932925d0)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.DateFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "end_inclusive": "endInclusive",
            "start_inclusive": "startInclusive",
        },
    )
    class DateFilterProperty:
        def __init__(
            self,
            *,
            end_inclusive: typing.Optional[jsii.Number] = None,
            start_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''Contains details on the time range used to filter findings.

            :param end_inclusive: A timestamp representing the end of the time period filtered on.
            :param start_inclusive: A timestamp representing the start of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                date_filter_property = inspectorv2.CfnFilter.DateFilterProperty(
                    end_inclusive=123,
                    start_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__412cca739fbade26efa876445772a168ea693eb111b9385ae83d92127bd547b5)
                check_type(argname="argument end_inclusive", value=end_inclusive, expected_type=type_hints["end_inclusive"])
                check_type(argname="argument start_inclusive", value=start_inclusive, expected_type=type_hints["start_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if end_inclusive is not None:
                self._values["end_inclusive"] = end_inclusive
            if start_inclusive is not None:
                self._values["start_inclusive"] = start_inclusive

        @builtins.property
        def end_inclusive(self) -> typing.Optional[jsii.Number]:
            '''A timestamp representing the end of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-endinclusive
            '''
            result = self._values.get("end_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def start_inclusive(self) -> typing.Optional[jsii.Number]:
            '''A timestamp representing the start of the time period filtered on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-datefilter.html#cfn-inspectorv2-filter-datefilter-startinclusive
            '''
            result = self._values.get("start_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "DateFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.FilterCriteriaProperty",
        jsii_struct_bases=[],
        name_mapping={
            "aws_account_id": "awsAccountId",
            "component_id": "componentId",
            "component_type": "componentType",
            "ec2_instance_image_id": "ec2InstanceImageId",
            "ec2_instance_subnet_id": "ec2InstanceSubnetId",
            "ec2_instance_vpc_id": "ec2InstanceVpcId",
            "ecr_image_architecture": "ecrImageArchitecture",
            "ecr_image_hash": "ecrImageHash",
            "ecr_image_pushed_at": "ecrImagePushedAt",
            "ecr_image_registry": "ecrImageRegistry",
            "ecr_image_repository_name": "ecrImageRepositoryName",
            "ecr_image_tags": "ecrImageTags",
            "finding_arn": "findingArn",
            "finding_status": "findingStatus",
            "finding_type": "findingType",
            "first_observed_at": "firstObservedAt",
            "inspector_score": "inspectorScore",
            "last_observed_at": "lastObservedAt",
            "network_protocol": "networkProtocol",
            "port_range": "portRange",
            "related_vulnerabilities": "relatedVulnerabilities",
            "resource_id": "resourceId",
            "resource_tags": "resourceTags",
            "resource_type": "resourceType",
            "severity": "severity",
            "title": "title",
            "updated_at": "updatedAt",
            "vendor_severity": "vendorSeverity",
            "vulnerability_id": "vulnerabilityId",
            "vulnerability_source": "vulnerabilitySource",
            "vulnerable_packages": "vulnerablePackages",
        },
    )
    class FilterCriteriaProperty:
        def __init__(
            self,
            *,
            aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            component_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_subnet_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ec2_instance_vpc_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_pushed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_repository_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            ecr_image_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            finding_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            inspector_score: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            network_protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.PortRangeFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            related_vulnerabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.MapFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.DateFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vendor_severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerability_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerability_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
            vulnerable_packages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.PackageFilterProperty", typing.Dict[builtins.str, typing.Any]]]]]] = None,
        ) -> None:
            '''Details on the criteria used to define the filter.

            :param aws_account_id: Details of the AWS account IDs used to filter findings.
            :param component_id: Details of the component IDs used to filter findings.
            :param component_type: Details of the component types used to filter findings.
            :param ec2_instance_image_id: Details of the Amazon EC2 instance image IDs used to filter findings.
            :param ec2_instance_subnet_id: Details of the Amazon EC2 instance subnet IDs used to filter findings.
            :param ec2_instance_vpc_id: Details of the Amazon EC2 instance VPC IDs used to filter findings.
            :param ecr_image_architecture: Details of the Amazon ECR image architecture types used to filter findings.
            :param ecr_image_hash: Details of the Amazon ECR image hashes used to filter findings.
            :param ecr_image_pushed_at: Details on the Amazon ECR image push date and time used to filter findings.
            :param ecr_image_registry: Details on the Amazon ECR registry used to filter findings.
            :param ecr_image_repository_name: Details on the name of the Amazon ECR repository used to filter findings.
            :param ecr_image_tags: The tags attached to the Amazon ECR container image.
            :param finding_arn: Details on the finding ARNs used to filter findings.
            :param finding_status: Details on the finding status types used to filter findings.
            :param finding_type: Details on the finding types used to filter findings.
            :param first_observed_at: Details on the date and time a finding was first seen used to filter findings.
            :param inspector_score: The Amazon Inspector score to filter on.
            :param last_observed_at: Details on the date and time a finding was last seen used to filter findings.
            :param network_protocol: Details on network protocol used to filter findings.
            :param port_range: Details on the port ranges used to filter findings.
            :param related_vulnerabilities: Details on the related vulnerabilities used to filter findings.
            :param resource_id: Details on the resource IDs used to filter findings.
            :param resource_tags: Details on the resource tags used to filter findings.
            :param resource_type: Details on the resource types used to filter findings.
            :param severity: Details on the severity used to filter findings.
            :param title: Details on the finding title used to filter findings.
            :param updated_at: Details on the date and time a finding was last updated at used to filter findings.
            :param vendor_severity: Details on the vendor severity used to filter findings.
            :param vulnerability_id: Details on the vulnerability ID used to filter findings.
            :param vulnerability_source: Details on the vulnerability score to filter findings by.
            :param vulnerable_packages: Details on the vulnerable packages used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                filter_criteria_property = inspectorv2.CfnFilter.FilterCriteriaProperty(
                    aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                        begin_inclusive=123,
                        end_inclusive=123
                    )],
                    related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                        comparison="comparison",
                
                        # the properties below are optional
                        key="key",
                        value="value"
                    )],
                    resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                        architecture=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                            lower_inclusive=123,
                            upper_inclusive=123
                        ),
                        name=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        release=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        version=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        )
                    )]
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__8bf898b4c669bfc838bf91c83d3735a9d69065b37baef35430be61dc52e3c81a)
                check_type(argname="argument aws_account_id", value=aws_account_id, expected_type=type_hints["aws_account_id"])
                check_type(argname="argument component_id", value=component_id, expected_type=type_hints["component_id"])
                check_type(argname="argument component_type", value=component_type, expected_type=type_hints["component_type"])
                check_type(argname="argument ec2_instance_image_id", value=ec2_instance_image_id, expected_type=type_hints["ec2_instance_image_id"])
                check_type(argname="argument ec2_instance_subnet_id", value=ec2_instance_subnet_id, expected_type=type_hints["ec2_instance_subnet_id"])
                check_type(argname="argument ec2_instance_vpc_id", value=ec2_instance_vpc_id, expected_type=type_hints["ec2_instance_vpc_id"])
                check_type(argname="argument ecr_image_architecture", value=ecr_image_architecture, expected_type=type_hints["ecr_image_architecture"])
                check_type(argname="argument ecr_image_hash", value=ecr_image_hash, expected_type=type_hints["ecr_image_hash"])
                check_type(argname="argument ecr_image_pushed_at", value=ecr_image_pushed_at, expected_type=type_hints["ecr_image_pushed_at"])
                check_type(argname="argument ecr_image_registry", value=ecr_image_registry, expected_type=type_hints["ecr_image_registry"])
                check_type(argname="argument ecr_image_repository_name", value=ecr_image_repository_name, expected_type=type_hints["ecr_image_repository_name"])
                check_type(argname="argument ecr_image_tags", value=ecr_image_tags, expected_type=type_hints["ecr_image_tags"])
                check_type(argname="argument finding_arn", value=finding_arn, expected_type=type_hints["finding_arn"])
                check_type(argname="argument finding_status", value=finding_status, expected_type=type_hints["finding_status"])
                check_type(argname="argument finding_type", value=finding_type, expected_type=type_hints["finding_type"])
                check_type(argname="argument first_observed_at", value=first_observed_at, expected_type=type_hints["first_observed_at"])
                check_type(argname="argument inspector_score", value=inspector_score, expected_type=type_hints["inspector_score"])
                check_type(argname="argument last_observed_at", value=last_observed_at, expected_type=type_hints["last_observed_at"])
                check_type(argname="argument network_protocol", value=network_protocol, expected_type=type_hints["network_protocol"])
                check_type(argname="argument port_range", value=port_range, expected_type=type_hints["port_range"])
                check_type(argname="argument related_vulnerabilities", value=related_vulnerabilities, expected_type=type_hints["related_vulnerabilities"])
                check_type(argname="argument resource_id", value=resource_id, expected_type=type_hints["resource_id"])
                check_type(argname="argument resource_tags", value=resource_tags, expected_type=type_hints["resource_tags"])
                check_type(argname="argument resource_type", value=resource_type, expected_type=type_hints["resource_type"])
                check_type(argname="argument severity", value=severity, expected_type=type_hints["severity"])
                check_type(argname="argument title", value=title, expected_type=type_hints["title"])
                check_type(argname="argument updated_at", value=updated_at, expected_type=type_hints["updated_at"])
                check_type(argname="argument vendor_severity", value=vendor_severity, expected_type=type_hints["vendor_severity"])
                check_type(argname="argument vulnerability_id", value=vulnerability_id, expected_type=type_hints["vulnerability_id"])
                check_type(argname="argument vulnerability_source", value=vulnerability_source, expected_type=type_hints["vulnerability_source"])
                check_type(argname="argument vulnerable_packages", value=vulnerable_packages, expected_type=type_hints["vulnerable_packages"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if aws_account_id is not None:
                self._values["aws_account_id"] = aws_account_id
            if component_id is not None:
                self._values["component_id"] = component_id
            if component_type is not None:
                self._values["component_type"] = component_type
            if ec2_instance_image_id is not None:
                self._values["ec2_instance_image_id"] = ec2_instance_image_id
            if ec2_instance_subnet_id is not None:
                self._values["ec2_instance_subnet_id"] = ec2_instance_subnet_id
            if ec2_instance_vpc_id is not None:
                self._values["ec2_instance_vpc_id"] = ec2_instance_vpc_id
            if ecr_image_architecture is not None:
                self._values["ecr_image_architecture"] = ecr_image_architecture
            if ecr_image_hash is not None:
                self._values["ecr_image_hash"] = ecr_image_hash
            if ecr_image_pushed_at is not None:
                self._values["ecr_image_pushed_at"] = ecr_image_pushed_at
            if ecr_image_registry is not None:
                self._values["ecr_image_registry"] = ecr_image_registry
            if ecr_image_repository_name is not None:
                self._values["ecr_image_repository_name"] = ecr_image_repository_name
            if ecr_image_tags is not None:
                self._values["ecr_image_tags"] = ecr_image_tags
            if finding_arn is not None:
                self._values["finding_arn"] = finding_arn
            if finding_status is not None:
                self._values["finding_status"] = finding_status
            if finding_type is not None:
                self._values["finding_type"] = finding_type
            if first_observed_at is not None:
                self._values["first_observed_at"] = first_observed_at
            if inspector_score is not None:
                self._values["inspector_score"] = inspector_score
            if last_observed_at is not None:
                self._values["last_observed_at"] = last_observed_at
            if network_protocol is not None:
                self._values["network_protocol"] = network_protocol
            if port_range is not None:
                self._values["port_range"] = port_range
            if related_vulnerabilities is not None:
                self._values["related_vulnerabilities"] = related_vulnerabilities
            if resource_id is not None:
                self._values["resource_id"] = resource_id
            if resource_tags is not None:
                self._values["resource_tags"] = resource_tags
            if resource_type is not None:
                self._values["resource_type"] = resource_type
            if severity is not None:
                self._values["severity"] = severity
            if title is not None:
                self._values["title"] = title
            if updated_at is not None:
                self._values["updated_at"] = updated_at
            if vendor_severity is not None:
                self._values["vendor_severity"] = vendor_severity
            if vulnerability_id is not None:
                self._values["vulnerability_id"] = vulnerability_id
            if vulnerability_source is not None:
                self._values["vulnerability_source"] = vulnerability_source
            if vulnerable_packages is not None:
                self._values["vulnerable_packages"] = vulnerable_packages

        @builtins.property
        def aws_account_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the AWS account IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-awsaccountid
            '''
            result = self._values.get("aws_account_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def component_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the component IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componentid
            '''
            result = self._values.get("component_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def component_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the component types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-componenttype
            '''
            result = self._values.get("component_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_image_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance image IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instanceimageid
            '''
            result = self._values.get("ec2_instance_image_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_subnet_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance subnet IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancesubnetid
            '''
            result = self._values.get("ec2_instance_subnet_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ec2_instance_vpc_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon EC2 instance VPC IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ec2instancevpcid
            '''
            result = self._values.get("ec2_instance_vpc_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_architecture(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon ECR image architecture types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagearchitecture
            '''
            result = self._values.get("ecr_image_architecture")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_hash(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details of the Amazon ECR image hashes used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagehash
            '''
            result = self._values.get("ecr_image_hash")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_pushed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the Amazon ECR image push date and time used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagepushedat
            '''
            result = self._values.get("ecr_image_pushed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_registry(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the Amazon ECR registry used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimageregistry
            '''
            result = self._values.get("ecr_image_registry")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_repository_name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the name of the Amazon ECR repository used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagerepositoryname
            '''
            result = self._values.get("ecr_image_repository_name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def ecr_image_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''The tags attached to the Amazon ECR container image.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-ecrimagetags
            '''
            result = self._values.get("ecr_image_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_arn(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding ARNs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingarn
            '''
            result = self._values.get("finding_arn")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_status(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding status types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingstatus
            '''
            result = self._values.get("finding_status")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def finding_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-findingtype
            '''
            result = self._values.get("finding_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def first_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was first seen used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-firstobservedat
            '''
            result = self._values.get("first_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def inspector_score(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.NumberFilterProperty"]]]]:
            '''The Amazon Inspector score to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-inspectorscore
            '''
            result = self._values.get("inspector_score")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.NumberFilterProperty"]]]], result)

        @builtins.property
        def last_observed_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was last seen used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-lastobservedat
            '''
            result = self._values.get("last_observed_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def network_protocol(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on network protocol used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-networkprotocol
            '''
            result = self._values.get("network_protocol")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def port_range(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.PortRangeFilterProperty"]]]]:
            '''Details on the port ranges used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-portrange
            '''
            result = self._values.get("port_range")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.PortRangeFilterProperty"]]]], result)

        @builtins.property
        def related_vulnerabilities(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the related vulnerabilities used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-relatedvulnerabilities
            '''
            result = self._values.get("related_vulnerabilities")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the resource IDs used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourceid
            '''
            result = self._values.get("resource_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def resource_tags(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.MapFilterProperty"]]]]:
            '''Details on the resource tags used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetags
            '''
            result = self._values.get("resource_tags")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.MapFilterProperty"]]]], result)

        @builtins.property
        def resource_type(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the resource types used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-resourcetype
            '''
            result = self._values.get("resource_type")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def severity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the severity used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-severity
            '''
            result = self._values.get("severity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def title(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the finding title used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-title
            '''
            result = self._values.get("title")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def updated_at(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]]:
            '''Details on the date and time a finding was last updated at used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-updatedat
            '''
            result = self._values.get("updated_at")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.DateFilterProperty"]]]], result)

        @builtins.property
        def vendor_severity(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vendor severity used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vendorseverity
            '''
            result = self._values.get("vendor_severity")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerability_id(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vulnerability ID used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilityid
            '''
            result = self._values.get("vulnerability_id")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerability_source(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]]:
            '''Details on the vulnerability score to filter findings by.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerabilitysource
            '''
            result = self._values.get("vulnerability_source")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]]], result)

        @builtins.property
        def vulnerable_packages(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.PackageFilterProperty"]]]]:
            '''Details on the vulnerable packages used to filter findings.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-filtercriteria.html#cfn-inspectorv2-filter-filtercriteria-vulnerablepackages
            '''
            result = self._values.get("vulnerable_packages")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, typing.List[typing.Union[_IResolvable_da3f097b, "CfnFilter.PackageFilterProperty"]]]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "FilterCriteriaProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.MapFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "key": "key", "value": "value"},
    )
    class MapFilterProperty:
        def __init__(
            self,
            *,
            comparison: builtins.str,
            key: typing.Optional[builtins.str] = None,
            value: typing.Optional[builtins.str] = None,
        ) -> None:
            '''An object that describes details of a map filter.

            :param comparison: The operator to use when comparing values in the filter.
            :param key: The tag key used in the filter.
            :param value: The tag value used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                map_filter_property = inspectorv2.CfnFilter.MapFilterProperty(
                    comparison="comparison",
                
                    # the properties below are optional
                    key="key",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__009bff3f64987bf2b6fbf83e6b34fdd47b0110d9ba805cb04cf145bbb5b29475)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument key", value=key, expected_type=type_hints["key"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
            }
            if key is not None:
                self._values["key"] = key
            if value is not None:
                self._values["value"] = value

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The operator to use when comparing values in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def key(self) -> typing.Optional[builtins.str]:
            '''The tag key used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-key
            '''
            result = self._values.get("key")
            return typing.cast(typing.Optional[builtins.str], result)

        @builtins.property
        def value(self) -> typing.Optional[builtins.str]:
            '''The tag value used in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-mapfilter.html#cfn-inspectorv2-filter-mapfilter-value
            '''
            result = self._values.get("value")
            return typing.cast(typing.Optional[builtins.str], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "MapFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.NumberFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "lower_inclusive": "lowerInclusive",
            "upper_inclusive": "upperInclusive",
        },
    )
    class NumberFilterProperty:
        def __init__(
            self,
            *,
            lower_inclusive: typing.Optional[jsii.Number] = None,
            upper_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that describes the details of a number filter.

            :param lower_inclusive: The lowest number to be included in the filter.
            :param upper_inclusive: The highest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                number_filter_property = inspectorv2.CfnFilter.NumberFilterProperty(
                    lower_inclusive=123,
                    upper_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__b6efc9c4516b1a3e22589ec1e26597252a4352fc85020ac641e71757b7752878)
                check_type(argname="argument lower_inclusive", value=lower_inclusive, expected_type=type_hints["lower_inclusive"])
                check_type(argname="argument upper_inclusive", value=upper_inclusive, expected_type=type_hints["upper_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if lower_inclusive is not None:
                self._values["lower_inclusive"] = lower_inclusive
            if upper_inclusive is not None:
                self._values["upper_inclusive"] = upper_inclusive

        @builtins.property
        def lower_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The lowest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-lowerinclusive
            '''
            result = self._values.get("lower_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def upper_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The highest number to be included in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-numberfilter.html#cfn-inspectorv2-filter-numberfilter-upperinclusive
            '''
            result = self._values.get("upper_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "NumberFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.PackageFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "architecture": "architecture",
            "epoch": "epoch",
            "name": "name",
            "release": "release",
            "source_layer_hash": "sourceLayerHash",
            "version": "version",
        },
    )
    class PackageFilterProperty:
        def __init__(
            self,
            *,
            architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            epoch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.NumberFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            release: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            source_layer_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
            version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union["CfnFilter.StringFilterProperty", typing.Dict[builtins.str, typing.Any]]]] = None,
        ) -> None:
            '''Contains information on the details of a package filter.

            :param architecture: An object that contains details on the package architecture type to filter on.
            :param epoch: An object that contains details on the package epoch to filter on.
            :param name: An object that contains details on the name of the package to filter on.
            :param release: An object that contains details on the package release to filter on.
            :param source_layer_hash: An object that contains details on the source layer hash to filter on.
            :param version: The package version to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                package_filter_property = inspectorv2.CfnFilter.PackageFilterProperty(
                    architecture=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    ),
                    name=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    release=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    ),
                    version=inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__1bffc1f427079a7381e5366b9fd38ff4f23a9a2d0463f6c7f0250a60e1c3aa65)
                check_type(argname="argument architecture", value=architecture, expected_type=type_hints["architecture"])
                check_type(argname="argument epoch", value=epoch, expected_type=type_hints["epoch"])
                check_type(argname="argument name", value=name, expected_type=type_hints["name"])
                check_type(argname="argument release", value=release, expected_type=type_hints["release"])
                check_type(argname="argument source_layer_hash", value=source_layer_hash, expected_type=type_hints["source_layer_hash"])
                check_type(argname="argument version", value=version, expected_type=type_hints["version"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if architecture is not None:
                self._values["architecture"] = architecture
            if epoch is not None:
                self._values["epoch"] = epoch
            if name is not None:
                self._values["name"] = name
            if release is not None:
                self._values["release"] = release
            if source_layer_hash is not None:
                self._values["source_layer_hash"] = source_layer_hash
            if version is not None:
                self._values["version"] = version

        @builtins.property
        def architecture(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the package architecture type to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-architecture
            '''
            result = self._values.get("architecture")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def epoch(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.NumberFilterProperty"]]:
            '''An object that contains details on the package epoch to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-epoch
            '''
            result = self._values.get("epoch")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.NumberFilterProperty"]], result)

        @builtins.property
        def name(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the name of the package to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-name
            '''
            result = self._values.get("name")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def release(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the package release to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-release
            '''
            result = self._values.get("release")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def source_layer_hash(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]:
            '''An object that contains details on the source layer hash to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-sourcelayerhash
            '''
            result = self._values.get("source_layer_hash")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]], result)

        @builtins.property
        def version(
            self,
        ) -> typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]]:
            '''The package version to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-packagefilter.html#cfn-inspectorv2-filter-packagefilter-version
            '''
            result = self._values.get("version")
            return typing.cast(typing.Optional[typing.Union[_IResolvable_da3f097b, "CfnFilter.StringFilterProperty"]], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PackageFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.PortRangeFilterProperty",
        jsii_struct_bases=[],
        name_mapping={
            "begin_inclusive": "beginInclusive",
            "end_inclusive": "endInclusive",
        },
    )
    class PortRangeFilterProperty:
        def __init__(
            self,
            *,
            begin_inclusive: typing.Optional[jsii.Number] = None,
            end_inclusive: typing.Optional[jsii.Number] = None,
        ) -> None:
            '''An object that describes the details of a port range filter.

            :param begin_inclusive: The port number the port range begins at.
            :param end_inclusive: The port number the port range ends at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                port_range_filter_property = inspectorv2.CfnFilter.PortRangeFilterProperty(
                    begin_inclusive=123,
                    end_inclusive=123
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__57f27af64057bdc90d805dc1f14192e3d6ecef8b43899ee7e276ad4a39443097)
                check_type(argname="argument begin_inclusive", value=begin_inclusive, expected_type=type_hints["begin_inclusive"])
                check_type(argname="argument end_inclusive", value=end_inclusive, expected_type=type_hints["end_inclusive"])
            self._values: typing.Dict[builtins.str, typing.Any] = {}
            if begin_inclusive is not None:
                self._values["begin_inclusive"] = begin_inclusive
            if end_inclusive is not None:
                self._values["end_inclusive"] = end_inclusive

        @builtins.property
        def begin_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The port number the port range begins at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-begininclusive
            '''
            result = self._values.get("begin_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        @builtins.property
        def end_inclusive(self) -> typing.Optional[jsii.Number]:
            '''The port number the port range ends at.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-portrangefilter.html#cfn-inspectorv2-filter-portrangefilter-endinclusive
            '''
            result = self._values.get("end_inclusive")
            return typing.cast(typing.Optional[jsii.Number], result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "PortRangeFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )

    @jsii.data_type(
        jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilter.StringFilterProperty",
        jsii_struct_bases=[],
        name_mapping={"comparison": "comparison", "value": "value"},
    )
    class StringFilterProperty:
        def __init__(self, *, comparison: builtins.str, value: builtins.str) -> None:
            '''An object that describes the details of a string filter.

            :param comparison: The operator to use when comparing values in the filter.
            :param value: The value to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html
            :exampleMetadata: fixture=_generated

            Example::

                # The code below shows an example of how to instantiate this type.
                # The values are placeholders you should change.
                from aws_cdk import aws_inspectorv2 as inspectorv2
                
                string_filter_property = inspectorv2.CfnFilter.StringFilterProperty(
                    comparison="comparison",
                    value="value"
                )
            '''
            if __debug__:
                type_hints = typing.get_type_hints(_typecheckingstub__d081b1255c15164560e59790e612b8f1e2382868fcbfff794be0ca61435dbce0)
                check_type(argname="argument comparison", value=comparison, expected_type=type_hints["comparison"])
                check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            self._values: typing.Dict[builtins.str, typing.Any] = {
                "comparison": comparison,
                "value": value,
            }

        @builtins.property
        def comparison(self) -> builtins.str:
            '''The operator to use when comparing values in the filter.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-comparison
            '''
            result = self._values.get("comparison")
            assert result is not None, "Required property 'comparison' is missing"
            return typing.cast(builtins.str, result)

        @builtins.property
        def value(self) -> builtins.str:
            '''The value to filter on.

            :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-inspectorv2-filter-stringfilter.html#cfn-inspectorv2-filter-stringfilter-value
            '''
            result = self._values.get("value")
            assert result is not None, "Required property 'value' is missing"
            return typing.cast(builtins.str, result)

        def __eq__(self, rhs: typing.Any) -> builtins.bool:
            return isinstance(rhs, self.__class__) and rhs._values == self._values

        def __ne__(self, rhs: typing.Any) -> builtins.bool:
            return not (rhs == self)

        def __repr__(self) -> str:
            return "StringFilterProperty(%s)" % ", ".join(
                k + "=" + repr(v) for k, v in self._values.items()
            )


@jsii.data_type(
    jsii_type="aws-cdk-lib.aws_inspectorv2.CfnFilterProps",
    jsii_struct_bases=[],
    name_mapping={
        "filter_action": "filterAction",
        "filter_criteria": "filterCriteria",
        "name": "name",
        "description": "description",
    },
)
class CfnFilterProps:
    def __init__(
        self,
        *,
        filter_action: builtins.str,
        filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
        name: builtins.str,
        description: typing.Optional[builtins.str] = None,
    ) -> None:
        '''Properties for defining a ``CfnFilter``.

        :param filter_action: The action that is to be applied to the findings that match the filter.
        :param filter_criteria: Details on the filter criteria associated with this filter.
        :param name: The name of the filter.
        :param description: A description of the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html
        :exampleMetadata: fixture=_generated

        Example::

            # The code below shows an example of how to instantiate this type.
            # The values are placeholders you should change.
            from aws_cdk import aws_inspectorv2 as inspectorv2
            
            cfn_filter_props = inspectorv2.CfnFilterProps(
                filter_action="filterAction",
                filter_criteria=inspectorv2.CfnFilter.FilterCriteriaProperty(
                    aws_account_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    component_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_image_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_subnet_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ec2_instance_vpc_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_architecture=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_hash=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_pushed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    ecr_image_registry=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_repository_name=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    ecr_image_tags=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_arn=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_status=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    finding_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    first_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    inspector_score=[inspectorv2.CfnFilter.NumberFilterProperty(
                        lower_inclusive=123,
                        upper_inclusive=123
                    )],
                    last_observed_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    network_protocol=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    port_range=[inspectorv2.CfnFilter.PortRangeFilterProperty(
                        begin_inclusive=123,
                        end_inclusive=123
                    )],
                    related_vulnerabilities=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    resource_tags=[inspectorv2.CfnFilter.MapFilterProperty(
                        comparison="comparison",
            
                        # the properties below are optional
                        key="key",
                        value="value"
                    )],
                    resource_type=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    title=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    updated_at=[inspectorv2.CfnFilter.DateFilterProperty(
                        end_inclusive=123,
                        start_inclusive=123
                    )],
                    vendor_severity=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_id=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerability_source=[inspectorv2.CfnFilter.StringFilterProperty(
                        comparison="comparison",
                        value="value"
                    )],
                    vulnerable_packages=[inspectorv2.CfnFilter.PackageFilterProperty(
                        architecture=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        epoch=inspectorv2.CfnFilter.NumberFilterProperty(
                            lower_inclusive=123,
                            upper_inclusive=123
                        ),
                        name=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        release=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        source_layer_hash=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        ),
                        version=inspectorv2.CfnFilter.StringFilterProperty(
                            comparison="comparison",
                            value="value"
                        )
                    )]
                ),
                name="name",
            
                # the properties below are optional
                description="description"
            )
        '''
        if __debug__:
            type_hints = typing.get_type_hints(_typecheckingstub__701269c3a3c8675419393e41eacb02f94675d9b8c43500c7ae0bd7ea72e3129f)
            check_type(argname="argument filter_action", value=filter_action, expected_type=type_hints["filter_action"])
            check_type(argname="argument filter_criteria", value=filter_criteria, expected_type=type_hints["filter_criteria"])
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
        self._values: typing.Dict[builtins.str, typing.Any] = {
            "filter_action": filter_action,
            "filter_criteria": filter_criteria,
            "name": name,
        }
        if description is not None:
            self._values["description"] = description

    @builtins.property
    def filter_action(self) -> builtins.str:
        '''The action that is to be applied to the findings that match the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filteraction
        '''
        result = self._values.get("filter_action")
        assert result is not None, "Required property 'filter_action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def filter_criteria(
        self,
    ) -> typing.Union[_IResolvable_da3f097b, CfnFilter.FilterCriteriaProperty]:
        '''Details on the filter criteria associated with this filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-filtercriteria
        '''
        result = self._values.get("filter_criteria")
        assert result is not None, "Required property 'filter_criteria' is missing"
        return typing.cast(typing.Union[_IResolvable_da3f097b, CfnFilter.FilterCriteriaProperty], result)

    @builtins.property
    def name(self) -> builtins.str:
        '''The name of the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-name
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''A description of the filter.

        :see: http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-inspectorv2-filter.html#cfn-inspectorv2-filter-description
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "CfnFilterProps(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


__all__ = [
    "CfnCisScanConfiguration",
    "CfnCisScanConfigurationProps",
    "CfnFilter",
    "CfnFilterProps",
]

publication.publish()

def _typecheckingstub__ee74cd979e0690afc5238694387a2bb443783c172f8af7544b4b5c468df80b9c(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    scan_name: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_level: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.CisTargetsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1c340cf5a8052b5b5d1021305af92e23dcb4f62645a1014b0a49bb031d376ee8(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daf01f89651352328420f5a52535d8376706a979b3cb022464732eddc33e94c8(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8f6f074ec34751eb6d66964ee6738d096c1429db3564cba2005e530e659871bc(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__17c38c82086f8ffe9712e88585d2f980663e72bbb5b6ac70574594200cb759c2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.ScheduleProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__53a976b81d95f07052322a80e8b1ff546ae083bdb3cb3d358b91e5b7e50b0909(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__5b4e1fac23c27cbc692267473e4cf9258b43062b9aea2a43b116dcfb105adb0d(
    value: typing.Optional[typing.Mapping[builtins.str, builtins.str]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8afffccf2a9a470f423d247abd4a6dfe735dc39c53a2abe26c8cdb1844ec12a2(
    value: typing.Optional[typing.Union[_IResolvable_da3f097b, CfnCisScanConfiguration.CisTargetsProperty]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__48b07d123221faefb49073a28736f1aec9dc2a488247f39ec213274809cd3b6a(
    *,
    account_ids: typing.Sequence[builtins.str],
    target_resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Mapping[builtins.str, typing.Sequence[builtins.str]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__bd3a6a48de82a0a7da55bb17cc5099cc069382b4a48c7b97e3ef62fa2f60aa59(
    *,
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__100314319c9ea946d9251b6fcc3341b05bf63331e32e3a7f7aa894b6b8421861(
    *,
    day: builtins.str,
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__db99f3a188203b64b30f42f8814cca36f1b859733833ecc2b25042b4eb91d395(
    *,
    daily: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.DailyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    monthly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.MonthlyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    one_time: typing.Any = None,
    weekly: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.WeeklyScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__f2452dd795ce037d8e45e12f3b1e33517e2f22095c208d70f01cce9d97cc7f45(
    *,
    time_of_day: builtins.str,
    time_zone: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d30b6b9756e498926a5cf63c7bbf5e7f937d68b176005d1670779697c6b3abb4(
    *,
    days: typing.Sequence[builtins.str],
    start_time: typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.TimeProperty, typing.Dict[builtins.str, typing.Any]]],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__e3f0430cb9cf97c73c0c85526ac298bc695a6c9d3bf5e578a6d9b5c85d5623dc(
    *,
    scan_name: typing.Optional[builtins.str] = None,
    schedule: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.ScheduleProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    security_level: typing.Optional[builtins.str] = None,
    tags: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    targets: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnCisScanConfiguration.CisTargetsProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__76aaac8f8d755716225a5dd2d4902f3e7ec007381fa82a2d163553362c975c9d(
    scope: _constructs_77d1e7e8.Construct,
    id: builtins.str,
    *,
    filter_action: builtins.str,
    filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__daeca541bed43f62727b37c4048db034533d9b1614725f3cf4c361b77df5323e(
    inspector: _TreeInspector_488e0dd5,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__02055b54b230012a61c4a22e04d2fc0ffa08a47a06385a880a1db32a3f55f237(
    props: typing.Mapping[builtins.str, typing.Any],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__a72dbbaedc7eb8a3b6da0867d3f429993d1cdfe3b095a514d2cb82730c01b31d(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b566081cfe458076187f61e1afab9cbbb5fb2cdd114aad2fa6e38280867325e5(
    value: typing.Union[_IResolvable_da3f097b, CfnFilter.FilterCriteriaProperty],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1b0548c4926be9ebf2a0675883b51af78c4f6a9c034f4d0fb7a9ebfd7ad038ee(
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__29a0d69128962a2d8d478ff9197ec92d930e2284a9cbff6337d95fb1932925d0(
    value: typing.Optional[builtins.str],
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__412cca739fbade26efa876445772a168ea693eb111b9385ae83d92127bd547b5(
    *,
    end_inclusive: typing.Optional[jsii.Number] = None,
    start_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__8bf898b4c669bfc838bf91c83d3735a9d69065b37baef35430be61dc52e3c81a(
    *,
    aws_account_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    component_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_image_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_subnet_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ec2_instance_vpc_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_pushed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_registry: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_repository_name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    ecr_image_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_arn: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_status: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    finding_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    first_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    inspector_score: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    last_observed_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    network_protocol: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    port_range: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.PortRangeFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    related_vulnerabilities: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_tags: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.MapFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    resource_type: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    title: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    updated_at: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.DateFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vendor_severity: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerability_id: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerability_source: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
    vulnerable_packages: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Sequence[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.PackageFilterProperty, typing.Dict[builtins.str, typing.Any]]]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__009bff3f64987bf2b6fbf83e6b34fdd47b0110d9ba805cb04cf145bbb5b29475(
    *,
    comparison: builtins.str,
    key: typing.Optional[builtins.str] = None,
    value: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__b6efc9c4516b1a3e22589ec1e26597252a4352fc85020ac641e71757b7752878(
    *,
    lower_inclusive: typing.Optional[jsii.Number] = None,
    upper_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__1bffc1f427079a7381e5366b9fd38ff4f23a9a2d0463f6c7f0250a60e1c3aa65(
    *,
    architecture: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    epoch: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.NumberFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    name: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    release: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    source_layer_hash: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
    version: typing.Optional[typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.StringFilterProperty, typing.Dict[builtins.str, typing.Any]]]] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__57f27af64057bdc90d805dc1f14192e3d6ecef8b43899ee7e276ad4a39443097(
    *,
    begin_inclusive: typing.Optional[jsii.Number] = None,
    end_inclusive: typing.Optional[jsii.Number] = None,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__d081b1255c15164560e59790e612b8f1e2382868fcbfff794be0ca61435dbce0(
    *,
    comparison: builtins.str,
    value: builtins.str,
) -> None:
    """Type checking stubs"""
    pass

def _typecheckingstub__701269c3a3c8675419393e41eacb02f94675d9b8c43500c7ae0bd7ea72e3129f(
    *,
    filter_action: builtins.str,
    filter_criteria: typing.Union[_IResolvable_da3f097b, typing.Union[CfnFilter.FilterCriteriaProperty, typing.Dict[builtins.str, typing.Any]]],
    name: builtins.str,
    description: typing.Optional[builtins.str] = None,
) -> None:
    """Type checking stubs"""
    pass