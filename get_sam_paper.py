"""
从 arxiv 获取 SAM 论文信息
"""
import urllib.request
import json
import ssl

# 绕过SSL验证
ssl._create_default_https_context = ssl._create_unverified_context

url = "https://arxiv.org/abs/2304.02643"

try:
    with urllib.request.urlopen(url, timeout=10) as response:
        html = response.read().decode('utf-8')

    # 提取关键信息
    info = {}

    # 提取标题
    if '<meta name="citation_title" content="' in html:
        start = html.find('<meta name="citation_title" content="') + len('<meta name="citation_title" content="')
        end = html.find('"', start)
        info['title'] = html[start:end]

    # 提取作者
    authors = []
    for line in html.split('\n'):
        if '<meta name="citation_author" content="' in line:
            start = len('<meta name="citation_author" content="')
            end = line.find('"', start)
            authors.append(line[start:end])
    info['authors'] = authors

    # 提取摘要
    if '<meta name="citation_abstract" content="' in html:
        start = html.find('<meta name="citation_abstract" content="') + len('<meta name="citation_abstract" content="')
        end = html.find('"', start)
        info['abstract'] = html[start:end].replace('\n', ' ').strip()

    # 提取发布日期
    if '<meta name="citation_publication_date"' in html:
        start = html.find('content="') + len('content="')
        end = html.find('"', start)
        info['date'] = html[start:end]

    # 提取PDF链接
    if 'href="/pdf/2304.02643' in html:
        start = html.find('href="/pdf/2304.02643')
        end = html.find('"', start)
        info['pdf_url'] = 'https://arxiv.org' + html[start:end]

    print("=== SAM 论文信息 ===")
    print(f"标题: {info.get('title', 'N/A')}")
    print(f"作者: {', '.join(info.get('authors', []))}")
    print(f"日期: {info.get('date', 'N/A')}")
    print(f"PDF: {info.get('pdf_url', 'N/A')}")
    print(f"\n摘要:\n{info.get('abstract', 'N/A')}")

except Exception as e:
    print(f"错误: {e}")
