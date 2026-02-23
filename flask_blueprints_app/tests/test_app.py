from app import create_app


def test_home_page_returns_200():
    app = create_app()
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_blog_post_detail_returns_200():
    app = create_app()
    client = app.test_client()

    response = client.get("/blog/1")

    assert response.status_code == 200


def test_api_health_returns_ok_json():
    app = create_app()
    client = app.test_client()

    response = client.get("/api/health")

    assert response.status_code == 200
    assert response.is_json
    assert response.get_json() == {"status": "ok"}
