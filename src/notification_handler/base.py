from abc import ABC, abstractmethod
from typing import Dict


class NotificationChannel(ABC):

    @abstractmethod
    def send_notification(self, request: Dict) -> None:
        pass