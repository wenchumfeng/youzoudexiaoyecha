import os
import markdown
import uuid
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 添加上下文处理器，使 datetime 在所有模板中可用
@app.context_processor
def inject_datetime():
    return {'datetime': datetime}

# 配置博客文章和留言存储目录
POSTS_DIRECTORY = os.path.join(app.root_path, 'posts')
COMMENTS_DIRECTORY = os.path.join(app.root_path, 'comments')

# 确保留言目录存在
os.makedirs(COMMENTS_DIRECTORY, exist_ok=True)

@app.route('/about')
def about():
    # 获取所有分类
    categories = set()
    for filename in os.listdir(POSTS_DIRECTORY):
        if filename.endswith('.md'):
            if '[' in filename and ']' in filename:
                categories.add(filename.split('[')[1].split(']')[0])
            else:
                categories.add('未分类')
    return render_template('about.html', categories=sorted(categories))



def inject_datetime():
    return {'datetime': datetime}

# 配置博客文章和留言存储目录
POSTS_DIRECTORY = os.path.join(app.root_path, 'posts')
COMMENTS_DIRECTORY = os.path.join(app.root_path, 'comments')

# 确保留言目录存在
os.makedirs(COMMENTS_DIRECTORY, exist_ok=True)

@app.route('/')
def index():
    # 获取所有博客文章
    posts = []
    categories = set()
    for filename in os.listdir(POSTS_DIRECTORY):
        if filename.endswith('.md'):
            # 提取分类信息和文章标题
            if '[' in filename and ']' in filename:
                category = filename.split('[')[1].split(']')[0]
                title = filename.split(']')[1][:-3].replace('-', ' ').title()
                categories.add(category)
            else:
                category = '未分类'
                title = filename[:-3].replace('-', ' ').title()
                categories.add('未分类')
            # 获取文件修改时间
            mtime = os.path.getmtime(os.path.join(POSTS_DIRECTORY, filename))
            date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            # 添加到文章列表
            posts.append({
                'title': title,
                'filename': filename,
                'date': date,
                'category': category
            })
    # 按日期降序排列
    posts.sort(key=lambda x: x['date'], reverse=True)
    return render_template('index.html', posts=posts, categories=sorted(categories))

@app.route('/category/<category>')
def category(category):
    # 获取指定分类的文章
    posts = []
    for filename in os.listdir(POSTS_DIRECTORY):
        if filename.endswith('.md'):
            # 提取分类信息
            if '[' in filename and ']' in filename:
                post_category = filename.split('[')[1].split(']')[0]
            else:
                post_category = '未分类'
            # 检查分类是否匹配
            if post_category == category:
                # 提取文章信息
                if post_category == '未分类':
                    title = filename[:-3].replace('-', ' ').title()
                else:
                    title = filename.split(']')[1][:-3].replace('-', ' ').title()
                # 获取文件修改时间
                mtime = os.path.getmtime(os.path.join(POSTS_DIRECTORY, filename))
                date = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
                # 添加到文章列表
                posts.append({
                    'title': title,
                    'filename': filename,
                    'date': date,
                    'category': post_category
                })
    # 按日期降序排列
    posts.sort(key=lambda x: x['date'], reverse=True)
    # 获取所有分类
    all_categories = set()
    for filename in os.listdir(POSTS_DIRECTORY):
        if filename.endswith('.md'):
            if '[' in filename and ']' in filename:
                all_categories.add(filename.split('[')[1].split(']')[0])
            else:
                all_categories.add('未分类')
    return render_template('index.html', posts=posts, categories=sorted(all_categories), current_category=category)

@app.route('/post/<filename>', methods=['GET', 'POST'])
def post(filename):
    # 读取博客文章内容
    file_path = os.path.join(POSTS_DIRECTORY, filename)
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    # 转换Markdown为HTML
    html_content = markdown.markdown(content)
    # 获取文章标题和分类
    if '[' in filename and ']' in filename:
        category = filename.split('[')[1].split(']')[0]
        title = filename.split(']')[1][:-3].replace('-', ' ').title()
    else:
        category = '未分类'
        title = filename[:-3].replace('-', ' ').title()

    # 处理留言提交
    if request.method == 'POST':
        name = request.form.get('name', '匿名')
        comment_content = request.form.get('content', '')
        if comment_content:
            # 生成留言ID
            comment_id = str(uuid.uuid4())
            # 保存留言
            comment_file = os.path.join(COMMENTS_DIRECTORY, f'{filename}_{comment_id}.txt')
            with open(comment_file, 'w', encoding='utf-8') as f:
                f.write(f'姓名: {name}\n')
                f.write(f'时间: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
                f.write(f'内容: {comment_content}\n')
            # 重定向到文章页面
            return redirect(url_for('post', filename=filename))

    # 读取留言
    comments = []
    for comment_file in os.listdir(COMMENTS_DIRECTORY):
        if comment_file.startswith(filename):
            with open(os.path.join(COMMENTS_DIRECTORY, comment_file), 'r', encoding='utf-8') as f:
                comment_lines = f.readlines()
                comment = {
                    'name': comment_lines[0].replace('姓名: ', '').strip(),
                    'time': comment_lines[1].replace('时间: ', '').strip(),
                    'content': comment_lines[2].replace('内容: ', '').strip()
                }
                comments.append(comment)
    # 按时间降序排列留言
    comments.sort(key=lambda x: x['time'], reverse=True)

    return render_template('post.html', title=title, content=html_content, category=category, comments=comments)

if __name__ == '__main__':
    app.run(debug=True)