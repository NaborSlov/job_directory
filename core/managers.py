from typing import List, Optional

from django.db import connection

from core.dataclass import Position, Employer, NewEmployer


class PositionManager:
    def all(self) -> List[Position]:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM core_position""")
            rows = cursor.fetchall()
            results = [Position(*row) for row in rows]

        return results

    def create(self, name, category) -> Position:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            INSERT INTO core_position (name, category)
            VALUES '{name}', '{category}'
            RETURNING *;""")
            row = cursor.fetchone()
            return Position(*row) if row else None

    def get_by_pk(self, pk) -> Optional[Position]:
        with connection.cursor() as cursor:
            cursor.execute(f"""SELECT * FROM core_position WHERE id = '{pk}'""")
            row = cursor.fetchone()
            return Position(*row) if row else None

    def update(self, pk, name: str = None, category: str = None) -> Optional[Position]:
        fields = {'name': name,
                  'category': category}
        set_fields = build_fields(fields)

        with connection.cursor() as cursor:
            cursor.execute(f"""
            UPDATE core_position
            SET {set_fields}
            WHERE id = '{pk}'
            RETURNING *;""")

            row = cursor.fetchone()
            result = Position(*row) if row else None

        return result

    def delete(self, pk) -> None:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            UPDATE core_employer
            SET position_id = NULL
            WHERE  position_id = '{pk}'
            """)
            cursor.execute(f"""
            DELETE FROM core_position
            WHERE id = '{pk}'
            """)


class EmployerManager:
    def all(self) -> List[Employer]:
        with connection.cursor() as cursor:
            cursor.execute(
                """SELECT * FROM core_employer as ce 
                LEFT JOIN core_position as cp ON ce.position_id = cp.id""")
            rows = cursor.fetchall()

        results = []
        for row in rows:
            position = Position(*row[-3:])
            results.append(Employer(*row[:-4], position=position))

        return results

    def create(self,
               first_name: str,
               last_name: str,
               patronymic: str,
               gender: str,
               age: int,
               position_id: int) -> Optional[NewEmployer]:
        with connection.cursor() as cursor:
            cursor.execute(
                f"""INSERT INTO core_employer (first_name, last_name, patronymic, gender, age, position_id)
                VALUES '{first_name}', '{last_name}', '{patronymic}', '{gender}', '{age}', '{position_id}'
                RETURNING *;""",
                )

            row = cursor.fetchone()

        return NewEmployer(*row) if row else None

    def get_by_pk(self, pk: int) -> Optional[Employer]:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            SELECT * FROM core_employer as ce
            JOIN core_position as cp ON ce.position_id = cp.id
            WHERE ce.id = '{pk}';
            """)

            row = cursor.fetchone()
            position = Position(*row[-3:])
            employer = Employer(*row[:-4], position=position)

        return employer

    def update(self,
               pk: int,
               first_name: str = None,
               last_name: str = None,
               patronymic: str = None,
               gender: str = None,
               age: int = None,
               position_id: int = None) -> Optional[Employer]:
        fields = {'first_name': first_name,
                  'last_name': last_name,
                  'patronymic': patronymic,
                  'gender': gender,
                  'age': age,
                  'position_id': position_id}
        set_fields = build_fields(fields)

        with connection.cursor() as cursor:
            cursor.execute(f"""
            UPDATE core_employer
            SET {set_fields}
            WHERE id = '{pk}'
            RETURNING *;""")

            row = cursor.fetchone()
            result = NewEmployer(*row) if row else None

        return result

    def delete(self, pk) -> None:
        with connection.cursor() as cursor:
            cursor.execute(f"""
            DELETE FROM core_employer
            WHERE id = '{pk}';
            """)


def build_fields(fields: dict) -> str:
    fields = {k: v for k, v in fields.items() if v is not None}
    result = ", ".join([f"{k} = '{v}'" for k, v in fields.items()])
    return result