/**
 * 初始化utterances评论系统
 */
(function() {
  // 等待页面加载完成
  document.addEventListener('DOMContentLoaded', function() {
    // 检查是否在文章页面
    if (document.querySelector('.post')) {
      // 创建utterances评论框
      const utterancesContainer = document.createElement('div');
      utterancesContainer.className = 'utterances-container';
      utterancesContainer.style.marginTop = '2rem';
      utterancesContainer.style.padding = '1rem';
      utterancesContainer.style.backgroundColor = '#f8f8f8';
      utterancesContainer.style.borderRadius = '8px';

      // 创建utterances iframe
      const utterancesFrame = document.createElement('script');
      utterancesFrame.src = 'https://utteranc.es/client.js';
      utterancesFrame.setAttribute('repo', 'your-github-username/your-blog-repo');
      utterancesFrame.setAttribute('issue-term', 'pathname');
      utterancesFrame.setAttribute('label', 'Comment');
      utterancesFrame.setAttribute('theme', 'github-light');
      utterancesFrame.setAttribute('crossorigin', 'anonymous');
      utterancesFrame.async = true;

      // 添加到页面
      utterancesContainer.appendChild(utterancesFrame);
      document.querySelector('.post-footer').after(utterancesContainer);
    }
  });
})();