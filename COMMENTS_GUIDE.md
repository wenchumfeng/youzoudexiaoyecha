# 博客留言功能配置指南

恭喜！你已经成功添加了基于GitHub Issues的utterances评论系统到你的博客。以下是完成配置的最后步骤：

## 1. 替换GitHub仓库信息

你需要在两个文件中替换占位符`your-github-username/your-blog-repo`为你实际的GitHub用户名和仓库名：

### 修改_config.next.yml文件
```yaml
# utterances
utterances:
  repo: 你的GitHub用户名/你的博客仓库名
  issue_term: pathname
  label: Comment
  theme: github-light
```

### 修改source/js/utterances.js文件
```javascript
utterancesFrame.setAttribute('repo', '你的GitHub用户名/你的博客仓库名');
```

## 2. 确保仓库是公开的

utterances需要访问你的GitHub仓库来创建和管理评论Issue，请确保你的博客仓库设置为公开。

## 3. 安装utterances应用

访问[utterances GitHub应用页面](https://github.com/apps/utterances)，点击"Install"按钮，然后选择你的博客仓库进行安装。

## 4. 重新构建和部署博客

完成上述配置后，运行以下命令重新构建你的博客：
```bash
npm run build
```

然后将更改推送到GitHub仓库，触发Cloudflare Pages自动部署。

## 5. 测试评论功能

部署完成后，访问你的博客文章页面，在文章底部应该能看到评论区。尝试发表一条评论来测试功能是否正常工作。

## 常见问题

- **评论区不显示**：检查GitHub仓库信息是否正确，仓库是否公开，以及utterances应用是否已安装。
- **评论无法提交**：确保你已登录GitHub，并且仓库允许评论。
- **样式问题**：如果评论区样式与博客不协调，可以在`utterances.js`文件中调整容器样式。

如果你遇到其他问题，可以查看[utterances官方文档](https://utteranc.es/)获取更多帮助。