from dataclasses import dataclass


@dataclass
class Position:
    id: int
    name: str
    category: str


@dataclass
class Employer:
    id: int
    first_name: str
    last_name: str
    patronymic: str
    gender: str
    age: int
    position: Position


@dataclass
class NewEmployer:
    id: int
    first_name: str
    last_name: str
    patronymic: str
    gender: str
    age: int
    position_id: int
