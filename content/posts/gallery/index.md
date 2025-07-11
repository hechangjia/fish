---
title: 图库
tags:
  - gallery
  - 图片
description: 这是专门用来展示图片的地方

---

## 嵌入PDF

**测试**
[PDF](gallery/第一章.pdf)

<iframe 
  src="gallery/第一章.pdf" 
  width="200%" 
  height="600px"
>
  <p>您的浏览器不支持PDF预览，请<a href="./assets/pdfs/第一章.pdf">下载文件</a></p>
</iframe>

## 嵌入视频

<video controls style="width: 80%;">
  <source src="./gallery/TimeShiftSystems.mp4" type="video/mp4">
</video>


<style>
  .my-video {
    width: 300%;
  }
</style>

<video controls class="my-video">
  <source src="./gallery/TimeShiftSystems.mp4" type="video/mp4">
</video>

## 图库

{{< gallery >}}
  <img src="gallery/Manim.jpg"  />
  <img src="gallery/banner_1.jpg"  />
  <img src="gallery/banner_2.jpg"  />
  <img src="gallery/banner_3.jpg"  />
  <img src="gallery/code.gif"  />
{{< /gallery >}}



{{< gallery >}}
  <img src="gallery/code.gif" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/banner_3.jpg" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/banner_2.jpg" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/banner_1.jpg" class="grid-w50 md:grid-w33 xl:grid-w25" />
  <img src="gallery/Manim.jpg" class="grid-w50 md:grid-w33 xl:grid-w25" />
{{< /gallery >}}

{{< carousel images="gallery/*.jpg" aspectRatio="21-9" interval="2500" >}}









