import data
import sender_stand_request

def get_kit_body(name):
    current_kit_name = data.new_kit.copy()
    current_kit_name["name"] = name
    return current_kit_name


def get_kit_body_without_name():
    current_kit_name = data.new_kit.copy()
    current_kit_name.pop("name", None)
    return current_kit_name


def positive_assert(name):
    kit_body = get_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()["name"] == name


def negative_assert(name):
    kit_body = get_kit_body(name) if name is not None else get_kit_body_without_name()
    kit_response = sender_stand_request.post_new_client_kit(kit_body)
    assert kit_response.status_code == 400



def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def test_create_kit_511_letter_in_name_get_success_response():
        positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_special_character_in_name_get_success_response():
    positive_assert("№%@")

def test_create_kit_spaces_in_name_get_success_response():
    positive_assert("A Aaa ")

def test_create_kit_numbers_in_name_get_success_response():
    positive_assert("123")

def test_create_user_0_letter_get_error_response():
    negative_assert("")

def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_different_parameter_in_name_get_error_response():
    negative_assert(123)

def test_create_user_no_name_get_error_response():
    negative_assert(None)