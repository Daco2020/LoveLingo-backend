from httpx import AsyncClient


async def test_root(async_client: AsyncClient):
    # when
    res = await async_client.get("/v1/lovelingos/")

    # then
    assert res.status_code == 200
    assert res.json()["message"] == "Hello World"
