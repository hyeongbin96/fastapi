# fastapi에서 비동기 프로그래밍을 구현하는 코드 예씨
from fastapi import FastAPI
import httpx
import asyncio

app = FastAPI()


async def get_remote_data(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        return response.json()


@app.get("/data")
async def read_data():
    external_data = await get_remote_data("https://naver.com")
    return external_data


# 비동기 처리 테스트 코드
import asyncio
import random


async def async_func(task_id: int, delay: int):
    print(f"Task {task_id}: {delay}초 대기 후 실행")
    await asyncio.sleep(delay)
    print(f"Task {task_id}: 완료되었습니다.")


async def main():
    tasks = []
    for i in range(1, 6):  # 총 5개의 작업 생성
        random_delay = random.randint(1, 10)  # 각 작업마다 랜덤 대기 시간 설정
        tasks.append(async_func(i, random_delay))

    await asyncio.gather(*tasks)  # 모든 작업을 동시에 실행


asyncio.run(main())
