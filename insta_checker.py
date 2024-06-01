import aiohttp
import asyncio

async def check_username_availability(session, username):
    url = f"https://www.instagram.com/{username}/"
    async with session.get(url) as response:
        if response.status == 404:
            return f"Username '{username}' is $$$."
        else:
            return f"Username '{username}' is taken."

async def main():
    # Read usernames from a text file
    with open("usernames.txt", "r") as file:
        usernames = file.read().splitlines()

    async with aiohttp.ClientSession() as session:
        tasks = []
        for username in usernames:
            tasks.append(check_username_availability(session, username))
        
        # Run all tasks concurrently and wait for them to complete
        results = await asyncio.gather(*tasks)
        
        for result in results:
            print(result)

if __name__ == "__main__":
    asyncio.run(main())
