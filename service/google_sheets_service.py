# gspread api reference: https://docs.gspread.org/en/latest/api/index.html

from gspread.utils import ValueRenderOption


async def test(google_service):
    worksheet = google_service.open("Fiat Lux Trophies").worksheet("Extreme Trials (ARR)")
    cells = worksheet.batch_get(['C2', 'D2', 'A2'], value_render_option=ValueRenderOption.formatted)

    print("return_str = [\"" + cells[0][0][0] + "\", \"" + cells[1][0][0] + "\", \"" + cells[2][0][0] + "\"]")

    return [cells[0][0][0], cells[1][0][0], cells[2][0][0]]

