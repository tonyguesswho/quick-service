import json


def test_add_order(test_app, test_database, add_service):
    service = add_service(name="House Cleaning", duration=60)
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2090-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 201
    assert "service request was created successfully" in data["message"]
    assert data["data"]["service_id"] == service.id


def test_add_order_invalid_email(test_app, test_database, add_service):
    service = add_service(name="House Cleaning", duration=60)
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "testtest.com",
                "service_id": service.id,
                "request_date": "2090-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Invalid email" in data["message"]


def test_add_order_invalid_service(test_app, test_database, add_service):
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": 999,
                "request_date": "2090-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Service ID is invalid" in data["message"]


def test_add_order_invalid_work_time(test_app, test_database, add_service):
    service = add_service(name="House Cleaning", duration=60)
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2090-11-10T07:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert (
        "Order can only be placed between 9 am and after 5 pm Monday - Saturday"
        in data["message"]
    )


def test_add_order_invalid_date(test_app, test_database, add_service):
    service = add_service(name="House Cleaning", duration=60)
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2000-11-10T07:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Order can only be placed in a future date/time." in data["message"]


def test_add_order_invalid_holiday(test_app, test_database, add_service, add_holiday):
    service = add_service(name="House Cleaning", duration=60)
    add_holiday(name="My day", date="2021-11-10T07:10:21.524485Z")
    client = test_app.test_client()
    resp = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2021-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data = json.loads(resp.data.decode())
    assert resp.status_code == 400
    assert "Order cannot be placed on a holiday." in data["message"]


def test_add_order_invalid_slot(test_app, test_database, add_service):
    service = add_service(name="House Cleaning", duration=60)
    client = test_app.test_client()
    resp_1 = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2090-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    resp_2 = client.post(
        "/orders",
        data=json.dumps(
            {
                "email": "test@test.com",
                "service_id": service.id,
                "request_date": "2090-11-10T09:10:21.524485Z",
            }
        ),
        content_type="application/json",
    )
    data_1 = json.loads(resp_1.data.decode())
    data_2 = json.loads(resp_2.data.decode())
    assert resp_1.status_code == 201
    assert "service request was created successfully" in data_1["message"]
    assert data_1["data"]["service_id"] == service.id
    assert resp_2.status_code == 400
    assert "Slot is not available" in data_2["message"]
