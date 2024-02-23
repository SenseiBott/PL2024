import re

def convertHeading(markdown, level):
  return re.sub(r'^{} (.*)$'.format('#' * level), r'<h{0}>\1</h{0}>'.format(level), markdown, flags=re.MULTILINE)

def convertItalic(markdown):
  return re.sub(r'_(.*?)_', r'<em>\1</em>', markdown)

def convertBold(markdown):
  return re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)

def convertBlockquote(markdown):
  return re.sub(r'^> (.*)$', r'<blockquote>\1</blockquote>', markdown, flags=re.MULTILINE)

def convertLists(markdown):
  lines = markdown.splitlines() 
  convertedLines = []
  inList = False

  for line in lines:
    if re.match(r"^\d+\.\s+|\-\s+", line):
      tag = "<ol>" if re.match(r"^\d+\.\s+", line) else "<ul>"
      convertedLines.append(tag) if not inList else None 
      inList = True
      convertedLines.append(re.sub(r"^\d+\.\s+|\-\s+", "<li>", line))
    elif line.strip() == "":
      convertedLines.append("</ol></ul>") if inList else None 
      inList = False
      convertedLines.append(line)
    else:
      convertedLines.append("</ol></ul>") if inList else None 
      inList = False
      convertedLines.append("<p>" + line + "</p>")

  convertedLines.append("</ol></ul>") if inList else None  
  return "\n".join(convertedLines)

def convertCode(markdown):
  return re.sub(r'`(.*)`', r'<code>\1</code>', markdown)

def convertHorizontalRules(markdown):
    return re.sub(r'^---$', r'<hr>', markdown, flags=re.MULTILINE)

def convertLinks(markdown):
  return re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

def convertImages(markdown):
  return re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img alt="\1" src="\2">', markdown)

def convertMDtoHTML(markdowninput, htmloutput):
  with open(markdowninput, 'r') as file:
    markdown = file.read()

  markdown = convertHeading(markdown, 1)
  markdown = convertHeading(markdown, 2)
  markdown = convertHeading(markdown, 3)
  markdown = convertItalic(markdown)
  markdown = convertBold(markdown)
  markdown = convertBlockquote(markdown)
  markdown = convertHorizontalRules(markdown)
  markdown = convertLists(markdown)
  markdown = convertCode(markdown)
  markdown = convertImages(markdown)
  markdown = convertLinks(markdown)

  with open(htmloutput, 'w') as file:
    file.write(markdown)
  
  
convertMDtoHTML('example.md', 'output.html')