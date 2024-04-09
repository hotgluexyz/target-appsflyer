"""AppsFlyer target sink class, which handles writing streams."""


from target_appsflyer.client import AppsFlyerSink


class EventsSink(AppsFlyerSink):
    """AppsFlyer target sink class."""
    name = "Events"
    endpoint = "/inappevent/{app_id}"

    def preprocess_record(self, record: dict, context: dict) -> dict:
        self.endpoint = self.endpoint.format(app_id=self.config.get('app_id'))
        return record
