from point_class import Point
import pytest

"""
We would like to be able to create a Point object.
A Point is defined by two attributes: Latitude and Longitude.
Constraints: 
- A non empty city name
- A latitude is between -90 and 90
- A longitude is between -180 and 180

"""

def test_make_point():
    p = Point("Doha", 14.445, 19.988)
    assert p is not None
    assert p.get_laitude() == 14.445
    assert p.get_longitude() == 19.988

def test_make_point_with_invalid_coordinates():
    with pytest.raises(ValueError) as e:
        Point("Anywhere", 92.22,100.22)
    assert str(e.value) == "Invalid latitude, longitude"

    with pytest.raises(ValueError) as e:
        Point("Anywhere", 92.22,40.22)
    assert str(e.value) == "Invalid latitude, longitude"

    with pytest.raises(ValueError) as e:
        Point("Anywhere", 20.53,192.22)
    assert str(e.value) == "Invalid latitude, longitude"

    with pytest.raises(ValueError) as e:
        Point("", 20.53,40.22)
    assert str(e.value) == "City name must be specified"



