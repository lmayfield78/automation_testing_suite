import requests
from constants import API_ENDPOINTS

# All tests are based on the following endpoint:
# https://automationexercise.com/


def test_get_all_products():
    """
    This test will get all products from the API and verify that the response is a list of products,
    and that the number of products is correct. Note: Though the last ID is 43
    in actuallity there are only 34 products.
    """
    url = f"{API_ENDPOINTS['BASE_URL']}{API_ENDPOINTS['all_products']}"
    response = requests.get(url)  # <-- This is the GET request
    assert response.status_code == 200
    data = response.json()
    assert "products" in data, "The key 'products' is missing in the response"
    products = data["products"]
    assert isinstance(products, list), "Products data is not a list"
    for product in products:
        assert "id" in product, "Product is missing 'id'"
        assert "name" in product, "Product is missing 'name'"
        assert "brand" in product, "Product is missing 'brand'"
        assert "category" in product, "Product is missing 'category'"

    assert len(products) == 34, f"Expected 34 products, got {len(products)}"


def test_unsupported_product_post_call():
    """
    This test will call the /api/productsList endpoint with an unsupported
    post request method and verify that the response is an error message.
    """
    url = f"{API_ENDPOINTS['BASE_URL']}{API_ENDPOINTS['all_products']}"
    response = requests.post(url)  # <-- This is the POST request
    data = response.json()
    assert (
        response.status_code == 200
    ), f"Unexpected status code: {response.status_code}"
    assert (
        data["responseCode"] == 405
    ), "Expected application-level status 405, got {data['responseCode']}"
    assert "message" in data, "Expected error message in the response"
    assert (
        data["message"] == "This request method is not supported."
    ), "Incorrect error message"
