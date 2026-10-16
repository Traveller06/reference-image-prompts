# 参考图风格解析与图片提示词

版本：1.0.0。一个只含技能的 ChatGPT / Codex 插件，用于将参考图解析为可直接复制的中文图片生成提示词。

## 能力

- 分别指定风格、动作、构图、人物身份参考，防止参考串用。
- 解析色彩、曝光、黑位、光源方向、景深及材质。
- 按要求替换食物、人物或环境，检查单帧动作和道具接触。
- 保持系列首帧画风，默认正文最多1024字符。
- 仅编写提示词，不自动生成图片，不需要服务器或付费API。

## 使用

上传参考图后说明：

> 第一张定风格，第二张仅参考递糕动作，食物改为绿豆糕，仅输出1024字符以内的图片提示词。

也可以说：

> 保持两张人物参考图的色调、光影和材质，写一幅河畔村景提示词。

风格参考不自动意味着复制人物身份。跨对话时应重新提供关键参考图；不能保证图像模型完全复现画风。

## 插件结构

- `plugin.json`：便携插件清单。
- `.codex-plugin/plugin.json`：兼容清单。
- `skills/reference-image-prompts/SKILL.md`：主工作流。
- `skills/reference-image-prompts/references/examples.md`：边界示例。
- `skills/reference-image-prompts/scripts/check_prompt_length.py`：字符统计。

## 在 GPT Work 中使用

将本项目打包后，通过支持插件导入的 GPT Work 插件页面安装，再从聊天框的插件选择入口使用。上传 GitHub 本身不会自动安装插件。

## 本地验证与打包

运行字符统计脚本，传入仅含提示词正文的 UTF-8 文件：

```sh
python skills/reference-image-prompts/scripts/check_prompt_length.py prompt.txt --limit 1024
```

将此目录的内容整体压缩，确保压缩包根部为 `plugin.json`、`skills/` 和可选的 `.codex-plugin/`。不要把整个视频仓库压入插件包。上传时使用 GPT Work 插件页的“上传插件压缩包”入口。

## 维护

更新时保持插件名称与技能名称稳定，同时同步两份清单的版本和展示信息。不要上传私人参考图片、对话记录、凭证或生成视频。

## 开源许可证

本项目采用 MIT 许可证，允许使用、修改和再分发，详见 LICENSE。参考图片与生成模型服务不包含在本项目内。
