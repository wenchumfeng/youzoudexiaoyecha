# 博客留言功能配置指南

恭喜！你已经成功添加了支持匿名评论的Valine评论系统到你的博客。以下是完成配置的最后步骤：

## 1. 获取LeanCloud账号和应用凭证

Valine基于LeanCloud提供后端服务，需要先注册LeanCloud账号并创建应用：

1. 访问[LeanCloud官网](https://leancloud.cn/)并注册账号
2. 登录后，点击"创建应用"，填写应用名称（如"blog-comments"），选择"开发版"免费套餐
3. 进入应用控制台，点击左侧导航栏中的"设置"->"应用Keys"
4. 记录下"App ID"和"App Key"，稍后会用到

## 2. 配置Valine

修改<mcfile name="_config.next.yml" path="e:/blog/youzoudexiaoyecha/_config.next.yml"></mcfile>文件，将`your-leancloud-appid`和`your-leancloud-appkey`替换为你在LeanCloud获取的实际凭证：

```yaml
# Valine - 支持匿名评论的轻量级评论系统
valine:
  appid: 你的LeanCloud App ID
  appkey: 你的LeanCloud App Key
  placeholder: 说点什么吧...
  avatar: monsterid  # 评论者头像样式
  meta: [nick]  # 只显示昵称
  pageSize: 10
  lang: zh-CN  # 设置为中文
  visitor: true  # 显示文章阅读量
  highlight: true
```

## 3. 配置安全域名

在LeanCloud应用控制台中，点击左侧导航栏的"设置"->"安全中心"，在"Web安全域名"中添加你的博客域名（如`https://your-project-name.pages.dev`），以确保评论系统能正常工作。

## 4. 删除不必要的文件

由于我们已从utterances切换到Valine，之前创建的utterances.js文件不再需要，可以删除：
```bash
del e:/blog/youzoudexiaoyecha/source/js/utterances.js
```

## 5. 更新自定义JS配置

修改<mcfile name="_config.next.yml" path="e:/blog/youzoudexiaoyecha/_config.next.yml"></mcfile>文件，移除对utterances.js的引用：

```yaml
# Custom JS
# custom_js:
#   - /js/custom.js
```

## 6. 重新构建和部署博客

完成上述配置后，运行以下命令重新构建你的博客：
```bash
npm run build
```

然后将更改推送到GitHub仓库，触发Cloudflare Pages自动部署。

## 7. 测试评论功能

部署完成后，访问你的博客文章页面，在文章底部应该能看到评论区。尝试发表一条匿名评论来测试功能是否正常工作。

## 常见问题

- **评论区不显示**：检查LeanCloud App ID和App Key是否正确，安全域名是否已配置。
- **评论无法提交**：确保博客域名已添加到LeanCloud的安全域名列表中。
- **头像不显示**：Valine使用Gravatar服务提供头像，若未设置Gravatar，将显示默认头像。
- **阅读量不更新**：检查`visitor`配置是否设为`true`。

如果你遇到其他问题，可以查看[Valine官方文档](https://valine.js.org/)获取更多帮助。