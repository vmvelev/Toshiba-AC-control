# Copyright 2022 Kamil Sroka

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from dataclasses import dataclass
from datetime import datetime
from enum import Enum, auto


@dataclass(frozen=True)
class ToshibaAcDeviceEnergyConsumption:
    energy_wh: float
    since: datetime


@dataclass(frozen=True)
class ToshibaAcDeviceEnergyConsumptionBucket:
    """Hourly energy use for one hour of the day (API Time field is 1-24)."""

    hour: int
    energy_wh: float


@dataclass(frozen=True)
class ToshibaAcDeviceDailyEnergyConsumption:
    """Per-hour energy consumption for a single calendar day."""

    since: datetime
    buckets: tuple[ToshibaAcDeviceEnergyConsumptionBucket, ...]

    @property
    def total_energy_wh(self) -> float:
        return sum(bucket.energy_wh for bucket in self.buckets)

    def energy_wh_for_hour(self, hour: int) -> float | None:
        """Return energy for API hour bucket (1-24)."""
        for bucket in self.buckets:
            if bucket.hour == hour:
                return bucket.energy_wh
        return None

    @property
    def current_hour_energy_wh(self) -> float | None:
        """Energy consumed in the current hour of day, if data is for today."""
        now = datetime.now(tz=self.since.tzinfo)
        if now.date() != self.since.date():
            return None
        return self.energy_wh_for_hour(now.hour + 1)


class ToshibaAcStatus(Enum):
    ON = auto()
    OFF = auto()
    NONE = None


class ToshibaAcMode(Enum):
    AUTO = auto()
    COOL = auto()
    HEAT = auto()
    DRY = auto()
    FAN = auto()
    NONE = None


class ToshibaAcFanMode(Enum):
    AUTO = auto()
    QUIET = auto()
    LOW = auto()
    MEDIUM_LOW = auto()
    MEDIUM = auto()
    MEDIUM_HIGH = auto()
    HIGH = auto()
    NONE = None


class ToshibaAcSwingMode(Enum):
    OFF = auto()
    SWING_VERTICAL = auto()
    SWING_HORIZONTAL = auto()
    SWING_VERTICAL_AND_HORIZONTAL = auto()
    FIXED_1 = auto()
    FIXED_2 = auto()
    FIXED_3 = auto()
    FIXED_4 = auto()
    FIXED_5 = auto()
    NONE = None


class ToshibaAcPowerSelection(Enum):
    POWER_50 = auto()
    POWER_75 = auto()
    POWER_100 = auto()
    NONE = None


class ToshibaAcMeritB(Enum):
    FIREPLACE_1 = auto()
    FIREPLACE_2 = auto()
    OFF = auto()
    NONE = None


class ToshibaAcMeritA(Enum):
    HIGH_POWER = auto()
    CDU_SILENT_1 = auto()
    ECO = auto()
    HEATING_8C = auto()
    SLEEP_CARE = auto()
    FLOOR = auto()
    COMFORT = auto()
    CDU_SILENT_2 = auto()
    OFF = auto()
    NONE = None


class ToshibaAcAirPureIon(Enum):
    OFF = auto()
    ON = auto()
    NONE = None


class ToshibaAcSelfCleaning(Enum):
    ON = auto()
    OFF = auto()
    NONE = None
