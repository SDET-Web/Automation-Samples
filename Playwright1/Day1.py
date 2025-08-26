""" Synchronous API (Blocking)
Runs sequentially, one step at a time.
Easier to read and debug. Used without async functions.
Quick scripts, debugging, when async isn’t needed."""

from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("http://yahoo.com")
    print(page.title())
    #page.screenshot(path="example.png")
    browser.close()

""" Asynchronous API (Non-blocking)
Runs multiple tasks concurrently.
Uses async/await for better performance in large tests.
Requires async functions and asyncio.
Best for: Large-scale tests, parallel execution, performance-critical tasks 
Web scraping, automation, handling multiple users """

import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto("http://playwright.dev")
        print(await page.title())
        await browser.close()

asyncio.run(main())