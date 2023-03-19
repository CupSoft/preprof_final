from pydantic import BaseModel


class DayPD(BaseModel):
    num: int | None
    current_sh: int | None
    current_power: int | None
    current_oxi: int | None
    use_power: int | None
    use_oxi: int | None
    distribution_engine: int | None
    distribution_autoclave: int | None


class PointPD(BaseModel):
    day: int | None
    current_power: int | None
    current_oxi: int | None


class AlgoResultPD(BaseModel):
    days: list[DayPD]
    points: list[PointPD]
