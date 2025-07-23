import asyncio
import time

async def brew_coffee():
    print("Starting to brew coffee...")
    await asyncio.sleep(3)  # Simulating a 3-minute coffee brewing time
    print("Coffee is ready!")


async def toast_bread():
    print("Starting to toast bread...")
    await asyncio.sleep(2)  # Simulating a 2-minute bread toasting time
    print("Bread is toasted!")


async def main():
    start = time.time()

    # Run both tasks concurrently
    await asyncio.gather(
        brew_coffee(),
        toast_bread()
    )

    end = time.time()

    print(f"\nTotal time taken: {end - start:.2f} Minutes")

asyncio.run(main())