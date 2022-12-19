from PIL import Image, ImageDraw, ImageFont


def create_image(home, away, time):
    width = 1620
    height = 2700

    font_tips = ImageFont.truetype("Arial_Black.ttf", size=100)
    font_time = ImageFont.truetype("Arial_Black.ttf", size=65)

    canvas = Image.new("RGB", (width, height))
    draw = ImageDraw.Draw(canvas)

    background = Image.open("photos/background.eps")
    background.load(scale=2)
    canvas.paste(background)

    draw.text((630, 0), time, fill=(255, 255, 255), font=font_time)
    draw.text((310, 70), "1X", fill=(255, 255, 255), font=font_tips)
    draw.text((620, 70), "X", fill=(255, 255, 255), font=font_tips)
    draw.text((850, 70), "X2", fill=(255, 255, 255), font=font_tips)
    draw.text((1090, 70), "12", fill=(255, 255, 255), font=font_tips)

    home_pic = Image.open(f"photos/{home}.eps")
    away_pic = Image.open(f"photos/{away}.eps")

    # improve image resize quality
    home_pic.load(scale=4)
    away_pic.load(scale=4)

    home_resized = home_pic.resize((270, 180))
    away_resized = away_pic.resize((270, 180))

    canvas.paste(home_resized, (0, 0))
    canvas.paste(away_resized, (width - 270, 0))

    canvas.save(f"output/{home}_{away}.png")


def write_tips(home, away, match_tips):
    img = Image.open(f"output/{home}_{away}.png")
    font = ImageFont.truetype("arialbd.ttf", size=35)

    offset1 = [4, 200]
    offset1x = [320, 200]
    offsetx = [580, 200]
    offsetx2 = [850, 200]
    offset12 = [1110, 200]
    offset2 = [1350, 200]

    draw = ImageDraw.Draw(img)

    for tip in match_tips[1]:

        if tip[1] == "1":
            draw.text(offset1, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offset1[1] += 38

        if tip[1] == "1X":
            draw.text(offset1x, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offset1x[1] += 38

        if tip[1] == "X":
            draw.text(offsetx, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offsetx[1] += 38

        if tip[1] == "X2":
            draw.text(offsetx2, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offsetx2[1] += 38

        if tip[1] == "12":
            draw.text(offset12, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offset12[1] += 38

        if tip[1] == "2":
            draw.text(offset2, f"{tip[0]}", fill=(255, 255, 255), font=font)
            offset2[1] += 38

    img.save(f"output/{home}_{away}.png")
    print(f"completed: {home}_{away}")


def create_all_images_with_tips(fixtures, tips):
    data = list(zip(fixtures, tips))

    for match in data:
        home = match[0][0]
        away = match[0][1]
        time = match[0][2]

        create_image(home, away, time)
        write_tips(home, away, match)


# https://docs.google.com/spreadsheets/d/1yHSTmSJpLCh_2Vf_tUeuRbjAstHE8nricPExhO6I3_o
# create_all_images_with_tips(FIXTURES, get_all_tips_from_google_sheets(spreadsheet_id, range_name))
