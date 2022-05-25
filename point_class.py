class Point():
    def __init__(self, name,latitude, longitude):
        self.name = name
        if not ( -90 <= latitude <= 90 ) or not (-180 <= longitude <= 180):
            raise ValueError("Invalid latitude, longitude")
        if name == "":
            raise ValueError("City name must be specified")
        self.latitude = latitude
        self.longitude = longitude

    def get_laitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude