from __future__ import annotations

import os

from pydantic import BaseModel
from target_hotglue.auth import ApiAuthenticator
from target_hotglue.client import HotglueSink
import requests
from singer_sdk.exceptions import FatalAPIError, RetriableAPIError
import requests


class AppsFlyerSink(HotglueSink):
    method = "POST"
    def get_http_headers(self):
        headers = {}
        
        headers["authentication"] = str(
            self.config.get("api_key")
        )
        headers["Content-Type"] = "application/json"
        return headers

    @property
    def base_url(self) -> str:
        return "https://api2.appsflyer.com"
    
    def validate_response(self, response: requests.Response) -> None:
        """Validate HTTP response."""
        if response.status_code in [429] or 500 <= response.status_code < 600:
            msg = self.response_error_message(response)
            error = {"status_code": response.status_code, "body":response.text}
            raise RetriableAPIError(error)
        elif 400 <= response.status_code < 500:
            try:
                msg = response.text
            except:
                msg = self.response_error_message(response)
            error = {"status_code": response.status_code, "body":msg}
            raise FatalAPIError(error)

    def log_request_response(self, record, response):
        self.logger.info(f"Sending payload for stream {self.name}: {record}")
        self.logger.info(f"Response: {response.text}")    

    def upsert_record(self, record: dict, context: dict):
        id = None
        state_updates = dict()
        response = self.request_api(self.method,self.endpoint,request_data=record,headers=self.get_http_headers())
        self.log_request_response(record, response)
        if response.status_code in [200]:
            state_updates["success"] = True
            
        elif response.status_code == 400:
            state_updates["success"] = False
            state_updates["error"] = response.text
        return id, response.ok, state_updates    
