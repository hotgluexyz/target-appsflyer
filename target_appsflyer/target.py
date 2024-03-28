"""AppsFlyer target class."""

from target_hotglue.target import TargetHotglue
from singer_sdk import typing as th

from target_appsflyer.sinks import (
    EventsSink,
)


class TargetAppsFlyer(TargetHotglue):
    """Sample target for AppsFlyer."""
    SINK_TYPES = [
        EventsSink,
    ]
    name = "target-appsflyer"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True
        ),
        th.Property(
            "app_id",
            th.StringType,
            required=True
        ),
    ).to_dict()

if __name__ == '__main__':
    TargetAppsFlyer.cli()
