from typing import Collection
from notion.client import NotionClient
from notion.block import  EmbedBlock
from notion.block import CodeBlock, PageBlock ,PDFBlock,ToggleBlock,ColumnBlock

client = NotionClient(token_v2="e8c767d3d31c71c651bfe1ba8a85c4fd7f396e1cd1e67526a51b1c99e680af9aca30eb3d75edc7b5c09adf9a6ad243b7d0811c1544f947852b2a4ec750751b3b0d7e4b24367a99e58dc9e192cebc")

"""from notion.collection import CollectionRowBlock

Page1=client.get_block('https://www.notion.so/b663986665cb456a86e1280f643d6f74')
page2=client.get_block('https://www.notion.so/3d7de562dd544609851569231cd6e942')
pathsPDF=[
          {'page':['PDF/النباتات اللاوعائية اللابذرية 1.pdf','PDF/النباتات الوعائية اللابذرية 2.pdf']},
          {'page':['PDF/النباتات الوعائية البذرية 1.pdf','PDF/النباتات الوعائية البذرية 2.pdf']}
         ]
print(pathsPDF[0]['page'][0])
Page1.children.add_new(ToggleBlock).title='الملفات'
Page1.children[0].children.add_new(ToggleBlock).title='الملف الاول'
Page1.children[0].children.add_new(ToggleBlock).title='الملف الثاني'
print('1')
Page1.children[0].children[0].children.add_new(PDFBlock).Uplode_file(pathsPDF[0]['page'][0])"""
Page1=client.get_block('https://www.notion.so/Personal-Home-1adb0b26045d48cda66c323b0ba2b5a4')
print(Page1.children[1].children.add_new(ColumnBlock))
print('done')