import requests
from bs4 import BeautifulSoup
 
url = "https://stackoverflow.com/tags?page={}&tab=popular"
page = 1


# Ý tưởng:
# 1.Mình sẽ kéo page source của url về
# 2. Làm đẹp source với bs4
# 3. Tìm tìm block chứa tất cả các block tag của page hiện tại
# 4. Tìm tất cả các block tag, mỗi block là 1 tag
# 5. Với mỗi block, ta viết 1 hàm để đọc các thông tin của nó
 
# 1. Gửi request tới url với page được truyền vào
r = requests.get(url.format(page))
print('status_code', r.status_code)

# 2. lam dep source
soup = BeautifulSoup(r.content, 'lxml')

# 3. Lấy block cha chứa tất cả các tags
block_tag = soup.select_one('div#tags-browser')

# 4. Các thẻ tag là con của block_tag, là các thẻ div có các class dưới đây
all_tags = block_tag.select('div.s-card.js-tag-cell.d-flex.fd-column')
print('Total tags count:', len(all_tags))


# 5. Viết hàm đọc các thông tin từ thẻ tag đó.
# Nếu option xử lý được bật, mình sẽ bỏ qua các khoảng trắng thừa, chỉ lấy giá trị số lượng
def get_tag_info(tag, preprocess=False):
    tag_name = tag.select_one('div.d-flex.jc-space-between.ai-center.mb12 > div > a').text
    tag_description = tag.select_one('div.flex--item.fc-medium.mb12.v-truncate4').text
    question_total = tag.select_one('div.mt-auto.d-flex.jc-space-between.fs-caption.fc-black-400 > div:nth-child(1)').text
    question_today = tag.select_one('div.mt-auto.d-flex.jc-space-between.fs-caption.fc-black-400 > div.flex--item.s-anchors.s-anchors__inherit > a:nth-child(1)').text
    question_this_week = tag.select_one('div.mt-auto.d-flex.jc-space-between.fs-caption.fc-black-400 > div.flex--item.s-anchors.s-anchors__inherit > a:nth-child(2)').text
    if preprocess:
        tag_description = tag_description.strip()
        question_total = question_total.split()[0]
        question_today = question_today.split()[0]
        question_this_week = question_this_week.split()[0]
    return tag_name, tag_description, question_total, question_today, question_this_week
 
# Thử in ra mà ko xử lý
print(get_tag_info(all_tags[0]))
print()
# Thử in ra và qua xử lý
print(get_tag_info(all_tags[0], True))
 
# Ta có thể lấy toàn bộ bằng cách duyệt lần lượt
# for tag in all_tags:
#     print(get_tag_info(tag, True))
 

