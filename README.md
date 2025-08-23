# 游走的小夜叉的博客 - Hexo + Cloudflare Pages 部署指南

## 项目简介
这是一个使用Hexo框架构建的个人博客，主题采用Next。本指南将帮助你将博客部署到Cloudflare Pages。

## 本地开发
1. 安装依赖
   ```bash
   npm install
   ```

2. 启动本地服务器
   ```bash
   npm run server
   ```
   访问 http://localhost:4000 查看博客

3. 创建新文章
   ```bash
   hexo new "文章标题"
   ```

## 部署到Cloudflare Pages

### 准备工作
1. 注册Cloudflare账号
2. 注册GitHub账号
3. 将项目推送到GitHub仓库

### 配置Cloudflare Pages
1. 登录Cloudflare控制台，进入Workers & Pages
2. 点击"连接到Git"
3. 选择你的GitHub仓库
4. 配置构建设置：
   - 生产分支: main
   - 构建命令: npm run build
   - 构建输出目录: public
5. 点击"保存并部署"

### 配置环境变量
在Cloudflare Pages项目设置中，添加以下环境变量：
- CLOUDFLARE_API_TOKEN: 你的Cloudflare API令牌
- CLOUDFLARE_ACCOUNT_ID: 你的Cloudflare账户ID

### 自定义域名（可选）
1. 在Cloudflare Pages项目设置中，点击"自定义域"
2. 输入你的域名并按照提示完成配置

## 自动部署
GitHub Actions工作流已配置（.github/workflows/deploy.yml），每次推送到main分支将自动触发部署。

## 博客留言功能
本博客使用Valine评论系统，支持匿名留言。完成部署后，请参考[COMMENTS_GUIDE.md](COMMENTS_GUIDE.md)配置留言功能。

## 注意事项
1. 确保在_config.yml中设置正确的url（https://your-project-name.pages.dev）
2. 替换部署配置中的your-project-name为你的实际项目名称
3. 首次部署可能需要手动触发GitHub Actions工作流
4. 留言功能需要配置LeanCloud应用凭证，详情见COMMENTS_GUIDE.md