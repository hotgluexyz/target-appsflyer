"""AppsFlyer target sink class, which handles writing streams."""


from target_appsflyer.client import AppsFlyerSink


class EventsSink(AppsFlyerSink):
    """AppsFlyer target sink class."""
    name = "Events"
    endpoint = "/inappevent"

    def preprocess_record(self, record: dict, context: dict) -> dict:
        self.endpoint = f"{self.endpoint}/{self.config.get('app_id')}"
        return record
