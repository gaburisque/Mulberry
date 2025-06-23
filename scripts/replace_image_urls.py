from bs4 import BeautifulSoup

# 読み込むHTMLファイルと差し替え後の保存先
input_html = "Mulberry-test.html"
output_html = "Mulberry-fixed.html"
image_folder = "downloaded_images"
url_list_file = "readdy_image_urls.txt"

# 画像URL一覧を読み込み
with open(url_list_file, "r", encoding="utf-8") as f:
    original_urls = [line.strip() for line in f if line.strip()]

# HTMLをパースしてimgタグを取得
with open(input_html, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

img_tags = soup.find_all("img")

# 差し替え処理
for i, tag in enumerate(img_tags):
    if i < len(original_urls) and tag.get("src") == original_urls[i]:
        tag["src"] = f"{image_folder}/img_{i + 1}.jpg"

# 差し替えたHTMLを保存
with open(output_html, "w", encoding="utf-8") as f:
    f.write(str(soup))

print(f"画像URLをローカル画像に差し替えました → {output_html}")