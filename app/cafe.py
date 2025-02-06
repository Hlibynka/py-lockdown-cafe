import datetime
from app.errors import (NotVaccinatedError,
                        OutdatedVaccineError,
                        NotWearingMaskError)


class Cafe:
    def __init__(self, name: str) -> None:
        self.name = name

    def visit_cafe(self, visitor: dict) -> str:
        """Checks if a visitor meets the pandemic restrictions."""
        if "vaccine" not in visitor:
            raise NotVaccinatedError("Visitor invaccine error")

        if visitor["vaccine"]["expiration_date"] < datetime.date.today():
            raise OutdatedVaccineError("Visitor's invaccine outdated error")

        if not visitor.get("wearing_a_mask", False):
            raise NotWearingMaskError("Mask wearing error")

        return f"Welcome to {self.name}"
