from os import environ

from dotenv import load_dotenv

from playwright.async_api import async_playwright

from src.utilities.scrap_data import ScrapData


load_dotenv()


class WebScrapping:
    def __init__(self):
        load_dotenv()
        self.site_espn = environ["SOCCER_RANK"]

    async def brazilian_soccer_championship_ranking(self, year):
        try:
            espn = self.site_espn.format(year=year)

            async with (async_playwright() as p):
                browser = await p.chromium.launch(headless=True)

                page = await browser.new_page()

                await page.goto(espn)

                await page.wait_for_timeout(5000)

                # teams names
                teams = await page.locator(
                    "div.ResponsiveTable.ResponsiveTable--fixed-left"
                ).locator(
                    "div.flex"
                ).locator(
                    "table.Table.Table--align-right.Table--fixed.Table--fixed-left"
                ).locator(
                    "tbody.Table__TBODY"
                ).inner_text()

                teams = teams.split("\n\n\n")

                # numeric information
                classify = await page.locator(
                    "div.ResponsiveTable.ResponsiveTable--fixed-left"
                ).locator(
                    "div.flex"
                ).locator(
                    "div.Table__ScrollerWrapper.relative.overflow-hidden"
                ).locator("div.Table__Scroller").locator("table.Table.Table--align-right").locator(
                    "tbody.Table__TBODY"
                ).inner_text()

                classify = classify.split("\n\n\n")

            teams_pos = await ScrapData.get_teams_positions_and_names(teams)
            ranking = await ScrapData.get_teams_data_ranking(classify)

            return teams_pos, ranking
        except Exception as e:
            raise Exception(e.args[0].message)
