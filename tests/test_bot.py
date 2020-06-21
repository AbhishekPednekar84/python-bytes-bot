import os
import requests
import dotenv
import bot_server

dotenv.load_dotenv()

token = os.getenv("TELEGRAM_TOKEN")


def test_telegram_get_updates(requests_mock):
    requests_mock.get(
        f"https://api.telegram.org/bot{token}/getUpdates", json={"kw": "flask"}
    )
    assert {"kw": "flask"} == requests.get(
        f"https://api.telegram.org/bot{token}/getUpdates"
    ).json()


def test_tp_search_api_single_word(requests_mock):
    requests_mock.get(
        "https://search.pythonbytes.fm/api/search?q=treebeard",
        json={"kw": "treebeard"},
    )
    assert {"kw": "treebeard"} == requests.get(
        "https://search.pythonbytes.fm/api/search?q=treebeard"
    ).json()


def test_tp_search_api_multi_word(requests_mock):
    requests_mock.get(
        "https://search.pythonbytes.fm/api/search?q=jupyter-binder",
        json={"kw": "jupyter-binder"},
    )
    assert {"kw": "jupyter-binder"} == requests.get(
        "https://search.pythonbytes.fm/api/search?q=jupyter-binder"
    ).json()


def test_tp_search_api_special_character(requests_mock):
    requests_mock.get(
        "https://search.pythonbytes.fm/api/search?q=jupyter%binder+nbinteract",
        json={"kw": "jupyter-binder-nbinteract"},
    )
    assert {"kw": "jupyter-binder-nbinteract"} == requests.get(
        "https://search.pythonbytes.fm/api/search?q=jupyter%binder+nbinteract"
    ).json()


def test_make_reply():
    result = bot_server.make_reply("thexfiles!@@", "test")
    assert (
        result
        == "Sorry! I did not find anything for <strong><em>thexfiles!@@</em></strong> 😓"
    )
