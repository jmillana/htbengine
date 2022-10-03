"""HTB machine model."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime

logger = logging.getLogger(__name__)

STATUS = ["active", "retired"]


class BOOL_ATTRS:
    """List the boolean attributes of the machine."""

    OWNED = "owned"
    SPAWNED = "spawned"
    FREE = "free"


@dataclass
class FeedbackChart:
    """Represents the feedback charts on HTB machines."""

    counterCake: int
    counterVeryEasy: int
    counterEasy: int
    counterTooEasy: int
    counterMedium: int
    counterBitHard: int
    counterHard: int
    counterTooHard: int
    counterExHard: int
    counterBrainFuck: int


@dataclass
class PlayInfo:
    """Representa the player information on the HTB machines."""

    isSpawned: bool | None = None
    isSpawning: bool | None = None
    isActive: bool | None = None
    active_player_count: int | None = None
    expires_at: datetime | None = None


@dataclass
class Maker:
    """Represents the authors of the HTB machines."""

    id: int
    name: str
    avatar: str
    isRespected: bool


@dataclass
class Tag:
    """Represents the tags on the HTB machines."""

    id: int
    tag_category_id: int


@dataclass
class HTBMachine:
    """Represents the information that any HTB machine have."""

    id: int | str
    name: str
    avatar: str
    ip: str
    os: str
    points: int | str
    static_points: int | str
    release: datetime | str
    difficulty: int | str
    difficultyText: str
    feedbackForChart: FeedbackChart
    playInfo: PlayInfo
    stars: float | str
    user_owns_count: int | str
    root_owns_count: int | str
    authUserHasReviewed: bool | str
    isTodo: bool | str
    easy_month: int | str
    sp_flag: int | str
    recommended: int | str
    authUserInUserOwns: bool | None | str
    authUserInRootOwns: bool | None | str
    free: bool | str
    maker: Maker
    maker2: Maker | None = None
    tags: list[Tag] = field(default_factory=list)
    active: bool | str = False
