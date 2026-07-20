from playwright.sync_api import sync_playwright


with sync_playwright() as p:

    browser = p.chromium.launch(
        headless=False
    )

    page = browser.new_page()

    page.goto(
        "https://www.betano.bet.br/live/",
        timeout=60000
    )


    page.wait_for_timeout(8000)


    texto = page.locator(
        "body"
    ).inner_text()


    linhas = [
        x.strip()
        for x in texto.split("\n")
        if x.strip()
    ]


    for i, linha in enumerate(linhas[:80]):

        print(
            i,
            "=>",
            linha
        )


    browser.close()