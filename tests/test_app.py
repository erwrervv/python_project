from app import create_app


def test_index():
    app = create_app({"TESTING": True})
    client = app.test_client()
    rv = client.get("/")
    assert rv.status_code == 200
    # Ensure HTML contains the expected message
    text = rv.get_data(as_text=True)
    assert "Hello, Flask!" in text
