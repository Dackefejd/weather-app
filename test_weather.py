from weather import get_weather

def test_api_status_code():
    # API testing - Stockholm (lat 59.3, lon 18.0)
    response = get_weather(59.3, 18.0)

    # checking for status: 200
    assert response.status_code == 200