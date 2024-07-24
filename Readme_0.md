# 陪伴小学生学习 Python 笔记：2024 年寒假

## ——零：关于 “青少年编程” 的看法

---

**说明：**

> 本文内容较长，持续更新中，连载于：`github/xiaohaimiao` [Python 学习笔记](https://github.com/xiaohaimiao/Python-Learning/ "Python 学习笔记")

在 `github` 或 `markdown` 编辑器中阅读本文时，可打开其目录功能方便浏览和跳转。

> - `github` 页面中，点击文档右上角的目录图标；
> 
> - `marktext` 编辑器中，按 `Ctrl-K`

---

## 目录

[首页：前言](README.md "返回：陪伴小学生学习 Python 笔记")

零：关于 “青少年编程” 的看法

[一、算法入门练习](Readme_1.md "查阅：一、算法入门练习")

[二、算法进阶练习](Readme_2.md "查阅：二、算法进阶练习")

 ---

### 1. 一些杂七杂八的信息

说起对于【**青少年学编程**】这个事情的感受，说多了都是泪，一句话：

> 能深切感受到来自各方大佬们，对父母们（的钱包）浓浓的关爱之心。
> 
> ——在这样的环境里，作为父母，真不容易。

目前小学六年级，寒假，在学 Python 和算法入门，水平一般，从学习效率角度还算满意，主动性尚可，算不上特别积极主动那种。

相比之下，肯定有很多更厉害的孩子，甚至父母还是大厂甚至国外大厂软件工程师。

我家也就普普通通的水平，也不给孩子压力，重点在培养兴趣，领入门。

简单介绍一下我家小朋友学编程的经历供参考：

- 幼儿园自己跟着 WeDo 玩过简单的结合乐高小颗粒的图形化编程，很简单不需要教。类似的玩过米兔的几套智能积木；

- 小学低年级用 `iPad` 上 `Apple` 免费的 `Playgrounds` 简单学过 `swift`；
  —— 此应用相当不错，但平台受限于 Apple 产品，不被国内各种比赛兼容。功能很强大，Swift 是真正商用级别的编程语言，尤其可以在学习过程中实战开发 AR 应用很赞；

- 四五年级假期用 `CodeCombat` ~~学过~~ 玩过 `javascript`；
  ——很好玩，纯逻辑，用代码操控游戏角色和武器攻击地图上的怪物、闯关并拾取物品，没涉及到 `HTML` 等内容；
  
  > 题外：就像二十多年 IBM 前的 `CodeRobot`，但更容易上手也更好玩，每一关针对性要解决的问题也很有意思。
  > 
  > ——`CodeRobot` 开放性过大，我当时用来试验多个 `TankBot` 之间协同配合的战法，类似现在的无人机作战模式。
  
  ——比较推荐 `CodeCombat`，可选 `Python` 语言；

- 六年级上学期临时被拉去参加 `iCode.org` 的比赛接触了一下 `iCode`，相对 `CodeCombat` 来说 `iCode` 更精简、更收敛，是一个个小 `puzzle` `解谜智力游戏`。
  ——介于小朋友幼儿园时玩的 `葡萄科技` 的 `哈啰葡星人` 和后来玩的 `Apple` 的 `Playgrounds` 之间。前者纯图形化拖放代码块闯关，后者支持代码操作角色，与目前流行的各种图形化编程平台的功能类似，但侧重于：`用尽可能少的代码块完成特定关卡的任务` ——iCode 支持图形化和 Python 两种方式；
  
  > 题外：`葡萄科技`这家公司曾经有很多不错的产品，我基本买全了。可惜该公司内斗后来转型做动画和拼插类玩具 `布鲁克` 去了——就是那个 `飞呀飞呀飞呀飞呀 什么都不怕` 类似汪汪队那类的动画。
  
  ——推荐把 iCode.org 上免费关玩一遍，毕竟开放性不足，一遍过；
  
  > iCode 这样的在全球普及编程组织是值得尊敬的，但到了国内结合特色的赛事商业模式就变味了，这类玩一遍的拿来做比赛项目，是不是有点太那啥了？
  > 
  > 我试着把比赛练习的题做了一遍，最后两题还是卡了段时间的，而一旦知道诀窍那就简单了。
  > 
  > 所以，孩子比赛名字中拿满分那几个，我实在是不相信他们的智力水平比我高的，更多是信息不对称罢了。比如我知道某位满分同学正是 `iCode` 本地某代理商的孩子。

- 六年级上学期临时被拉去参加 `腾讯 Coding` 编程比赛，对比之前玩的 `Kitten` 略有差异，但也就是 **海淀区方言 和 朝阳区方言 的区别**罢了，都是 `Scratch` 衍生品；

- 五年级暑假：玩 `CodeCombat` 时，从 `Javascript` 改为了 `Python`，做了一些简单入门练习，比如画图等趣味性的内容；六年级寒假：系统性的把 Python 基础编程、算法入门过一遍——见此学习笔记。
  ——**直到这一次**，我才真正介入到孩子学编程的过程，**需要扎扎实实过一遍**。

对于 **图形化编程**：

- 市面上各类 `图形化编程` ，诸如 `编程猫`、`腾讯 Coding` 等等，大同小异，不用太在意：
  ——都是 麻省理工学院 `mit scratch` 开放源代码后，**雨后春笋冒出来**的；
  ——这些平台也仅仅比当年乐高的儿童版 `Wedo` 高级一些，我家两位小朋友都是在幼儿园自己玩学会的 `Wedo`，一二年级后自己跟着 `免费教程` `自学` `玩会` 的 `Scratch`，一点儿都不难；
  ——原因是 `学习图形化编程的作用` **被夸大了**，而**那些平台为了各自商业目的而赞助的各方大佬们（`有背景、有License`）组织的比赛**，之间也没太明显的区别，没有太多实际意义，**本质就是卖证书**。——欢迎告我诽谤。
  ——真正问题是：证书品类丰富了、数量庞大了，招生那边还不是一样按人数控制？

总之，这些琳琅满目的各类比赛、平台、编程班等等，真正有意义的测试和比赛只有两类，只有到小学高年级、初中以后才会逐步接触：

1. `CPS-J/S` 和 `NOIP/NOI`，信奥赛路线，算法为主的竞赛；

2. 编程水平和能力自测：
   学习了编程，参加一下自测，系统性的检验一下自己的学习效果，但不要对证书本身太当回事。等孩子大了，去全球最大的编程交友社区 `Github` 刷项目、去刷 `LeetCode`，真刀真枪更有意思。这几年国内蓝桥杯的刷题质量貌似也提升了，高中以后不妨去这些地方与世界各地的朋友共同促进。

**个人观点：**

> - **图形化编程 孩子自己跟着玩就行**：
>   
>   - 幼儿园中班大班玩 `Wedo`，顺带逐步过渡到小颗粒乐高；
>   
>   - 一、二年级自学图形化编程，用 `编程猫`、`腾讯Coding` 什么都行，参加比赛时你会发现每个赛项里都有这几家——各种坑父母，回头写个专题吧
> 
> - **不必去跟着机构学，不为省钱，关键是省时间**：
>   ——孩子的时间更宝贵，成长的不同阶段都只有一次；
>   ——跟着那些机构慢吞吞学，孩子被哄得开开心心，家长判断不了质量和效果，只是掏钱买课包，这些时间学点儿别的不好么？
>   ——当然，如果学别的也类似（浪费时间），那倒没什么差别。
> 
> - **参加图形化编程的比赛有意义么？有，没那么大**；图形化编程，只是有逻辑思维的概念，有编程的基本概念——不参加也有。
> 
> - **这类证书有意义么？有，没那么大**。
>   有的地方有所谓科技特长生政策。但说实话，图形化编程 这种烂大街的东西，招生一方不知道`烂大街`么？
>   ——如何从那么多持证候选人中筛选出指定数量的？
>   ——参考最近电影《学爸》中让孩子学编钟那一段吧；
> 
> - **关注孩子的：自学能力、解决问题的能力**——自己思考如何去解决问题，想办法寻求帮助、获得资源和继续学习
>   ——这两类能力才是**学编程的真正目的和关键**。

### 2. 目标和定位

在我看来，孩子将来未必要从事软件开发行业，

> - 哪怕是量子编程、生物编程，
> 
> - AI辅助你编程，还是被AI支配的编程，
> 
> - 甚至BCI脑机接口的编程，等等

但环顾一圈，那么多兴趣爱好中，

——**编程最值得学，值得投入时间和精力**。

前面提到，真正让孩子值得深入的编程学习的原因，重点是：

> + 自学能力
> 
> + 解决问题的能力，尤其：
>   
>   + 解决复杂问题的能力
>   
>   + 解决新问题的能力

所以，**我对自家孩子的期待，或者说我努力的方向：**

1. **帮助孩子体会到算法的乐趣，争取走上 NOI 路线** 虽然将来未必有兴趣、未必能沉下心来战 NOI，甚至**未必能进五十人名单**
   ——不试试看不知道，关键在：让孩子体会到类似的乐趣和爽感。
   
   能否进入 `NOI` ？能否进入`全国五十人名单`？能保送哪个大学？
   ——说实话，重要么？
   ——**能进入那个级别的孩子，需要保送？** **他们的学习能力和效率**，一样可以自己考上，甚至更高。

2. 其次，**重点是提升能力**： 信息素养方面的能力只是必备技能，好比每个人都会玩手机，刷抖音什么的，不难。而更重要是**学习能力和解决问题的能力**；

3. 再有，目前 `AI 辅助人类` 的时代，甚至未来 `人类辅助 AI` 的时代，会编程总要有很多优势——至少**比不会编程的人更容易理解和利用好 AI 工具**。

### 3. 学编程的门槛

**学编程最常见的问题：我不知道学了 C/C++/Python 能做什么？**

更别提数据结构和算法课，大部分人完全是为了分数而学习。

这**其实是动力问题**。

所以，重点是 **让学习与解决问题结合起来**，让学生体会到 `用编程解决问题 的 快感`，形成正向激励。

迈过入门的门槛，之后他/她会自己学习、找资料完成后续的学习，就算上路了。

### 4. 学编程语言，究竟学什么？

不同的编程语言，背后的 `编程知识` 是相同的。

好比**英语，汉语**，语言特点不同、发音不同、语法不同，**各种不同**。

但内容中涉及的 `人类生活常识` 是相同的。

在各种编程语言中，语法不同、关键字略有不同，但三大基础结构是相同的：

> - 顺序结构
> 
> - 分支结构
> 
> - 循环结构

甚至，这三大基础结构也不是编程特有的，而是人类日常思维、语言逻辑中固有的。

解决生活中的任何问题，都离不开这三个基础的思维逻辑模块，是它们的各种组合。

比如：

> 去菜市场买两斤西红柿，如果看到西瓜就买一个。
> （这是个程序员的笑话：老婆让程序员老公去买菜，最后买了一个西红柿回来）

无非，用某种特定的编程语言来写下来，用代码实现罢了。

而，从一种编程语言，到另外一种编程语言，所涉及的语法变化、关键字（单词）变化，也就那么点儿。

所以，绝大部分有经验的软件工程师，都类似：

> **至少精通一门**，熟悉甚至熟练好几门——根据需要还可以很快学会新的。

他们不会认为这里面有什么问题，他们会告诉你：

> 重要的是`编程思想`，而`编程思想`都是一样的。

正如讲英语和讲汉语的人，绝大部分 `生活常识` 都是相同相近的，所以能够实现两种语言的翻译，甚至比手画脚也能简单交流，正是这个原因。

所以，找一门相对容易上手的编程语言，学到登堂入室，掌握了一定的`编程知识`、`编程思想`之后，再**根据需要切换为其它语言**，岂不是更高效？

——怕学不会？就这么丁点儿要求，怕不是小看了程序员？

### 5. 为何选择 Python？而不是 C/C++？

#### C/C++

> 有些人会告诉你，小学高年级就可以开始学习 C/C++。

我不反对。但从客观角度说，C/C++ 上手难度略大，学习过程略枯燥。
我高中主要用 Basic/QBasic 和 Pascal/Turbo Pascal，后来学了 ASM 和 C，在 DOS 下写了个GUI库和汉字显示库、袖珍汉字环境和中文自阅读文件生成器，还做了一些当时流行的游戏的修改器（《仙剑奇侠》、《大航海时代》、《命令与征服》等等）——全凭兴趣。

直到大学才学的数据结构——说实话，很无聊，要不是已经有底子，真难坚持完。

另外，

> 培训机构的利益相关者会告诉你，某某孩子小学五年级就参加什么全国大赛，C/C++拿了一等奖，云云。

任何培训机构，都喜欢利用 `幸存者偏差` 这样的逻辑谬误和心理偏差来误导消费者。

关键问题是：

> - 你的孩子是那个幸存者么？
> 
> - 没有拿奖的、甚至因为学习枯燥而失去兴趣的占比有多大？
> 
> - 相对来说哪种语言更容易入门？培养孩子兴趣的成功率更高？

#### Python

说实话，我很不喜欢 Python，过去。

Python 这种脚本语言让我这类强迫症最头疼的一点：

> Python 的代码逻辑依赖于排版！！！一旦缩进变了，代码逻辑可能会大变！
> 
> 甚至不能写在一行上！

——但得益于社区大量的积累，Python 真的非常香。

虽然我主力用的其它语言、它们的社区也很不错，但 Python 社区就更活跃了。

但要注意，市面上有大量的过度宣传和错误宣传，需要正确面对，例如：

> - 很多培训机构，用模板化的案例来开展教学，看起来的确【速成】了，但这些学员里可能只有不到 1% 的能在师傅领进门之后，继续深入学习下去；
> 
> - 学习编程，虽然照着那些案例照猫画虎能够提升兴趣和积极性，但学少林七十二绝技还得一步步走到登堂入室，这里面的平衡点绝对不是那些培训机构宣传的那么简单；
> 
> - 很多宣传夸大了 Python 的实际作用和意义，作为前专业软件开发工程师（退休），更多用来做一些小范围使用的小工具、或当作万能胶来用。
>   ——也有少数公司和个人用 Python 来搭建一些产品和平台。大概如此，不展开，免得引战。
> 
> - 小朋友学 Python，切忌心浮气躁去搞 `爬虫` 什么的。千万扎扎实实打基础，学习背后涉及的知识。
>   
>   写个程序 “爬” 这个网站 “爬” 那个网站，恰恰把大量时间浪费在很多`一次性信息`上。这类工作，有经验的没兴趣，一般搭好框架，然后交给刚入行的助理去干。
>   
>   > 若干年前，曾经有位来应聘的程序员，非坚持 Python 如何了不起。问有什么特别的，想来想去只有一句：Python 擅长开发爬虫。
>   > 问他上家公司做什么工作，回答：做爬虫。再问：爬虫开发完了干什么？答：换家公司做爬虫。
>   > 哭笑不得。
>   > 
>   > ——哪种语言开发 爬虫 都很简单，只是被爬取的网站和网页经常修改，Python 作为脚本相对容易修改调整罢了。
>   > 
>   > 早年我设计搜索引擎时专门设计了一套基于 Perl 的 爬虫引擎 来降低适配成本，并不是说 Python 来开发爬虫就如何厉害，其它语言就不行。

虽然**可以直接学** C/C++，**我选择**让孩子先学 Python，入门后再速通 C/C++。

孩子上个假期玩 `CodeCombat` 从 `Javascript` 改为 `Python`，算是 ”自然学习“ 了一点点 Python 基础，这个假期我带着他把基础练习完整做了一遍，争取把基础打扎实一些，于是有了这一份学习笔记。

一家之言，各家情况不同，观点不同，仅供参考。

---

[回到首页：前言](README.md "返回：陪伴小学生学习 Python 笔记")

零：关于 “青少年编程” 的看法

[一、算法入门练习](Readme_1.md "查阅：一、算法入门练习")

[二、算法进阶练习](Readme_2.md "查阅：二、算法进阶练习")

---