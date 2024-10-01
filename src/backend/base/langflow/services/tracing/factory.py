from typing import TYPE_CHECKING

from langflow.services.factory import ServiceFactory
from langflow.services.tracing.service import TracingService

if TYPE_CHECKING:
    from langflow.services.settings.service import SettingsService


class TracingServiceFactory(ServiceFactory):
    def __init__(self):
        super().__init__(TracingService)

    def create(self, settings_service: "SettingsService"):
        return TracingService(settings_service)