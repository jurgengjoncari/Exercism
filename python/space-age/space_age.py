class SpaceAge:
    orbital_periods = {
        "Earth": 1.0,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132
    }

    def __init__(self, seconds):
        self.seconds = seconds
    def on_planet(self, orbital_period):
        return round(self.seconds / 31557600 / orbital_period, 2)
    def on_earth(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Earth"])
    def on_mercury(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Mercury"])
    def on_venus(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Venus"])
    def on_mars(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Mars"])
    def on_jupiter(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Jupiter"])
    def on_saturn(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Saturn"])
    def on_uranus(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Uranus"])
    def on_neptune(self):
        return SpaceAge.on_planet(self, SpaceAge.orbital_periods["Neptune"])