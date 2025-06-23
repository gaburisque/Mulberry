from bs4 import BeautifulSoup

# 読み込むHTMLファイル（適宜ファイル名を確認）
html_file = "Mulberry-test.html"

# 出力先
output_file = "readdy_image_urls.txt"

# HTMLファイルを読み込んで画像URLを抽出
with open(html_file, "r", encoding="utf-8") as f:
    soup = BeautifulSoup(f, "html.parser")

image_tags = soup.find_all("img")
image_urls = [img["src"] for img in image_tags if "src" in img.attrs and img["src"].startswith("http")]

# 書き出し
with open(output_file, "w", encoding="utf-8") as f:
    for url in image_urls:
        f.write(url + "\n")

print(f"{len(image_urls)} 件の画像URLを readdy_image_urls.txt に保存しました。")