# CIR 多模组汉化包 Pro / CIR Mod Localization Pro

<img src="pack.png" width="160" alt="CIR localization pack icon">

**Minecraft: Java Edition 1.21.1 · v1.4 · 资源包格式 / Pack format 34**

现有包内署名 / Existing pack credits: **Safe_Saffawa & Real_Infinistar**

## 中文简介

为 CIR 整合包维护的中文补译、译名修订和模组指南资源包。当前仓库保留 **61 个资源命名空间**，含 **89 份语言文件**及 **289 份指南相关文件**；其中 **持续支持 35 项，暂停支持 24 项，可能恢复支持 2 项**。持续维护范围包括 AE2 及附属指南、机械动力及在用附属、幽邃黑暗、神化系列、灾变、FTB Quests 等；新生魔艺、植物魔法相关历史资源及其他暂停条目见下方支持状态表。

覆盖范围以本仓库实际文件为准：部分模组只包含少量补译或译名覆盖，不代表所有模组均已完整汉化。资源目录中的旧命名空间也单独计数，因此命名空间数量不等于独立模组数量。

### 安装

1. 从 [Releases](https://github.com/CIR-Server/CIR-Mod-Localization/releases/latest) 下载 `CIR-Mod-Localization-Pro-v1.4.zip`。
2. 放入实例的 `resourcepacks` 文件夹，保持 ZIP 格式，在游戏中启用，并置于需要覆盖的资源包上方。
3. 切换为简体中文，按 F3+T 重载资源或重新启动游戏。

本包主要提供简体中文，个别模组附有繁体中文或英文键值。对应模组未安装时，其资源不会生效。本仓库仅提供资源包，矿石描边在 [CIR-Ore-Outlines](https://github.com/CIR-Server/CIR-Ore-Outlines) 单独维护。

### 许可与署名

包内 AE2 系列指南取自 **CFPAOrg / Minecraft-Mod-Language-Package**。其原有署名和 **CC BY-NC-SA 4.0（署名—非商业性使用—相同方式共享）** 要求保留，不能将这些内容整体改为 MIT。CIR 在本发布版中的原创补译与文档也按 CC BY-NC-SA 4.0 分享；所引用的模组原文和基础素材保留原作者权利。见 [LICENSE](LICENSE)、[ATTRIBUTION.md](ATTRIBUTION.md) 与 [CREDITS.md](CREDITS.md)。

原作者及共同贡献者可在确认署名方式后补充至 [CONTRIBUTORS.md](CONTRIBUTORS.md)，不预填未经确认的账号或邮箱。补译、纠错与补充署名的方法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## English introduction

A Chinese localization resource pack maintained for the CIR modpack, containing translation additions, terminology corrections and localized mod guides. The repository retains **61 resource namespaces**, with **89 language files** and **289 guide-related files**: **35 entries are actively supported, 24 are paused, and support may resume for 2 entries**. Active coverage includes AE2 and addon guides, Create and currently used addons, Deeper and Darker, Apotheosis and addons, Cataclysm, FTB Quests and more. Historical Ars/Botania-related content and other paused entries are identified in the support-status tables below.

Coverage varies by namespace. Some entries are small translation overrides rather than complete translations. Legacy namespaces are listed separately, so the namespace total is not the number of distinct mods. See the inventory below for the actual shipped files.

### Installation

1. Download `CIR-Mod-Localization-Pro-v1.4.zip` from [Releases](https://github.com/CIR-Server/CIR-Mod-Localization/releases/latest).
2. Keep the ZIP intact, place it in the instance's `resourcepacks` folder, enable it, and put it above packs whose translations should be overridden.
3. Select Simplified Chinese, then reload resources with F3+T or restart Minecraft.

The pack primarily targets Simplified Chinese. A few namespaces also contain Traditional Chinese or English overrides. Resources for uninstalled mods remain unused. Ore outlines are maintained separately in [CIR-Ore-Outlines](https://github.com/CIR-Server/CIR-Ore-Outlines).

### License and contributors

The bundled AE2-family guides originate from **CFPAOrg / Minecraft-Mod-Language-Package** and retain **CC BY-NC-SA 4.0** and their attribution. Those files are not relicensed under MIT. CIR's original localization contributions and documentation in this release are shared under CC BY-NC-SA 4.0 as well; retained upstream text and artwork keep their respective ownership. See [LICENSE](LICENSE), [ATTRIBUTION.md](ATTRIBUTION.md) and [CREDITS.md](CREDITS.md).

Original authors and joint contributors can be added to [CONTRIBUTORS.md](CONTRIBUTORS.md) after their preferred credit and contribution scope are confirmed. Unconfirmed accounts and email addresses are not pre-filled. Contribution and credit-update instructions are in [CONTRIBUTING.md](CONTRIBUTING.md).

## 支持状态与已包含资源 / Support status and included resources

核对日期：**2026-11-23**。基于本地 **CIR-MODPACK-v4.1（Minecraft 1.21.1）** 客户端模组 JAR 元数据，并结合维护者确认的服务端使用情况与后续计划，对已列出的 61 个资源命名空间逐项分类：**持续支持 35 项，暂停支持 24 项，可能恢复支持 2 项**。

Checked on **2026-11-23** against the local **CIR-MODPACK-v4.1 (Minecraft 1.21.1)** client mod metadata, together with maintainer-confirmed server usage and future plans: **35 actively supported entries, 24 paused entries, and 2 entries for which support may resume** across the 61 listed resource namespaces.

### 分类规则 / Classification rules

- **持续支持 / Active**：对应模组仍在当前客户端或服务端使用，并且未被下述系列暂停策略覆盖。Terralith 根据维护者确认的服务端使用情况持续支持；`expatternprovider` 按其对应的 ExtendedAE 项目判定。 / The target mod is still used by the client or server and is not covered by a family-wide pause below. Terralith remains supported based on maintainer-confirmed server usage; the legacy `expatternprovider` namespace follows the installed ExtendedAE project.
- **暂停支持 / Paused**：新生魔艺、植物魔法及相关模组自 **2025-12** 暂停；Mekanism 及相关模组自 **2025-07** 暂停。其他不在当前客户端中、且未另行确认持续支持或可能恢复支持的旧条目归入暂停支持，不推定其历史暂停日期。 / Ars Nouveau, Botania and related mods have been paused since **2025-12**; Mekanism and related mods since **2025-07**. Other historical entries absent from this client are paused unless active support or possible resumption has been separately confirmed; no historical date is inferred.
- **可能恢复支持 / Support may resume**：锦制乐事与应用机械未来可能重新纳入维护，目前没有确定的恢复时间。 / Supplementaries Delight and Applied Kinetics may return to the maintenance scope in the future; no resumption date is committed.
- 暂停支持表示不再持续跟进相应模组版本；已有历史资源仍保留在包中。状态反映本汉化项目的维护范围，不代表原模组自身停止维护。 / Paused support describes this localization project's maintenance scope. Existing historical files remain available; the status does not imply that the upstream mod is discontinued.

### 系列维护时间 / Family maintenance history

| 系列 / Family | 状态 / Status | 暂停时间 / Paused since | 说明 / Notes |
|---|---|---|---|
| 新生魔艺及相关模组 / Ars Nouveau and related mods | 暂停支持 / Paused | 2025-12 | 包含下表中的 Ars Creo、Ars Elemental、Ars Nouveau、Ars Technica、arseng、StarbuncleMania / Includes the six listed Ars-related entries |
| 植物魔法及相关模组 / Botania and related mods | 暂停支持 / Paused | 2025-12 | 当前资源清单中的 Applied Botanics 同属此类 / Applied Botanics in the current inventory follows this policy |
| Mekanism 及相关模组 / Mekanism and related mods | 暂停支持 / Paused | 2025-07 | 当前包未列出独立 Mekanism 资源命名空间，因此此历史政策不额外计入下面 61 项资源统计 / No separate Mekanism namespace is shipped in the current inventory, so this historical policy is not an extra entry in the 61-namespace totals |

语言与指南列为文件数量；指南可能包含 Markdown、图片及 SNBT，不单指指南页数。 / Language and guide columns count files; guides include Markdown, images and SNBT, not only pages.

### 持续支持 / Active support (35)

| 模组／项目 / Mod or project | 命名空间 / Namespace | 语言 / Language files | 指南 / Guide files | 核对说明 / Notes |
|---|---|---:|---:|---|
| Advanced AE | `advanced_ae` | 0 | 18 | 当前客户端已安装 / Installed in the current client |
| Applied Energistics 2 | `ae2` | 1 | 143 | 当前客户端已安装 / Installed in the current client |
| AE2 Lightning Tech | `ae2lt` | 2 | 0 | 当前客户端已安装 / Installed in the current client |
| AE2WTLib | `ae2wtlib` | 0 | 7 | 当前客户端已安装 / Installed in the current client |
| Apotheosis | `apotheosis` | 3 | 0 | 当前客户端已安装 / Installed in the current client |
| Apothic Attributes | `apothic_attributes` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Apothic Compats | `apothic_compats` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| AppliedFlux | `appflux` | 1 | 15 | 当前客户端已安装 / Installed in the current client |
| Caelus API | `caelus` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| L_Ender's Cataclysm 1.21.1 | `cataclysm` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create: CC Better Recipes | `ccbr` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Combat Roll | `combat_roll` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create | `create` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Confectionery | `create_confectionery` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Let The Adventure Begin | `create_ltab` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create: Power Loader | `create_power_loader` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| create: things and misc | `create_things_and_misc` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Crafts & Additions | `createaddition` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Deco | `createdeco` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Diesel Generators | `createdieselgenerators` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create Stock Bridge | `createstockbridge` | 2 | 0 | 当前客户端已安装 / Installed in the current client |
| Deeper and Darker | `deeperdarker` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Expanded Delight | `expandeddelight` | 2 | 0 | 当前客户端已安装 / Installed in the current client |
| ExtendedAE (legacy resource namespace) | `expatternprovider` | 1 | 0 | 对应已安装的 ExtendedAE；旧命名空间保留兼容 / Legacy namespace of installed ExtendedAE; retained for compatibility |
| ExtendedAE | `extendedae` | 0 | 68 | 当前客户端已安装 / Installed in the current client |
| Create: Extra Gauges | `extra_gauges` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| FTB Quests | `ftbquests` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Infernal Mobs | `infernalmobs` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Create: Interiors | `interiors` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| My Nether's Delight | `mynethersdelight` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Ocean's Delight | `oceansdelight` | 2 | 0 | 当前客户端已安装 / Installed in the current client |
| Regions Unexplored | `regions_unexplored` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Sable | `sable` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Supplementaries | `supplementaries` | 1 | 0 | 当前客户端已安装 / Installed in the current client |
| Terralith | `terralith` | 26 | 0 | 服务端仍在使用，按维护者确认持续支持 / Still used on the server; continued support confirmed by the maintainer |

### 暂停支持 / Paused support (24)

| 模组／项目 / Mod or project | 命名空间 / Namespace | 语言 / Language files | 指南 / Guide files | 暂停时间 / Paused since | 原因 / Reason |
|---|---|---:|---:|---|---|
| Anvil Repairing | `anvilrepairing` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| Applied Botanics | `appbot` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| Ars Creo | `ars_creo` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| Ars Elemental | `ars_elemental` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| Ars Nouveau | `ars_nouveau` | 1 | 38 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| Ars Technica | `ars_technica` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| arseng | `arseng` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| Create: Connected | `create_connected` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| Create: Factory Logistics | `create_factory_logistics` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| create_mechanical_extruder | `create_mechanical_extruder` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| createsifter | `createsifter` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| crystal_clear | `crystal_clear` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| design_decor | `design_decor` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| dndecor | `dndecor` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| miners_delight | `miners_delight` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| moderntrainparts | `moderntrainparts` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| nethersdelight | `nethersdelight` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| starbunclemania | `starbunclemania` | 1 | 0 | 2025-12 | 新生魔艺／植物魔法相关，按维护计划暂停 / Ars or Botania family; paused by maintenance policy |
| tofucraft | `tofucraft` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| tofucreate | `tofucreate` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| tofudelight | `tofudelight` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| totemfactory | `totemfactory` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| vinery | `vinery` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |
| Weather2 | `weather2` | 1 | 0 | 未指定 / Unspecified | 当前客户端未安装；历史暂停时间未指定 / Absent from the current client; historical pause date unspecified |

### 可能恢复支持 / Support may resume (2)

| 模组／项目 / Mod or project | 命名空间 / Namespace | 语言 / Language files | 指南 / Guide files | 说明 / Notes |
|---|---|---:|---:|---|
| 锦制乐事 / Supplementaries Delight | `supplementariesdelight` | 1 | 0 | 可能恢复支持，尚无确定时间 / Support may resume; no date committed |
| 应用机械 / Applied Kinetics | `createappliedkinetics` | 1 | 0 | 可能恢复支持，尚无确定时间 / Support may resume; no date committed |

## 打包 / Build

运行 / Run `python tools/build_pack.py` with Python 3.
输出 / Output: `dist/CIR-Mod-Localization-Pro-v1.4.zip`.

首次公开发布仅修正一处 AE2 语言文件末尾逗号，并更新发布说明与资源包显示版本；已有译文、指南与图片保持原内容。
The first public release removes a trailing comma from one AE2 language file and updates publication metadata; existing translation wording, guides and images are preserved.


