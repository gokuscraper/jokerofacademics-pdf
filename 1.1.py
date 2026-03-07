Request URL:
https://jokerofacademics.com/articles.php?page=2
Request Method:
GET
Status Code:
200 OK
Remote Address:
127.0.0.1:7897
Referrer Policy:
strict-origin-when-cross-origin

< !DOCTYPE
html >
< html
lang = "en" >
< head >
< !-- Google
tag(gtag.js) -->
< script async src = "https://www.googletagmanager.com/gtag/js?id=G-Q0921SVTTG" > < / script >
< script >
window.dataLayer = window.dataLayer | | [];
function
gtag()
{dataLayer.push(arguments);}
gtag('js', new
Date());

gtag('config', 'G-Q0921SVTTG');
< / script >
< meta
charset = "UTF-8" >
< meta
name = "viewport"
content = "width=device-width, initial-scale=1.0" >
< title > Published
Articles — Joker 🤡f
Academics < / title >
< link
href = "https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Abril+Fatface&family=Bebas+Neue&family=Lato:wght@300;400;700&display=swap"
rel = "stylesheet" >
< style >
:root
{
    --google - blue:  # 4285F4;
        --google - red:  # EA4335;
--google - yellow:  # FBBC04;
--google - green:  # 34A853;
--dark:  # 1a1a1a;
--light:  # f9f6f0;
--card - bg:  # ffffff;
--text - muted:  # 757575;
--border:  # e0e0e0;
}
*{margin: 0;
padding: 0;
box - sizing: border - box;}
body
{background: var(--light);
font - family: 'Lato', sans - serif;
color: var(--dark);}

/ * ── 导航（与
index.html
完全一致）── * /
nav
{
    position: sticky;
top: 0;
z - index: 100;
background: var(--dark);
border - bottom: 4
px
solid
var(--google - yellow);
display: flex;
justify - content: center;
flex - wrap: wrap;
}
nav
a
{
    color:  # fff; text-decoration: none;
        padding: 14
px
22
px;
font - family: 'Bebas Neue', sans - serif;
font - size: 1
rem;
letter - spacing: 0.12
em;
transition: all
0.2
s;
position: relative;
}
nav
a::after
{
    content: '';
position: absolute;
bottom: 0;
left: 50 %;
right: 50 %;
height: 4
px;
background: var(--google - yellow);
transition: all
0.2
s;
}
nav
a: hover
{color: var(--google - yellow);}
nav
a: hover::after
{left: 0;
right: 0;}
nav
a.active
{color: var(--google - yellow);}
nav
a.active::after
{left: 0;
right: 0;}
nav
a: nth - child(2):hover
{color: var(--google - red);}
nav
a: nth - child(2):hover::after
{background: var(--google - red);}
nav
a: nth - child(3):hover
{color: var(--google - blue);}
nav
a: nth - child(3):hover::after
{background: var(--google - blue);}

@media(max - width

: 500
px) {nav
a
{padding: 12px 14px;
font - size: 0.9
rem;}}

/ * ── 页面容器 ── * /
.page - wrap
{max - width: 1000px;
margin: 0
auto;
padding: 48
px
24
px
80
px;}

/ * ── 页面标题区（复用
index.html
的
section - label
风格）── * /
.page - header
{margin - bottom: 36px;}
.section - label
{
    font - family: 'Bebas Neue', sans - serif;
font - size: 0.85
rem;
letter - spacing: 0.35
em;
text - transform: uppercase;
margin - bottom: 8
px;
display: flex;
align - items: center;
gap: 10
px;
color:  # c8930a;
}
.section - label::before
{
    content: '';
display: inline - block;
width: 28
px;
height: 3
px;
background: var(--google - yellow);
}
.page - title
{
    font - family: 'Playfair Display', serif;
font - size: clamp(2
rem, 4
vw, 2.8
rem); font - weight: 900;
line - height: 1.1;
}
.page - desc
{color: var(--text - muted);
margin - top: 8
px;
font - size: 0.95
rem;}

/ * ── 筛选栏 ── * /
.filter - bar
{
    display: flex;
align - items: center;
gap: 14
px;
margin - bottom: 28
px;
flex - wrap: wrap;
}
.filter - bar
label
{
    font - family: 'Bebas Neue', sans - serif;
letter - spacing: 0.1
em;
font - size: 0.9
rem;
color: var(--text - muted);
}
.filter - bar
select
{
    padding: 8px 14px;
border: 2
px
solid
var(--dark);
font - family: 'Lato', sans - serif;
font - size: 0.88
rem;
background:  # fff; cursor: pointer; outline: none;
border - radius: 0;
-webkit - appearance: none;
transition: border - color
0.2
s;
}
.filter - bar
select: focus
{border - color: var(--google - yellow);}
.result - count
{
    margin - left: auto;
font - size: 0.83
rem;
color: var(--text - muted);
font - family: 'Bebas Neue', sans - serif;
letter - spacing: 0.08
em;
}

/ *搜索框样式 * /
.search - wrap
{
    display: flex;
align - items: center;
gap: 8
px;
flex: 1
1
260
px;
}
.search - wrap
input[type = "text"] {
    flex: 1;
padding: 8
px
12
px;
border: 2
px
solid
var(--dark);
font - family: 'Lato', sans - serif;
font - size: 0.9
rem;
border - radius: 0;
outline: none;
}
.search - wrap
input[type = "text"]:focus
{
    border - color: var(--google - yellow);
}
.search - wrap
button
{
    padding: 8px 10px;
border: 2
px
solid
var(--dark);
background: var(--dark);
color:  # fff;
font - family: 'Bebas Neue', sans - serif;
font - size: 0.85
rem;
letter - spacing: 0.12
em;
text - transform: uppercase;
cursor: pointer;
}
.search - wrap
button: hover
{
    background: var(--google - yellow);
color: var(--dark);
}

/ * ── 文章网格列表（高密度，多列）── * /
.article - list
{
    display: grid;
grid - template - columns: repeat(auto - fill, minmax(260
px, 1
fr));
gap: 20
px;
}

.article - card
{
    background: var(--card - bg);
border: 2
px
solid
var(--dark);
padding: 18
px
18
px
18
px
24
px; / *左边留空给色条 * /
       position: relative;
overflow: hidden;
transition: transform
0.2
s, box - shadow
0.2
s;
display: flex;
flex - direction: column;
gap: 8
px;
}
/ *左侧彩色竖条，颜色按全局顺序分配：黄、蓝、红、绿（1 - 4
循环） * /
.article - card::before
{
    content: '';
position: absolute;
top: 0;
left: 0;
width: 6
px;
height: 100 %;
}
.article - card.color - 1::before
{background: var(--google - yellow);} / *黄  # FBBC04 */
.article - card.color - 2::before
{background: var(--google - blue);} / *蓝  # 4285F4 */
.article - card.color - 3::before
{background: var(--google - red);} / *红  # EA4335 */
.article - card.color - 4::before
{background: var(--google - green);} / *绿  # 34A853 */
.article - card: hover
{transform: translateY(-3px); box - shadow: 5
px
5
px
0
var(--dark);}

/ *封面缩略图：固定比例，保持不变形 * /
.card - cover
{
    flex - shrink: 0;
width: 120
px;
border: 1
px
solid
var(--border);
overflow: hidden;
background:  # fff;
border - radius: 2
px;
margin - bottom: 4
px;
}
.card - cover
img
{
    width: 100 %;
height: auto;
max - height: 160
px;
object - fit: contain;
display: block;
}
.card - cover.no - cover
{
    font - size: 2rem;
color:  # ccc;
}

/ *卡片内容 * /
.card - body
{flex: 1;
min - width: 0;
display: flex;
flex - direction: column;
gap: 4
px;}

.card - tag
{
    font - size: 0.72rem;
font - weight: 700;
letter - spacing: 0.1
em;
text - transform: uppercase;
padding: 3
px
8
px;
border - radius: 2
px;
display: inline - block;
margin - bottom: 8
px;
}
/ *标签颜色与卡片色条一致，按全局顺序：黄、蓝、红、绿 * /
.article - card.color - 1.card - tag
{background: var(--google - yellow);
color: var(--dark);} / *黄 * /
.article - card.color - 2.card - tag
{background: var(--google - blue);
color:  # fff; }        /* 蓝 */
.article - card.color - 3.card - tag
{background: var(--google - red);
color:  # fff; }        /* 红 */
.article - card.color - 4.card - tag
{background: var(--google - green);
color:  # fff; }       /* 绿 */

.card - title
{
    font - family: 'Playfair Display', serif;
font - size: 1.02
rem;
font - weight: 700;
line - height: 1.35;
margin - bottom: 2
px;
max - height: 2.7
em;
overflow: hidden;
}
.card - title
a
{color: var(--dark);
text - decoration: none;}
.card - title
a: hover
{color: var(--google - red);}

.card - author
{font - size: 0.8rem;
color:  # 666; font-style: italic; }

.card - abstract
{
    font - size: 0.83rem;
line - height: 1.5;
color:  # 555;
max - height: 3.1
em;
overflow: hidden;
}

.card - meta
{
    display: flex;
align - items: center;
gap: 10
px;
font - size: 0.74
rem;
color: var(--text - muted);
flex - wrap: wrap;
margin - top: 4
px;
}
.card - meta.doi
a
{color: var(--google - blue);
text - decoration: none;}
.card - meta.doi
a: hover
{text - decoration: underline;}
.card - read - more
{
    margin - left: auto;
font - family: 'Bebas Neue', sans - serif;
font - size: 0.9
rem;
letter - spacing: 0.08
em;
color: var(--google - red);
text - decoration: none;
}
.card - read - more: hover
{text - decoration: underline;}

/ * ── 空状态 ── * /
.empty - state
{text - align: center;
padding: 80
px
20
px;}
.empty - state.icon
{font - size: 3.5rem;
margin - bottom: 16
px;}
.empty - state
h3
{
    font - family: 'Playfair Display', serif;
font - size: 1.4
rem;
font - weight: 700;
margin - bottom: 8
px;
}
.empty - state
p
{color: var(--text - muted);
font - size: 0.95
rem;}

/ * ── 分页（与
index.html
风格一致：Bebas
Neue
字体，黄色高亮）── * /
.pagination
{
    display: flex;
justify - content: center;
align - items: center;
gap: 8
px;
margin - top: 48
px;
flex - wrap: wrap;
}
.pagination
a,.pagination
span
{
    display: inline - flex;
align - items: center;
justify - content: center;
min - width: 38
px;
height: 38
px;
padding: 0
12
px;
border: 2
px
solid
var(--dark);
font - family: 'Bebas Neue', sans - serif;
letter - spacing: 0.08
em;
font - size: 0.95
rem;
text - decoration: none;
color: var(--dark);
background:  # fff; transition: all 0.15s;
}
.pagination
a: hover
{background: var(--dark);
color: var(--google - yellow);}
.pagination
span.current
{
    background: var(--google - yellow);
border - color: var(--google - yellow);
color: var(--dark);
font - weight: 700;
}
.pagination
span.disabled
{
    color:  # bbb; cursor: default; border-color: #ddd; background: #fafafa;
}

/ * ── 色条分隔线（与首页一致）── * /
.color - divider
{display: flex;
height: 5
px;
width: 100 %;
margin - bottom: 0;}
.color - divider
div
{flex: 1;}
.color - divider.c1
{background: var(--google - blue);}
.color - divider.c2
{background: var(--google - red);}
.color - divider.c3
{background: var(--google - yellow);}
.color - divider.c4
{background: var(--google - green);}

/ * ── 页脚（与
index.html
完全一致）── * /
footer
{
    background: var(--dark);
border - top: 6
px
solid;
border - image: linear - gradient(90
deg, var(--google - blue)
25 %, var(--google - red)
25 % 50 %, var(--google - yellow)
50 % 75 %, var(--google - green)
75 %) 1;
padding: 40
px
24
px
24
px;
color: rgba(255, 255, 255, 0.5);
font - size: 0.85
rem;
}
.footer - inner
{max - width: 1000px;
margin: 0
auto;}
.footer - bottom
{
    display: flex;
justify - content: space - between;
flex - wrap: wrap;
gap: 10
px;
}
.issn
{color: rgba(255, 255, 255, 0.3);
font - family: monospace;}
footer
a
{color: rgba(255, 255, 255, 0.5);
text - decoration: none;}
footer
a: hover
{color: var(--google - yellow);}
< / style >
    < / head >
        < body >

        <!-- 导航（统一为
Home
导航结构，Articles
高亮）-->
< nav >
  < a
href = "/" > Home < / a >
                      < a
href = "/articles.php"


class ="active" > Articles < / a >

< a
href = "/leaderboard.php" > Leaderboard < / a >
< a
href = "/board.php" > Editorial
Board < / a >
< a
href = "/#contact" > Contact < / a >
< a
href = "/author/login.php"


class ="nav-author-portal" > Author Portal / 投稿人入口 < / a >

< / nav >

< div


class ="page-wrap" >

< !-- 页面标题 -->
< div


class ="page-header" >

< div


class ="section-label" > Published Works < / div >

< h1


class ="page-title" > All Articles < / h1 >

< p


class ="page-desc" > Peer-reviewed research published in Joker 🤡f Academics < / p >

< / div >

< !-- 筛选栏 -->
< div


class ="filter-bar" >

< label
for ="catFilter" > Category:< / label >
< select
id = "catFilter"
onchange = "filterCategory(this.value)" >
< option
value = "" > All
Categories < / option >
< option
value = "Absurdist Methodology" >
Absurdist
Methodology < / option >
< option
value = "Absurdist Methodology 荒诞主义方法论" >
Absurdist
Methodology
荒诞主义方法论 < / option >
< option
value = "Absurdist Methodology  荒诞主义方法论" >
Absurdist
Methodology  荒诞主义方法论 < / option >
< option
value = "absurdist_methods" >
absurdist_methods < / option >
< option
value = "Academic Culture" >
Academic
Culture < / option >
< option
value = "Academic Culture 学术文化" >
Academic
Culture
学术文化 < / option >
< option
value = "Academic Culture  学术文化" >
Academic
Culture  学术文化 < / option >
< option
value = "academic_culture_meta" >
academic_culture_meta < / option >
< option
value = "Comedic Psychology" >
Comedic
Psychology < / option >
< option
value = "games_econ_systems" >
games_econ_systems < / option >
< option
value = "Humor &amp; Comedy Studies" >
Humor & amp;
Comedy
Studies < / option >
< option
value = "Humor &amp; Comedy Studies幽默与喜剧研究" >
Humor & amp;
Comedy
Studies幽默与喜剧研究 < / option >
< option
value = "humor_comedy" >
humor_comedy < / option >
< option
value = "Interdisciplinary Chaos" >
Interdisciplinary
Chaos < / option >
< option
value = "Interdisciplinary Chaos 跨学科的混乱" >
Interdisciplinary
Chaos
跨学科的混乱 < / option >
< option
value = "Interdisciplinary Chaos  跨学科混乱" >
Interdisciplinary
Chaos  跨学科混乱 < / option >
< option
value = "Interdisciplinary Chaos  跨学科混沌" >
Interdisciplinary
Chaos  跨学科混沌 < / option >
< option
value = "interdisciplinary_chaos" >
interdisciplinary_chaos < / option >
< option
value = "Meta-Academic Research" >
Meta - Academic
Research < / option >
< option
value = "Meta-Academic Research  元学术研究" >
Meta - Academic
Research  元学术研究 < / option >
< option
value = "Other" >
Other < / option >
< option
value = "Other  其他" >
Other  其他 < / option >
< option
value = "psychology_social" >
psychology_social < / option >
< option
value = "Satirical Economics" >
Satirical
Economics < / option >
< option
value = "Satirical Economics  讽刺经济学" >
Satirical
Economics  讽刺经济学 < / option >
< option
value = "元学术研究" >
元学术研究 < / option >
< option
value = "其他" >
其他 < / option >
< option
value = "喜剧心理学" >
喜剧心理学 < / option >
< option
value = "学术文化" >
学术文化 < / option >
< option
value = "幽默与喜剧研究" >
幽默与喜剧研究 < / option >
< option
value = "荒诞主义方法论" >
荒诞主义方法论 < / option >
< option
value = "跨学科混乱" >
跨学科混乱 < / option >
< option
value = "跨学科混沌" >
跨学科混沌 < / option >
< / select >

< label
for ="sortSelect" > Sort:< / label >
< select
id = "sortSelect"
onchange = "changeSort(this.value)" >
< option
value = "latest"
selected > Latest < / option >
< option
value = "downloads" > Most
Downloaded < / option >
< / select >

< form


class ="search-wrap" method="get" action="/articles.php" >

< input
type = "text"
name = "q"
placeholder = "Search by title..."
value = "" >
< button
type = "submit" > Search < / button >
< / form >

< span


class ="result-count" >


221
ARTICLES < / span >
< / div >

< !-- 文章列表 -->
< div


class ="article-list" >

< div


class ="article-card color-4" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305153441_7a589e1e__.png?v=1772917690"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > 跨学科混沌 < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=897" >
牛顿万有引力定律在极端进食行为中的作用机制与量化研
究——基于抖音博主“良子大胃袋”的进食行为实证分析 < / a >
< / h2 >

< div


class ="card-author" >


大胃菌王                              — 基础力学研究所 < / div >

< p


class ="card-abstract" > 本研究首次将牛顿万有引力定律与抖音头部大胃王博主“良子大胃袋”的极端进食行为进行直接绑定研究，突破了现有研究仅关注大胃王人群胃肠道生理适应、代谢特征的局限，将万有引力从进食行为的“背景环境变量”升级为核心驱动自变量。研究基于牛顿万有引力近地重力场简化模型，构建了食团吞咽重力助推、胃容受性重力介导扩容、胃内压重力调控、胃内空间重力优化四大


理论模型，以“良子大胃袋”2024
~2025
年发布的
15
条标准化无剪辑进食挑战视频为核心样本… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 221 < / span >
< span >⬇ 106 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/897" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=897" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-3" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260301003605_e3c22f98__.jpg?v=1772916051"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > 跨学科混沌 < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=767" >
内卷与荒诞的流体动力学：基于后现代社会学的大学生深夜饮酒“零收益”博弈模型及心理应变屈服强度分析 < / a >
< / h2 >

< div


class ="card-author" >


齐广通                              — 白酒重点实验室研究所 < / div >

< p


class ="card-abstract" > 当代高等教育的规训矩阵中，大学生的主体性正面临结构性的挤压。本文旨在突破传统定性研究的窠臼，将材料力学中的疲劳损伤机制与金融学的高频交易模型跨学科引入社会学领域。通过对深夜烧烤摊这一“液态缓冲带”的酒桌调查，本文量化分析了常温工业级液体（C₂H₅OH水溶液）在消化道内的流体动力学演变，并计算了与之对应的“精神应变屈服强度”。研究表明，凌晨时分的拼酒行为本质上是在低流动性约束下，为实现情绪资产暴力拉升而进行的“高杠杆零收益博弈”。本研究为… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 235 < / span >
< span >⬇ 162 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/767" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=767" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-2" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305161647_a1af8465_b882c579bc95bce4ff479349220f2bc5.jpg?v=1772915592"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Other < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=911" >
单向沉没成本与自我感动机制：当代青年无反馈型依恋关系中的资源错配及破产风险 < / a >
< / h2 >

< div


class ="card-author" >


一减没                              — 纯爱战神高等研究院 < / div >

< p


class ="card-abstract" > 本研究旨在系统性解构当代青年在异性求偶场域中一种被称为“无反馈型依恋”（Non-feedback Attachment，坊间俗称“舔狗”）的极端行为模式。该模式下，行动主体在面临接收方长期的极低或负向反馈时，依然进行无休止的资源（时间、金钱、情绪）单向转移。


方法： 研究融合了行为经济学的“沉没成本谬误”与认知心理学的“认知失调理论”，构建了“自我感动型效用函数模型”（Self - moving
Utility
Model），并通过对50… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 804 < / span >
< span >⬇ 610 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/911" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=911" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-1" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305201718_956513cb__.png?v=1772911167"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > 其他 < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=933" >
论900摄氏度物理定向热学能量波对临床及其刁钻及医闹患者癌细胞的杀灭作用 < / a >
< / h2 >

< div


class ="card-author" >


王鹤达                              — 大连医科大学 < / div >

< p


class ="card-abstract" > 本研究首创性提出900摄氏度物理热学定向能量辐射波对现有人体常见肿瘤治疗的新模式。通过物理+化学药物的联合治疗模式解决现有临床上出现的化疗药物耐药性逐渐增加的问题。体外实验和C57X小鼠动物模型实验结果显示：对常见的肿瘤细胞如HeLa, SiHa, SK-OV-3, HEC-1-A, HepG2的48小时抑制率明显高于临床指南认可的顺铂治疗计量的抑制率；在C57小鼠模型中的抑制率达到了罕见的100 % 。本文通过物理热力学、药物释放模型、细胞移植模… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 289 < / span >
< span >⬇ 174 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/933" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=933" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-4" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305110732_82fa1a6c_.JPG?v=1772904491"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Interdisciplinary Chaos < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=882" >
Lab
Dynamics: Gaslight, Gatekeep, Ghost < / a >
< / h2 >

< div


class ="card-author" >


Dr.Eugeniee                              — 现代Dating文化研究中心 < / div >

< p


class ="card-abstract" > 本文整合社会学、量化金融、非线性动力学与量子隐喻等多学科视角，构建一套系统性分析框架，用以阐释导师—研究生关系背后的深层结构与动态演化逻辑。研究将学术场域视为有限资源约束下的策略博弈空间，导师与研究生在权力、资源、情感三维谱系中展开持续互动。本文引入现代投资组合理论与金融风险指标体系，将导师类比为学术资产组合管理者，学生视为风险收益各异的投资标的，实验室视作动态优化的资产组合：以夏普比率度量学生的风险调整后学术价值，以换手率刻画实验室群… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 100 < / span >
< span >⬇ 35 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/882" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=882" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-3" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260306111624_cf2c58b2__2026-03-06_111337.png?v=1772916408"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > 跨学科混沌 < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=966" >
为什么不能网恋 < / a >
< / h2 >

< div


class ="card-author" >


桃桃不要当答辩                              — National
Clown
University
国立小丑大学 < / div >

< p


class ="card-abstract" > 本文以现实案例为基础，系统探究了过去十年网络环境下异性聊天中过度自我表露与 & quot;假性亲密关系 & quot;形成机制的社会现象。基于社会渗透理论、超人际模型和依恋理论，分析了网络环境如何通过 & quot;加速渗透 & quot;和 & quot;理想化投射 & quot;机制促成虚假亲密感的形成。研究发现，网络聊天中的自我表露深度与速度显著高于线下交往，但这种快速建立的亲密关系往往缺乏现实基础，导致 & quot;假性亲密关系 & quot;的高发。本文交叉疏离和探索了中文文献中史秀雄的 & quot;Irrelationship & quot;概念与西方心理学… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 584 < / span >
< span >⬇ 457 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/966" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=966" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-2" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305144841_207a4a9d_IMG_9145.jpeg?v=1772916148"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Interdisciplinary Chaos < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=892" >
爱欲的巴别塔：当我们谈论失恋时，我们在谈论什么废话——一项融合哲学、社会学与心理学的元分析 < / a >
< / h2 >

< div


class ="card-author" >


弃情绝爱后我成为了新一代苏格拉底                              — 吕克昂哲学博士研究院 < / div >

< p


class ="card-abstract" > 本研究以个人从暧昧拉扯、执念复联到断交绝笔、情感戒断的完整心路为基底，融合哲学、社会学与心理学视角展开元分析，探讨暧昧关系中“拥有时焦虑难安，失去时痛苦倍增”的深层心理。剖析人明知关系无结果却仍执着拉扯，直至痛苦极致后毅然放弃的内在动因，指出失恋时的种种表达，本质是对心理疼痛的回应、对常态丧失的抗拒，更是完成失恋反思、情感戒断、恋爱伦理哲学审视，实现自我认可回归与价值重构的过程。 < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 389 < / span >
< span >⬇ 336 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/892" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=892" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-1" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305032551_1c7d9fab_e9685ccc-3778-4843-ab80-5517f2e2d57e.png?v=1772912332"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Interdisciplinary Chaos < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=878" >
共建的两个账本 - 跨域能力共建工程的“双相效应”  伪实证比较研究 < / a >
< / h2 >

< div


class ="card-author" >


小作坊下料就是猛                              — 好单位 < / div >

< p


class ="card-abstract" > 跨域能力共建工程通常以“技术输出、体系共建、能力复制”的语言呈现，但实践中常出现一种不太体面、却极其稳定的结构：临床与服务端的可见增益可以与学科与生态端的隐性失血同时发生。本文用公开资料比较法选取5个典型案例，分别呈现两种机制路径：其一为“技术帮扶型”，以培训—标准—在地闭环为核心，使能力沉淀在承接方；其二为“资源虹吸 / 依赖锁定型”，以权力重排、现金流控制或病源 / 资金 / 话语权集中为核心，工程虽打着“共建”的旗号，却在运行中削弱本地生态与… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 341 < / span >
< span >⬇ 133 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/878" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=878" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-4" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260304225210_0e333c49_E4D99752509F49F4DB4A852664163969.png?v=1772905662"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Absurdist Methodology < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=867" >
进食熵增与节奏支配：文苹吃播内容宇宙的结构熵—时长耦合模型 < / a >
< / h2 >

< div


class ="card-author" >


Dotkk                              — 广阳小你科技猿 < / div >

< p


class ="card-abstract" > 吃播研究往往能把“感觉”描述得淋漓尽致，但要把这种“感觉”转化为可量化的“证据”


却很难。本文通过分析文苹的吃播，围绕“鸡翅、排骨、大虾、其他”四大类食材，构建了一套既
能看懂、又能复算的分析框架。我们先从整体内容结构入手，看看食物分配是均匀还是集中的；再
针对三类核心食材，比较它们的总数量、总时长以及单位进食时间；最后，我们还会揭秘每类食材
的最快和最慢进食日期，并检验这些差异的稳定性。结果显示：文苹的吃播内容分布明显不均，“… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 254 < / span >
< span >⬇ 67 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/867" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=867" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-3" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260305000625_f7032cdd_1.jpg?v=1772917007"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Interdisciplinary Chaos < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=870" >
基于流体力学的 & quot;
社交尴尬 & quot;
扩散模型：尬聊的湍流理论与黏度系数计算 < / a >
< / h2 >

< div


class ="card-author" >


气氛凝固观测者                              — 社交灾难研究所 < / div >

< p


class ="card-abstract" > 针对社交场合中 & quot;气氛突然安静 & quot;的高频现象，本文将尴尬情绪的群体传播视为一种可建模


的流体扩散过程，并提出社交流体力学分析框架。我们将社交场域抽象为二维连续介质，尴尬度定
义为标量场
φ(x, y, t)，话题转换建模为速度场
v(x, y, t)；采用纳维 - 斯托克斯方程刻画尴尬值的时空演
化，并引入 & quot;
社交雷诺数 & quot;
描述层流 - 湍流相变。通过在
20
场真实聚会中部署多模态传感系统（麦克风
阵列、深度相机、情绪识别），实时采集
289
组尴尬… < / p >

< div


class ="card-meta" >

< span >📅 07
Mar
2026 < / span >
< span >👁 363 < / span >
< span >⬇ 232 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/870" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=870" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-2" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260227230542_79cf8ce5_e3284896a5a2613d89f0e431b03e7862.png?v=1772910799"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > 跨学科混沌 < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=736" >
基于海南高考赋分制度的8级钳工5视频量化评估 < / a >
< / h2 >

< div


class ="card-author" >


意大利西呱                              — 北京师范大学海口附属学校，海南
海口
571126 < / div >

< p


class ="card-abstract" > 摘要：鉴于用户8级钳工5于社交平台发布的视频类型单一、流程相似，本文创新性提出“接缝衡量——时长衡量——热度衡量”三位一体评估法。结合海南省高考赋分制度宽容度高、强调性强、量化公平的显著优势，设计了完整的8级钳工5视频量化评估制度，将主观评价转化为直观数据评价，将主观结论上升为有理有据的量化结论，显著提高了对“8级钳工5”视频评价的有效性、可信度。本文使用8级钳工5的典型视频检验评估效果，并得出评估较为有效的结论。本文所提出的视频评估制… < / p >

< div


class ="card-meta" >

< span >📅 06
Mar
2026 < / span >
< span >👁 334 < / span >
< span >⬇ 97 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/736" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=736" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< div


class ="article-card color-1" >

< !-- 封面图 -->
< div


class ="card-cover" >

< img
src = "https://static.jokerofacademics.com/uploads/covers/20260304221904_f7646950_258001bde5b3da62341b8d37d2942b09.jpg?v=1772915676"
alt = "Cover"
loading = "lazy"
onerror = "this.parentElement.innerHTML='<span class=\'no-cover\'>📄</span>'" >
< / div >

< !-- 内容 -->
< div


class ="card-body" >

< span


class ="card-tag" > Academic Culture < / span >

< h2


class ="card-title" >

< a
href = "/article.php?id=859" >
网红宠物IP爆火现象下当代青年精神文化与物质诉求研究——以草地牛、噜噜、露比、耄耋为例 < / a >
< / h2 >

< div


class ="card-author" >


奥德彪                              — 霍格沃茨魔法学院沈阳校区 < / div >

< p


class ="card-abstract" > 随着互联网技术和短视频平台的发展，草地牛、噜噜、露比、耄耋等网红宠物IP快速走红，成为当代青年社交和精神生活的重要组成部分。本文以这四个网红宠物IP为研究对象，采用文献研究法，分析其爆火现象背后当代青年的精神文化诉求与物质诉求。研究发现，网红宠物IP的爆火是青年精神压力、情感缺失与现实条件约束共同作用的结果。在精神文化层面，青年通过这些IP获得情感代偿与心理疗愈，构建身份认同与圈层归属，其价值观念也从内卷、追求完美转向松弛、悦己与情绪自… < / p >

< div


class ="card-meta" >

< span >📅 06
Mar
2026 < / span >
< span >👁 717 < / span >
< span >⬇ 489 < / span >
< span >
💬
< span


class ="waline-comment-count"


data - path = "/article/859" >
0
< / span >
< / span >
< a


class ="card-read-more" href="/article.php?id=859" >


Read
More →
< / a >
< / div >
< / div >

< / div > <!-- /.article - card -->
< / div >

< !-- 分页 -->
< div


class ="pagination" >

< !-- 上一页 -->
< a
href = "?page=1" >‹ Prev < / a >

< !-- 页码（最多显示
5
个，当前页居中）-->
< a
href = "?page=1" > 1 < / a >
< span


class ="current" > 2 < / span >

< a
href = "?page=3" > 3 < / a >
< a
href = "?page=4" > 4 < / a >
< span


class ="disabled" > … < / span >

< !-- 下一页 -->
< a
href = "?page=3" > Next › < / a >
< / div >

< / div > <!-- /.page - wrap -->

< div


class ="color-divider" > < div class ="c1" > < / div > < div class ="c2" > < / div > < div class ="c3" > < / div > < div class ="c4" > < / div > < / div >

< footer >
< div


class ="footer-inner" >

< div


class ="footer-bottom" >

< span >© 2025
Joker 🤡f
Academics.Published
under
CC
BY
4.0.
· < a
href = "/" > Home < / a >
· < a
href = "/#submit" > Submit < / a >
< / span >
< / div >
< / div >
< / footer >

< script >
function
filterCategory(val)
{
    const
url = new
URL(window.location.href);
url.searchParams.delete('page'); // 切换分类时回到第1页
if (val)
{
    url.searchParams.set('category', val);
} else {
    url.searchParams.delete('category');
}
window.location.href = url.toString();
}
function
changeSort(val)
{
    const
url = new
URL(window.location.href);
url.searchParams.delete('page'); // 切换排序时回到第1页
if (val & & val !== 'latest')
{
    url.searchParams.set('sort', val);
} else {
    url.searchParams.delete('sort');
}
window.location.href = url.toString();
}
< / script >

< !-- Waline
评论数统计（仅用于列表页展示评论数量）-->
< script
type = "module" >
import

{commentCount}
from

'https://cdn.jsdelivr.net/npm/@waline/client@3.12.2/dist/waline.js';
commentCount({
    serverURL: 'https://jokerofacademics.com/waline',
    selector: '.waline-comment-count',
});
< / script >

< script
defer
src = "https://static.cloudflareinsights.com/beacon.min.js/v8c78df7c7c0f484497ecbca7046644da1771523124516"
integrity = "sha512-8DS7rgIrAmghBFwoOTujcf6D9rXvH8xm8JQ1Ja01h9QX8EzXldiszufYa4IFfKdLUKTTrnSFXLDkUEOTrZQ8Qg=="
data - cf - beacon = '{"version":"2024.11.0","token":"790715ec2f174982a58d79a241005b1d","r":1,"server_timing":{"name":{"cfCacheStatus":true,"cfEdge":true,"cfExtPri":true,"cfL4":true,"cfOrigin":true,"cfSpeedBrain":true},"location_startswith":null}}'
crossorigin = "anonymous" > < / script >
< / body >
< / html >
采集出所有文章Id  给我py