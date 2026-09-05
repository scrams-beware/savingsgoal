# === Stage 2: Add dataclasses or typed dictionaries for the main domain records ===
# Project: SavingsGoal
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime
from decimal import Decimal

@dataclass
class Contribution:
    id: str = field(default_factory=lambda: f"contrib_{datetime.now():%Y%m%d%H%M%S}")
    date: date = field(default_factory=date.today)
    amount: Decimal = Decimal("0.00")
    note: str = ""
    category: str = ""

@dataclass
class Milestone:
    id: str = field(default_factory=lambda: f"mile_{datetime.now():%Y%m%d%H%M%S}")
    title: str = ""
    target_amount: Decimal = Decimal("0.00")
    achieved_date: date | None = None
    achieved_amount: Decimal = Decimal("0.00")
    description: str = ""

@dataclass
class SavingsGoal:
    id: str = field(default_factory=lambda: f"goal_{datetime.now():%Y%m%d%H%M%S}")
    name: str = ""
    target_amount: Decimal = Decimal("0.00")
    current_amount: Decimal = Decimal("0.00")
    start_date: date = field(default_factory=date.today)
    contributions: list[Contribution] = field(default_factory=list)
    milestones: list[Milestone] = field(default_factory=list)
    created_at: datetime = field(default_factory=datetime.now)

    @property
    def remaining(self) -> Decimal:
        return self.target_amount - self.current_amount

    @property
    def progress_pct(self) -> float:
        if self.target_amount == Decimal("0.00"):
            return 0.0
        return float(self.current_amount / self.target_amount * 100)
