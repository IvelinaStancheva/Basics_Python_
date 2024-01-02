from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    BASE_OXY = 120

    def __init__(self, name: str):
        super().__init__(name, self.BASE_OXY)

    def miss(self, time_to_catch):
        self.oxygen_level = max(round(self.oxygen_level - time_to_catch * 0.6), 0)

    def renew_oxy(self):
        self.oxygen_level = self.BASE_OXY